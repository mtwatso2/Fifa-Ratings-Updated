# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:51:04 2022

@author: MWatson717
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

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

########## FIFA 2019 Data ##########

url  = 'https://www.fifaindex.com/players/fifa19_282/?page=1'       #September 27 2018
last = 'https://www.fifaindex.com/players/fifa19_282/?page=604'

df19 = get_fut(url, last)

df19.to_csv('fifa19.csv', index=False)



########## FIFA 2020 Data ##########

url_20  = 'https://www.fifaindex.com/players/fifa20_358/?page=1'    #September 26 2019
last_20 = 'https://www.fifaindex.com/players/fifa20_358/?page=620'

df20 = get_fut(url_20, last_20) 

df20.to_csv('fifa20.csv', index=False)



########## FIFA 2021 Data ##########

url_21 = 'https://www.fifaindex.com/players/fifa21_423/?page=1'     #October 5 2020 

last_21 = 'https://www.fifaindex.com/players/fifa21_423/?page=633'

df21 = get_fut(url_21, last_21)

df21.to_csv('fifa21.csv', index=False)



########## FIFA 2022 Data ##########

url_22 = 'https://www.fifaindex.com/players/fifa22_490/?page=1'     #September 27 2021

last_22 = 'https://www.fifaindex.com/players/fifa22_490/?page=618'

df22 = get_fut(url_22, last_22)

df22.to_csv('fifa22.csv', index=False)

