# -*- coding: utf-8 -*-
"""
@author: MWatson717
"""

#This file contains functions used for the project

import requests
import lxml.html as lh
import pandas as pd
import numpy as np


def get_all_links(url, league=True):
    '''
    This funciton takes a URL and returns a list of URLs as well as a URL to next years homepage
    
    Parameters
    ----------
    url : str
        a URL to the homepage of a Football Reference season/tournament
    league: bool
        Default True, used to select correct URLs for given years data
        
    Returns
    -------
    ls2 : list
        list of URLs of desired data tables 
    nex : str
        link to next seasons/tournaments home page
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
        
    return ls2, nex


def scraper(url):
    '''
    This function takes a URL and returns a datafrme from it
    
    Parameters
    ----------
    url : str
        URL to a specific Football Reference data table  

    Returns
    -------
    df : DataFrame
        A DataFrame of the data from url
    '''
    lst = pd.read_html(url, header=1)
    df = lst[0]
    
    return df


def get_data(lst):
    '''    
    This function takes a list of URLs and returns a dataframe for each URL
    
    Parameters
    ----------
    lst : list
        list of URLs created from 'get_all_links' function

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
    standard = scraper(lst[5])
    shooting = scraper(lst[4])
    passing = scraper(lst[2])
    misc = scraper(lst[1])
    pos = scraper(lst[3])
    defense = scraper(lst[0])
    
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
        strs = df.iloc[:, 1:5]                                      
        ints = df.iloc[:, np.r_[5:10, 11:13, 14:18]].astype(float)
    elif comp == 'Int':
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
        strs = df.iloc[:, 1:5]       
        ints = df.iloc[:, [5, 9, 10, 16, 17]].replace('', np.NaN).astype(float)
    elif comp == 'Int':
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
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[11:15, 16:18, 19:21, 25:29]].replace('', np.NaN).astype(float)
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Nation', 'Pos', 'Squad', 'Pas_TotDist', 'Pas_PrgDist', 'Cmp_S', 'Att_S', 
                        'Cmp_M', 'Att_M', 'Cmp_L', 'Att_L', 'KP', 'Pas_A3','PPA', 'CrsPA']
    elif comp == 'Int':
        strs = df.iloc[:, 1:4]
        ints = df.iloc[:, np.r_[10:14, 15:17, 18:20, 24:28]]
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
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[10:15, 17:23]].replace('', np.NaN).astype(float)
    elif comp == 'Int':
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
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[8:17, 18:30, 31]].replace('', np.NaN).astype(float)
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Nation', 'Pos', 'Squad','Touches', 'Tch_DP', 'Tch_D3', 'Tch_M3','Tch_A3', 
                        'Tch_AP', 'Live', 'Dr_Succ', 'Dr_Att', 'Num_Dr_Past', 'Megs','Carries', 'Cr_TotDist', 
                        'Cr_PrgDist', 'Cr_Prog', 'Cr_A3', 'CPA', 'Mis', 'Dis', 'Targ', 'Rec', 'Prog_Pas_Rec']
    elif comp == 'Int':
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
        strs = df.iloc[:, 1:5]
        ints = df.iloc[:, np.r_[9:14, 16:19, 20:28, 29:31]].replace('', np.NaN).astype(float)     
        data = pd.concat([strs, ints], axis=1)
        data.columns = ['Player', 'Nation', 'Pos', 'Squad', 'TklW', 'Tkl_D3', 'Tkl_M3',
                        'Tkl_A3', 'Tkl_VD', 'Past', 'Press', 'Press_Succ', 'Pr_D3', 'Pr_M3',
                        'Pr_A3', 'Blocks', 'Blk_Sh', 'ShSv', 'Blk_Pass', 'Int', 'Clr', 'Err']
    elif comp == 'Int':
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
    
    return df
