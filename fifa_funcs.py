# -*- coding: utf-8 -*-
"""
@author: MWatson717
"""

#This file contains functions used for the project

import requests
import lxml.html as lh
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup, Comment


def get_all_links(url, lst=[], league=True):
    '''
    This funciton takes a URL and returns a list of URLs as well as a URL to next years homepage
    
    Parameters
    ----------
    url : str
        a URL to the homepage of a Football Reference season/tournament
    lst : list
        a empty list that the output will be sent to
    league: bool
        Default True, used to select correct URLs for given years data
        
    Returns
    -------
    lst : list
        list of lists of URLs of desired data tables, with each sublist corresponding to one year 
    '''
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    links = doc.xpath('//div[@id="inner_nav"]//@href')
    
    try:
        nex = doc.xpath('//div[@class="prevnext"]/a[@class="button2 next"]/@href') #selecting URL for next year
        nex = 'https://fbref.com' + nex[0]
    except:
        pass
    
    if league == True:    #Need this to be able to use for league/tournament data
        links[:] = [x for x in links if 'players' in x] #there isnt 'players' in URLs for tournmants
        
    sub_str = ['stats', 'shooting', 'passing/', 'possession', 'defense', 'misc'] #need / in passing because theres another link for passing_types
    
    ls = [i for i in links if any(sub in i for sub in sub_str)] #selecting only desired URLs
    
    ls = list(set(ls)) #removing duplicates
    
    ls2 = []
    
    for i in ls: #added https: before URLs
        x = 'https://fbref.com' + i
        ls2.append(x)
        
    ls2.sort() #links come in different order everytime code is ran, sort alphabetically for ease
    
    lst.append(ls2)
    
    if nex:
        get_all_links(nex, lst, league) #recursively call function to get links for following year if it exists
        
    return lst



def scraper(url, league = True):
    '''
    This function takes a URL and returns a datafrme from it
    
    Parameters
    ----------
    url : str
        URL to a specific Football Reference data table  
    league : bool
        Default 'True'; data is stored differently for League vs International competitions, need to scrape differently

    Returns
    -------
    df : DataFrame
        A DataFrame of the data from url
    '''
    if league == True:
        lst = pd.read_html(url, header=1)
        df = lst[0]
    else:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        lst = []
        for comment in soup.find_all(string=lambda text:isinstance(text,Comment)):
            data = BeautifulSoup(comment,"lxml")
            for items in data.select("table tr"):
                tds = [' '.join(item.text.split()) for item in items.select("th,td")]
                lst.append(tds)
    
        df = pd.DataFrame(lst[1:])
        df.columns = df.iloc[0]
        df = df[1:]
    
    return df


def get_data(lst, league = True):
    '''    
    This function takes a list of URLs and returns a dataframe for each URL
    
    Parameters
    ----------
    lst : list
        list of URLs created from 'get_all_links' function
    league : bool
        Default 'True'; used for scraper function to select data correctly
    
    Returns
    -------
    standard : DataFrame
        Standard stats dataframe
    shooting : DataFrame
        Shooting stats dataframe
    passing : DataFrame
        Passing stats dataframe
    misc : DataFrame
        Miscellaneous stats dataframe
    pos : DataFrame
        Possession stats dataframe
    defense : DataFrame
        Defense stats dataframe
    '''
    standard = scraper(lst[5], league)
    shooting = scraper(lst[4], league)
    passing  = scraper(lst[2], league)
    misc     = scraper(lst[1], league)
    pos      = scraper(lst[3], league)
    defense  = scraper(lst[0], league)
    
    return standard, shooting, passing, misc, pos, defense


def clean_std(df, comp):
    '''
    This funcion cleans the 'Standard' data table from Football Reference
    
    Parameters
    ----------
    df : DataFrame
        Standard stats dataframe
    comp: str
        What type of competiton data is from, options are: 'League', 'Club Cup' or 'Int' 
        
    Returns
    -------
    data : DataFrame
        Cleaned Standard stats dataframe
    '''
    df = df.drop_duplicates(keep = False)  #column names are repeated after every 25 rows, so row 26, 51 etc
    df = df.replace(',', '', regex=True)   #minutes score as 1,777, we want 1777
    
    if comp == 'League':
        strs = df.iloc[:, 1:6]                                      #not inclusive 
        ints = df.iloc[:, np.r_[6:11, 12:14, 15:19]].astype(float)  #not inclusive
    elif comp == 'Club Cup':
        df = df.replace('', '0', regex=True)#issue with Champs league 20-21, player with missing minutes
        strs = df.iloc[:, 1:5]                                      
        ints = df.iloc[:, np.r_[5:10, 11:13, 14:18]].astype(float)
    elif comp == 'Int':
        df = df.replace('', '0') # issue with 2018 WC data
        strs = df.iloc[:, 1:4]
        ints = df.iloc[:, np.r_[4:9, 10:12, 13:17]].astype(float) #different columns for each competition type
        
    data = pd.concat([strs, ints], axis=1)
    
    return data


def clean_shoot(df, comp):
    '''
    This funcion cleans the 'Shooting' data table from Football Reference
    
    Parameters
    ----------
    df : DataFrame
        Shooting stats dataframe
    comp: str
        What type of competiton data is from, options are: 'League', 'Club Cup' or 'Int' 

    Returns
    -------
    data : DataFrame
        Cleaned Shooting stats dataframe
    '''
    df = df.drop_duplicates(keep = False)
    df = df.replace(',', '', regex=True) 
    
    if comp == 'League':
        strs = df.iloc[:, 1:6]       
        ints = df.iloc[:, [6, 10, 11, 17, 18]].astype(float)
    elif comp == 'Club Cup':
        df = df.replace('', '0', regex=True) 
        strs = df.iloc[:, 1:5]       
        ints = df.iloc[:, [5, 9, 10, 16, 17]].replace('', np.NaN).astype(float)
    elif comp == 'Int':
        df = df.replace('', '0') 
        strs = df.iloc[:, 1:4]
        ints = df.iloc[:, [4, 8, 9, 15, 16]].replace('', np.NaN).astype(float)
        
    data = pd.concat([strs, ints], axis=1)
    data = data.rename(columns = {'Dist':'Avg_Sh_Dist'}) #rename column regardless of comp type
    
    return data


def clean_pass(df, comp):
    '''
    This funcion cleans the 'Passing' data table from Football Reference
    
    Parameters
    ----------
    df : DataFrame
        Passing stats dataframe
    comp: str
        What type of competiton data is from, options are: 'League', 'Club Cup' or 'Int' 

    Returns
    -------
    data : DataFrame
        Cleaned Passing stats dataframe
    '''
    df = df.drop_duplicates(keep = False)
    df = df.replace(',', '', regex=True) 
    
    if comp == 'League':
        strs = df.iloc[:, 1:6]
        ints = df.iloc[:, np.r_[12:16, 17:19, 20:22, 26:30]].astype(float)
        data = pd.concat([strs, ints], axis=1)
        data = data.rename(columns = {'TotDist':'Pas_TotDist', 'PrgDist':'Pas_PrgDist', 'Cmp.1':'Cmp_S', 
                                      'Att.1':'Att_S', 'Cmp.2':'Cmp_M', 'Att.2':'Att_M', 'Cmp.3':'Cmp_L', 
                                      'Att.3':'Att_L', '1/3':'Pas_A3'}) #different col order, rename for each compo
    elif comp == 'Club Cup':
        df = df.replace('', '0', regex=True) 
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[11:15, 16:18, 19:21, 25:29]].replace('', np.NaN).astype(float)
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Nation', 'Pos', 'Squad', 'Pas_TotDist', 'Pas_PrgDist', 'Cmp_S', 'Att_S', 
                        'Cmp_M', 'Att_M', 'Cmp_L', 'Att_L', 'KP', 'Pas_A3','PPA', 'CrsPA']
    elif comp == 'Int':
        df = df.replace('', '0') 
        strs = df.iloc[:, 1:4]
        ints = df.iloc[:, np.r_[10:14, 15:17, 18:20, 24:28]].replace('', np.NaN).astype(float)
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Pos', 'Squad', 'Pas_TotDist', 'Pas_PrgDist','Cmp_S', 'Att_S', 
                        'Cmp_M', 'Att_M', 'Cmp_L', 'Att_L', 'KP', 'Pas_A3','PPA', 'CrsPA']

    return data  


def clean_misc(df, comp):
    '''
    This funcion cleans the 'Defense' data table from Football Reference
    
    Parameters
    ----------
    df : DataFrame
        Miscellaneous stats dataframe
    comp: str
        What type of competiton data is from, options are: 'League', 'Club Cup' or 'Int' 
        
    Returns
    -------
    data : DataFrame
        Cleaned Miscellaneous stats dataframe
    '''
    df = df.drop_duplicates(keep = False)
    df = df.replace(',', '', regex=True) 
    
    if comp == 'League':
        strs = df.iloc[:, 1:6]
        ints = df.iloc[:, np.r_[11:16, 18:24]].astype(float)    
    elif comp == 'Club Cup':
        df = df.replace('', '0', regex=True)
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[10:15, 17:23]].replace('', np.NaN).astype(float)
    elif comp == 'Int':
        df = df.replace('', '0') 
        strs = df.iloc[:, 1:4]
        ints = df.iloc[:, np.r_[9:14, 16:22]].replace('', np.NaN).astype(float)
        
    data = pd.concat([strs, ints], axis=1)
    data = data.rename(columns = {'Won':'AD_Won', 'Lost':'AD_Lost'})
    
    return data


def clean_pos(df, comp):
    '''
    This funcion cleans the 'Possession' data table from Football Reference
    
    Parameters
    ----------
    df : DataFrame
        Possession stats dataframe
    comp: str
        What type of competiton data is from, options are: 'League', 'Club Cup' or 'Int' 

    Returns
    -------
    data : DataFrame
        Cleaned Possession stats dataframe
    '''
    df = df.drop_duplicates(keep = False)
    df = df.replace(',', '', regex=True)
    
    if comp == 'League':
        strs = df.iloc[:, 1:6]
        ints = df.iloc[:, np.r_[9:18, 19:31, 32]].astype(float)
        data = pd.concat([strs, ints], axis=1)
        data = data.rename(columns = {'Def Pen':'Tch_DP', 'Def 3rd':'Tch_D3', 'Mid 3rd':'Tch_M3',
                                      'Att 3rd':'Tch_A3', 'Att Pen':'Tch_AP', 'Succ':'Dr_Succ',
                                      'Att':'Dr_Att', '#Pl':'Num_Dr_Past','TotDist':'Cr_TotDist', 
                                      'PrgDist':'Cr_PrgDist', 'Prog':'Cr_Prog', '1/3':'Cr_A3',
                                      'Prog.1':'Prog_Pas_Rec'})   
    elif comp == 'Club Cup':
        df = df.replace('', '0', regex=True)
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[8:17, 18:30, 31]].replace('', np.NaN).astype(float)
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Nation', 'Pos', 'Squad','Touches', 'Tch_DP', 'Tch_D3', 'Tch_M3','Tch_A3', 
                        'Tch_AP', 'Live', 'Dr_Succ', 'Dr_Att', 'Num_Dr_Past', 'Megs','Carries', 'Cr_TotDist', 
                        'Cr_PrgDist', 'Cr_Prog', 'Cr_A3', 'CPA', 'Mis', 'Dis', 'Targ', 'Rec', 'Prog_Pas_Rec']
    elif comp == 'Int':
        df = df.replace('', '0') 
        strs = df.iloc[:, 1:4]   
        ints = df.iloc[:, np.r_[7:16, 17:29, 30]].replace('', np.NaN).astype(float)
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Pos', 'Squad','Touches', 'Tch_DP', 'Tch_D3', 'Tch_M3','Tch_A3', 
                        'Tch_AP', 'Live', 'Dr_Succ', 'Dr_Att', 'Num_Dr_Past', 'Megs','Carries', 'Cr_TotDist', 
                        'Cr_PrgDist', 'Cr_Prog', 'Cr_A3', 'CPA', 'Mis', 'Dis', 'Targ', 'Rec', 'Prog_Pas_Rec']
    return data


def clean_def(df, comp):
    '''
    This funcion cleans the 'Defense' data table from Football Reference
    
    Parameters
    ----------
    df : DataFrame
        Defense stats dataframe
    comp: str
        What type of competiton data is from, options are: 'League', 'Club Cup' or 'Int' 

    Returns
    -------
    data : DataFrame
        Cleaned Defense stats dataframe
    '''
    df = df.drop_duplicates(keep = False)
    df = df.replace(',', '', regex=True) 
    
    if comp == 'League':
        strs = df.iloc[:, 1:6]
        ints = df.iloc[:, np.r_[10:15, 17:20, 21:29, 30:32]].astype(float)     
        data = pd.concat([strs, ints], axis=1)                            
        data = data.rename(columns = {'Def 3rd':'Tkl_D3', 'Mid 3rd':'Tkl_M3', 'Att 3rd':'Tkl_A3',
                                      'Tkl.1':'Tkl_VD', 'Succ':'Press_Succ', 'Def 3rd.1':'Pr_D3',
                                      'Mid 3rd.1':'Pr_M3', 'Att 3rd.1':'Pr_A3', 'Sh':'Blk_Sh',
                                      'Pass':'Blk_Pass'})
    elif comp == 'Club Cup':
        df = df.replace('', '0', regex=True)
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[9:14, 16:19, 20:28, 29:31]].replace('', np.NaN).astype(float)     
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Nation', 'Pos', 'Squad', 'TklW', 'Tkl_D3', 'Tkl_M3',
                        'Tkl_A3', 'Tkl_VD', 'Past', 'Press', 'Press_Succ', 'Pr_D3', 'Pr_M3',
                        'Pr_A3', 'Blocks', 'Blk_Sh', 'ShSv', 'Blk_Pass', 'Int', 'Clr', 'Err']
    elif comp == 'Int':
        df = df.replace('', '0') 
        strs = df.iloc[:, 1:4]  
        ints = df.iloc[:, np.r_[8:13, 15:18, 19:27, 28:30]].replace('', np.NaN).astype(float)
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Pos', 'Squad', 'TklW', 'Tkl_D3', 'Tkl_M3',
                        'Tkl_A3', 'Tkl_VD', 'Past', 'Press', 'Press_Succ', 'Pr_D3', 'Pr_M3',
                        'Pr_A3', 'Blocks', 'Blk_Sh', 'ShSv', 'Blk_Pass', 'Int', 'Clr', 'Err']
        
    return data


def clean_all(d1, d2, d3, d4, d5, d6, comp):
    '''
    This functions takes in 6 DFs and cleans them based on what type of competition data is from
    
    Parameters
    ----------
    d1 : DataFrame
        Standard Stats dataframe       
    d2 : DataFrame
        Shooting Stats dataframe        
    d3 : DataFrame
        Passing Stats dataframe        
    d4 : DataFrame
        Possession Stats dataframe        
    d5 : DataFrame
        Standard Stats dataframe       
    d6 : DataFrame
        Defense Stats dataframe   
    comp : str
        What type of competiton data is from, options are: 'League', 'Club Cup' or 'Int' 

    Returns
    -------
    st : DataFrame
        Cleaned Standard Stats dataframe       
    sh : DataFrame
        Cleaned Shooting Stats dataframe      
    pa : DataFrame
        Cleaned Passing Stats dataframe     
    mi : DataFrame
        Cleaned Possession Stats dataframe   
    po : DataFrame
        Cleaned Standard Stats dataframe 
    de : DataFrame
        Cleaned Defense Stats dataframe  
    '''
    st = clean_std(d1, comp)
    sh = clean_shoot(d2, comp)
    pa = clean_pass(d3, comp)
    mi = clean_misc(d4, comp)
    po = clean_pos(d5, comp)
    de = clean_def(d6, comp)
    
    return st, sh, pa, mi, po, de


def merge(df1, df2):
    '''
    This function merges two dataframes on matching columns
    
    Parameters
    ----------
    df1 : dataframe
        The first dataframe to be merged
    df2 : dataframe
        The second dataframe to be merged
    
    Returns
    -------
    data : dataframe
        df1 and df2 merged together    
    '''
    lst1 = list(df1.columns)
    lst2 = list(df2.columns)
    lst1_set = set(lst1)
    same = list(lst1_set.intersection(lst2))
    
    data = pd.merge(left = df1, right = df2, how = 'inner', left_on = same, right_on = same)
    
    return data


def merge_all(d1, d2, d3, d4, d5, d6):
    '''
    This function takes 6 dataframes and merges them together into 1 based on common columns

    Parameters
    ----------
    d1 : DataFrame
        A dataframe, can be any of the 6, order doesnt matter
    d2 : DataFrame
        A dataframe, can be any of the 6, order doesnt matter
    d3 : DataFrame
        A dataframe, can be any of the 6, order doesnt matter
    d4 : DataFrame
        A dataframe, can be any of the 6, order doesnt matter
    d5 : DataFrame
        A dataframe, can be any of the 6, order doesnt matter
    d6 : DataFrame
        A dataframe, can be any of the 6, order doesnt matter

    Returns
    -------
    data : DataFrame
        all 6 inputs merged together into 1 dataframe

    '''
    data = merge(d1, d2)
    data = merge(data, d3)
    data = merge(data, d4)
    data = merge(data, d5)
    data = merge(data, d6)
    
    return data


def edit_pos(data):
    '''
    This function edits the 'Position' variables in the dataframe 'data':
        Drops Goalies 'GK' from the data
        Remaps the 'Position' varible in 'FW', 'MF' and 'DF'

    Parameters
    ----------
    data : DataFrame
        Merged data from a given season/tournament

    Returns
    -------
    df : DataFrame
        'data' with 'Pos' column edited
    '''
    data = data[(data['Pos'] != 'GK') & (data['Pos'] != 'GKMF')]  #removiing goales from data 
    
    positions = ['FWMF', 'FWDF', 'MFFW', 'MFDF', 'DFMF', 'DFFW']
    new = ['FW', 'FW', 'MF', 'MF', 'DF', 'DF']
    df = data.replace(positions, new)   #changing position values 
    
    return df
'''This function checks to see if there are duplicate rows for the same player(s)'''



def dup_players(data):
    '''
    This function checks a dataframe for a given season/tournament for duplciate players and fixes them
    by aggregating the data based on certain conditions

    Parameters
    ----------
    data : DataFrame
        Merged data from a given season/tournament

    Returns
    -------
    df : DataFrame
        'data' with duplicated players fixed

    '''
    if len(data) > len(data.Player.value_counts()):  #Checking to see if some players are in the data more than once
        print("There are currently", len(data), "rows in the data.")
        print("There are", len(data.Player.value_counts()), "unique player names.\n")
            
        cols = data.columns.to_list() #List of all columns
        keep = ['Player', 'Age', 'Born']  #These variables will be used to aggregate rows

        agg_cols = [x for x in cols if x not in keep] #columns on which aggregation will occur
        agg_func = dict()
        first = ['Nation', 'Pos', 'Squad', 'Comp']
        for i in agg_cols:
            if i in first:
                agg_func[i] = 'first'
            else:
                agg_func[i] =  'sum'

        df = data.groupby(keep).aggregate(agg_func).reset_index()
        print((len(data) - len(df)), "rows were removed\n")
        
        vc = df.Player.value_counts()
        vc = vc[vc > 1]
        if len(vc) > 1:
            print("These rows are for players who have the same name: ")
            for i, v in vc.iteritems():
                print(i, v) 
    else:
        print('No Duplicate Players in the data')
        df = data
    
    return df



def get_headers(url):
    '''
    Returns a list of tuples of column names and an empty list for values from the given url

    Parameters
    ----------
    url : string
        URL to a fifaindex page containing player ratings

    Returns
    -------
    cols : list
        list of tuples of column name and empty list to be filled with data
    '''
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.find('table')
    table_data = table.find_all('tr')[3:] #first three rows are empty, so skip them
    
    cols=[] #empty list     
    for td in table_data[0].find_all('td')[1:]: #first column is just picture of player, can skip
        cols.append((td['data-title'], [])) #creating tuples for each column, with lists for values for each
        
    return cols
    


def scrape_fut(url, last, cols, j=2):
    '''
    Puts data from page 'url' into 'cols' and continues recursively until the 'last' url, using j as page index

    Parameters
    ----------
    url : string
        The first page to get data from
    last : string
        The last page to get data from
    cols : list
        list of tuples created with 'get_headers' function
    j : int, optional
        Used for increasing url page number for recursiveness. The default is 2.

    Returns
    -------
    cols : list
        list of tuples with coumn names and lists of data
    '''
    print('Getting data from {}'.format(url))
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.find('table')
    table_data = table.find_all('tr')
    
    i=0
    
    for row in table_data:
        tds = row.find_all('td')[1:]
    
        if len(tds) == 0: #random empty rows in table, just skip them
            pass
        else:
            i=0
            if tds[-1].has_attr('data-title'): #deals with issue with no 'Team' 
                for td in tds:
                    if td['data-title'] == 'Nationality' or td['data-title'] == 'Team': #these are images, we want title
                        cols[i][1].append(td.find('a').get('title')) #title
                        i += 1
                    else:
                        cols[i][1].append(td.text)
                        i += 1
            else:
                pass #skip the player with no team available
              
    if url != last: #want to keep going until 'last' page is scraped
        url2 = url.split('=')[0] + '={}'.format(j) #increasing page number by 1
        j += 1
        scrape_fut(url2, last, cols, j)
                  
    return cols



def clean_fut(lst):
    '''
    Takes a list of tuples and returns a dataframe. Also edits 'Team' column and splits the 'OVR / POT' column

    Parameters
    ----------
    lst : list
        list of tuples created by 'scrape_fut' and 'get_header' functions

    Returns
    -------
    df : DataFrame
        A DataFrame containing FIFA player ratings for a given FIFA game
    '''
    Dict = {title:column for (title,column) in lst}
    df = pd.DataFrame(Dict)
    
    df[['Team', 'Year']] = df['Team'].str.split(' FIFA ', expand=True) 
    df['Overall'] = df['OVR / POT'].str[:2] #first 2 characters of string are overall
    df['Potential'] = df['OVR / POT'].str[2:] #second 2 characters are potential
    
    df = df.drop('OVR / POT', axis=1) #can remove now that two new columns are created
    
    df = df[['Name', 'Age', 'Nationality', 'Team', 'Preferred Positions', 'Overall', 'Potential', 'Year']] #reorder columns
    df[['Age', 'Overall', 'Potential']] = df[['Age', 'Overall', 'Potential']].astype(int) #change column types
    
    return df



def get_fut(url, last, j=2):
    '''
    Scrapes data from first 'url' to 'last' url and returns a DataFrame

    Parameters
    ----------
    url : string
        First page of data to be scraped
    last : TYPE
        Last page of data to be scraped
    j : int, optional
        Used for increasing page number of 'url'. The default is 2.

    Returns
    -------
    df : DataFrame
        A DataFrame containing FIFA player ratings for a given FIFA game
    '''
    cols = get_headers(url)
    dlst = scrape_fut(url, last, cols, j)
    df   = clean_fut(dlst)
    
    return df



def add_dfs(df1, df2, df2_type):
    '''
    This function concatenates two dataframes (df1 and df2), using df2_type to determine which columns
    to merge on 

    Parameters
    ----------
    df1 : DataFrame
        A DataFrame containing soccer stats 
    df2 : TYPE
        A DataFrame containing soccer stats
    df2_type : string
        What type of competition df2 is (Club tournament or Country tournament)

    Returns
    -------
    data : DataFrame
        df1 and df2 merged together

    '''
    cols = df1[['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born']] 
                                                                                   
    df1 = df1.drop(['Nation', 'Pos', 'Squad', 'Comp', 'Age'], axis=1)                 
    
    if df2_type == 'Club':
        df2 = df2.drop(['Age', 'Nation', 'Pos', 'Squad'], axis=1)
    elif df2_type == 'Country':
        df2 = df2.drop(['Age', 'Pos', 'Nation'], axis=1)
        
    df = df1.set_index(['Player', 'Born']).add(df2.set_index(['Player', 'Born']), fill_value=0).reset_index()
    
    print('There are {} players out of {} possible present in both datsets'.format(len(df2) - (len(df) - len(df1)), len(df2)))

    data = cols.merge(df, on=['Player', 'Born'])
    
    return data

        

def add_all(df_list, type_list):
    '''
    This function adds multiple DataFrames together (from df_list) using the corresponding string per df
    from type_list to determine which columns to merge on 

    Parameters
    ----------
    df_list : list
        List of DataFrames to be merged
    type_list : TYPE
        List of competition types, first df in df_list does not need type 

    Returns
    -------
    data : TYPE
        DESCRIPTION.

    '''
    length = len(df_list)
    
    data = df_list[0]
    
    for i in range(length-1):
        data = add_dfs(data, df_list[i+1], type_list[i])
        
    return data
