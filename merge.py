# -*- coding: utf-8 -*-
"""
@author: MWatson717
"""

#Merging all data together
import fifa_funcs as f
import pandas as pd

### Need to get country codes since FBREF data uses these while FUT data has country name

url = 'https://en.wikipedia.org/wiki/List_of_FIFA_country_codes'

codes = pd.read_html(url)

cc = codes[0].append(codes[1:4], ignore_index=True)

code_mapper = {'Korea Republic' : 'South Korea', 'Bosnia & Herzegovina' : 'Bosnia and Herzegovina',
               'Guinea Bissau' : 'Guinea-Bissau', 'Curacao' : 'Curaçao', 'Korea DPR' : 'North Korea',
               'Antigua & Barbuda' : 'Antigua and Barbuda', 'St Kitts Nevis' : 'Saint Kitts and Nevis',
               'Central African Rep.' : 'Central African Republic', 'Trinidad & Tobago' : 'Trinidad and Tobago',
               'São Tomé & Príncipe' : 'São Tomé and Príncipe', 'St Lucia' : 'Saint Lucia'}


### FIFA 19 ###
d17_18 = pd.read_csv('data17_18.csv')

wc = pd.read_csv('world_cup_2018.csv')

d17 = [d17_18, wc]
t17 = ['Country']

data_1718 = f.add_all(d17, t17)

fifa19 = pd.read_csv('fifa19.csv')

fifa19['Nationality'].replace(code_mapper, inplace=True)

fifa19 = fifa19[['Name', 'Nationality', 'Overall', 'Year']]

f19 = pd.merge(fifa19, cc, how='left', left_on='Nationality', right_on='Country')

f19 = f19[['Name', 'Overall', 'Year', 'Code']]

fut19 = pd.merge(data_1718, f19, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut19.drop(['Name', 'Code'], axis=1, inplace=True)


### FIFA 20 ###
d18_19 = pd.read_csv('data18_19.csv')
c18_19 = pd.read_csv('champ18_19.csv')
e18_19 = pd.read_csv('europa18_19.csv')

d18 = [d18_19, c18_19, e18_19]
t18 = ['Club', 'Club']

data_1819 = f.add_all(d18, t18)

fifa20 = pd.read_csv('fifa20.csv')

fifa20['Nationality'].replace(code_mapper, inplace=True)

fifa20 = fifa20[['Name', 'Nationality', 'Overall', 'Year']]

f20 = pd.merge(fifa20, cc, how='left', left_on='Nationality', right_on='Country')

f20 = f20[['Name', 'Overall', 'Year', 'Code']]

fut20 = pd.merge(data_1819, f20, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut20.drop(['Name', 'Code'], axis=1, inplace=True)


### FIFA 21 ###
d19_20 = pd.read_csv('data19_20.csv')
c19_20 = pd.read_csv('champ19_20.csv')
e19_20 = pd.read_csv('europa19_20.csv')

d19 = [d19_20, c19_20, e19_20]
t19 = ['Club', 'Club']

data_1920 = f.add_all(d19, t19)

fifa21 = pd.read_csv('fifa21.csv')

fifa21['Nationality'].replace(code_mapper, inplace=True)

fifa21 = fifa21[['Name', 'Nationality', 'Overall', 'Year']]

f21 = pd.merge(fifa21, cc, how='left', left_on='Nationality', right_on='Country')

f21 = f21[['Name', 'Overall', 'Year', 'Code']]

fut21 = pd.merge(data_1920, f21, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut21.drop(['Name', 'Code'], axis=1, inplace=True)


### FIFA 22 ###
d20_21 = pd.read_csv('data20_21.csv')
c20_21 = pd.read_csv('champ20_21.csv')
e20_21 = pd.read_csv('europa20_21.csv')
euro_2021 = pd.read_csv('euro_cup_2021.csv')
copa_2021 = pd.read_csv('copa_america_2021.csv')

d20 = [d20_21, c20_21, e20_21, euro_2021, copa_2021]
t20 = ['Club', 'Club', 'Country', 'Country']

data_2021 = f.add_all(d20, t20)

fifa22 = pd.read_csv('fifa22.csv')

fifa22['Nationality'].replace(code_mapper, inplace=True)

fifa22 = fifa22[['Name', 'Nationality', 'Overall', 'Year']]

f22 = pd.merge(fifa22, cc, how='left', left_on='Nationality', right_on='Country')

f22 = f22[['Name', 'Overall', 'Year', 'Code']]

fut22 = pd.merge(data_2021, f22, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut22.drop(['Name', 'Code'], axis=1, inplace=True)

data = pd.concat([fut19, fut20, fut21, fut22], ignore_index=True)

data['Game'] = data['Year'].astype(int).astype('category')

data.drop('Year', axis=1, inplace=True)

#data.to_csv('fut_data.csv', index=False)
