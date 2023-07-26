# -*- coding: utf-8 -*-
"""
@author: MWatson717
"""

#Merging all data together
import fifa_funcs_2623 as f
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

data_1718 = f.add_all(d17, t17)     #2364 rows

fifa19 = pd.read_csv('fifa19.csv')

fifa19['Nationality'].replace(code_mapper, inplace=True)

fifa19 = fifa19[['Name', 'Nationality', 'Overall', 'Year']]

f19 = pd.merge(fifa19, cc, how='left', left_on='Nationality', right_on='Country')

f19 = f19[['Name', 'Overall', 'Year', 'Code']]

fut19 = pd.merge(data_1718, f19, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut19.drop(['Name', 'Code'], axis=1, inplace=True) #started with 2364, reduced to 1879


### FIFA 20 ###
d18_19 = pd.read_csv('data18_19.csv')            # Big 5 Leagues (England, Spain, Italy, Germany, France)
n18_19 = pd.read_csv('eridivisie18_19.csv')      # Netherlands Eridivisie
p18_19 = pd.read_csv('primeira18_19.csv')        # Portugal Primeira Liga
c18_19 = pd.read_csv('champ18_19.csv')           # England Championship (2nd division)

all18_19 = pd.concat([d18_19, n18_19, p18_19, c18_19])  #3910 rows

u18_19 = pd.read_csv('ucl18_19.csv')             # UEFA Champions League
e18_19 = pd.read_csv('europa18_19.csv')          # UEFA Europa League 

d18 = [all18_19, u18_19, e18_19]
t18 = ['Club', 'Club']

data_1819 = f.add_all(d18, t18)     #4428 rows 

fifa20 = pd.read_csv('fifa20.csv')

fifa20['Nationality'].replace(code_mapper, inplace=True)

fifa20 = fifa20[['Name', 'Nationality', 'Overall', 'Year']]

f20 = pd.merge(fifa20, cc, how='left', left_on='Nationality', right_on='Country')

f20 = f20[['Name', 'Overall', 'Year', 'Code']]

fut20 = pd.merge(data_1819, f20, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut20.drop(['Name', 'Code'], axis=1, inplace=True)  #2884 rows


### FIFA 21 ###
d19_20 = pd.read_csv('data19_20.csv')            # Big 5 Leagues (England, Spain, Italy, Germany, France)
n19_20 = pd.read_csv('eridivisie19_20.csv')      # Netherlands Eridivisie
p19_20 = pd.read_csv('primeira19_20.csv')        # Portugal Primeira Liga
c19_20 = pd.read_csv('champ19_20.csv')           # England Championship (2nd division)

all19_20 = pd.concat([d19_20, n19_20, p19_20, c19_20])  #4006 rows

u19_20 = pd.read_csv('ucl19_20.csv')             # UEFA Champions League
e19_20 = pd.read_csv('europa19_20.csv')          # UEFA Europa League 

d19 = [all19_20, u19_20, e19_20]
t19 = ['Club', 'Club']

data_1920 = f.add_all(d19, t19)     #2411 rows

fifa21 = pd.read_csv('fifa21.csv')

fifa21['Nationality'].replace(code_mapper, inplace=True)

fifa21 = fifa21[['Name', 'Nationality', 'Overall', 'Year']]

f21 = pd.merge(fifa21, cc, how='left', left_on='Nationality', right_on='Country')

f21 = f21[['Name', 'Overall', 'Year', 'Code']]

fut21 = pd.merge(data_1920, f21, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut21.drop(['Name', 'Code'], axis=1, inplace=True)  #2962 rows


### FIFA 22 ###
d20_21 = pd.read_csv('data20_21.csv')            # Big 5 Leagues (England, Spain, Italy, Germany, France)
n20_21 = pd.read_csv('eridivisie20_21.csv')      # Netherlands Eridivisie
p20_21 = pd.read_csv('primeira20_21.csv')        # Portugal Primeira Liga
c20_21 = pd.read_csv('champ20_21.csv')           # England Championship (2nd division)

all20_21 = pd.concat([d20_21, n20_21, p20_21, c20_21])  #4112 rows

u20_21 = pd.read_csv('ucl20_21.csv')             # UEFA Champions League
e20_21 = pd.read_csv('europa20_21.csv')          # UEFA Europa League 

d20 = [all20_21, u20_21, e20_21]
t20 = ['Club', 'Club']

data_2021 = f.add_all(d20, t20)     #4822 rows

fifa22 = pd.read_csv('fifa22.csv')

fifa22['Nationality'].replace(code_mapper, inplace=True)

fifa22 = fifa22[['Name', 'Nationality', 'Overall', 'Year']]

f22 = pd.merge(fifa22, cc, how='left', left_on='Nationality', right_on='Country')

f22 = f22[['Name', 'Overall', 'Year', 'Code']]

fut22 = pd.merge(data_2021, f22, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut22.drop(['Name', 'Code'], axis=1, inplace=True)  #2811 rows


### FIFA 23 ###
d21_22 = pd.read_csv('data21_22.csv')            # Big 5 Leagues (England, Spain, Italy, Germany, France)
n21_22 = pd.read_csv('eridivisie21_22.csv')      # Netherlands Eridivisie
p21_22 = pd.read_csv('primeira21_22.csv')        # Portugal Primeira Liga
c21_22 = pd.read_csv('champ21_22.csv')           # England Championship (2nd division)

all21_22 = pd.concat([d21_22, n21_22, p21_22, c21_22])  #4235 rows

u21_22 = pd.read_csv('ucl21_22.csv')             # UEFA Champions League
e21_22 = pd.read_csv('europa21_22.csv')          # UEFA Europa League 

d21 = [all21_22, u21_22, e21_22]
t21 = ['Club', 'Club']

data_2122 = f.add_all(d21, t21)     #5131 rows

fifa23 = pd.read_csv('fifa23.csv')

fifa23['Nationality'].replace(code_mapper, inplace=True)

fifa23 = fifa23[['Name', 'Nationality', 'Overall', 'Year']]

f23 = pd.merge(fifa23, cc, how='left', left_on='Nationality', right_on='Country')

f23 = f23[['Name', 'Overall', 'Year', 'Code']]

fut23 = pd.merge(data_2122, f23, how='left', left_on=['Player', 'Nation'], 
                 right_on=['Name', 'Code']).dropna().drop_duplicates(subset=['Player']).reset_index(drop=True)

fut23.drop(['Name', 'Code'], axis=1, inplace=True)  #2967 rows


## Adding it all together ##
data = pd.concat([fut19, fut20, fut21, fut22, fut23], ignore_index=True)

data['Game'] = data['Year'].astype(int).astype('category')

data.drop('Year', axis=1, inplace=True)

data.to_csv('FUT_data_726.csv', index=False)


pd.pivot_table(data, values='Player', index='Comp', columns='Game', aggfunc='count', margins=True)


### FIFA 24 ###
d22_23 = pd.read_csv('data22_23.csv')            # Big 5 Leagues (England, Spain, Italy, Germany, France)
n22_23 = pd.read_csv('eridivisie22_23.csv')      # Netherlands Eridivisie
p22_23 = pd.read_csv('primeira22_23.csv')        # Portugal Primeira Liga
c22_23 = pd.read_csv('champ22_23.csv')           # England Championship (2nd division)

all22_23 = pd.concat([d22_23, n22_23, p22_23, c22_23])  #4196 rows 

u22_23 = pd.read_csv('ucl22_23.csv')             # UEFA Champions League
e22_23 = pd.read_csv('europa22_23.csv')          # UEFA Europa League 

d22 = [all22_23, u22_23, e22_23]
t22 = ['Club', 'Club']

data_2223 = f.add_all(d22, t22)     #5050 rows 

#FIFA is rebranding as EA FC starting for the 2023-2024 season, might not be able to scrape data from the same source


