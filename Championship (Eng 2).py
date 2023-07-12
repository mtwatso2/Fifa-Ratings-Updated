# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:16:38 2023

@author: MWatson717
"""

import fifa_funcs_2623 as f

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4') #to ignore warning about using a list of links


##### Championship (England 2nd Division) 2018-2019 #####
url1 = 'https://fbref.com/en/comps/10/2018-2019/2018-2019-Championship-Stats'

links = f.get_all_links(url1, other=True)
    
st, sh, ps, ms, pos, df = f.get_data(links[0], league = False) #need league = False here to get the player data instead of team 

st, sh, ps, ms, pos, df = f.clean_all(st, sh, ps, ms, pos, df, comp = 'Club Cup') #because there is no 'league' variable like BIG 5 has

champ18_19 = f.merge_all(st, sh, ps, ms, pos, df)

champ18_19 = f.edit_pos(champ18_19)

champ18_19['Nation'] = champ18_19['Nation'].str.split().str[1] #removing 2 letter abreviation

champ18_19 = f.dup_players(champ18_19)

champ18_19.isna().sum().sum() #1 missing

missing = champ18_19.loc[champ18_19.isnull().sum(1) > 0]

print(missing) #Mohamed Eisa of club Briston City is from Sudan 

champ18_19.at[471, 'Nation'] = 'SDN'

champ18_19.isna().sum().sum() #no more missing values

champ18_19.insert(6, 'Comp', 'Championship')

champ18_19.to_csv('champ18_19.csv', index=False)


##### Championship (England 2nd Division) 2019-2020 #####
st2, sh2, ps2, ms2, pos2, df2 = f.get_data(links[1], league = False) #need league = False here to get the player data instead of team 

st2, sh2, ps2, ms2, pos2, df2 = f.clean_all(st2, sh2, ps2, ms2, pos2, df2, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

champ19_20 = f.merge_all(st2, sh2, ps2, ms2, pos2, df2)

champ19_20 = f.edit_pos(champ19_20)

champ19_20['Nation'] = champ19_20['Nation'].str.split().str[1] #removing 2 letter abreviation

champ19_20 = f.dup_players(champ19_20)

champ19_20.isna().sum().sum() #1 missing

missing2 = champ19_20.loc[champ19_20.isnull().sum(1) > 0]

print(missing2)

champ19_20.at[21, 'Nation'] = 'NED' #Alessio da Cruz of club Sheffield Weds is from the Netherlands 

champ19_20.isna().sum().sum() #no more missing values

champ19_20.insert(6, 'Comp', 'Championship')

champ19_20.to_csv('champ19_20.csv', index=False)


##### Championship (England 2nd Division) 2020-2021 #####
st3, sh3, ps3, ms3, pos3, df3 = f.get_data(links[2], league = False) #need league = False here to get the player data instead of team 

st3, sh3, ps3, ms3, pos3, df3 = f.clean_all(st3, sh3, ps3, ms3, pos3, df3, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

champ20_21 = f.merge_all(st3, sh3, ps3, ms3, pos3, df3)

champ20_21 = f.edit_pos(champ20_21)

champ20_21['Nation'] = champ20_21['Nation'].str.split().str[1] #removing 2 letter abreviation

champ20_21 = f.dup_players(champ20_21)

champ20_21.isna().sum().sum() #0 missing

champ20_21.insert(6, 'Comp', 'Championship')

champ20_21.to_csv('champ20_21.csv', index=False)


##### Championship (England 2nd Division) 2021-2022 #####
st4, sh4, ps4, ms4, pos4, df4 = f.get_data(links[3], league = False) #need league = False here to get the player data instead of team 

st4, sh4, ps4, ms4, pos4, df4 = f.clean_all(st4, sh4, ps4, ms4, pos4, df4, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

champ21_22 = f.merge_all(st4, sh4, ps4, ms4, pos4, df4)

champ21_22 = f.edit_pos(champ21_22)

champ21_22['Nation'] = champ21_22['Nation'].str.split().str[1] #removing 2 letter abreviation

champ21_22 = f.dup_players(champ21_22)

champ21_22.isna().sum().sum() #3 missing

missing3 = champ21_22.loc[champ21_22.isnull().sum(1) > 0]

print(missing3)

champ21_22.at[417, 'Nation'] = 'WAL' #Luke Mariette of club Blackpool is from Wales 

champ21_22.at[510, 'Nation'] = 'POR' #Quevin Castro of club West Brom is from Portugal 

champ21_22.at[650, 'Nation'] = 'ENG' #Zak Lovelace of club Millwall is from England

champ21_22.isna().sum().sum() # 0 missing now 

champ21_22.insert(6, 'Comp', 'Championship')

champ21_22.to_csv('champ21_22.csv', index=False)


##### Championship (England 2nd Division) 2022-2023 #####
st5, sh5, ps5, ms5, pos5, df5 = f.get_data(links[4], league = False) #need league = False here to get the player data instead of team 

st5, sh5, ps5, ms5, pos5, df5 = f.clean_all(st5, sh5, ps5, ms5, pos5, df5, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

champ22_23 = f.merge_all(st5, sh5, ps5, ms5, pos5, df5)

champ22_23 = f.edit_pos(champ22_23)

champ22_23['Nation'] = champ22_23['Nation'].str.split().str[1] #removing 2 letter abreviation

champ22_23 = f.dup_players(champ22_23)

champ22_23.isna().sum().sum() # 4 missing values 

missing4 = champ22_23.loc[champ22_23.isnull().sum(1) > 0]

print(missing4)

champ22_23.at[242, 'Nation'] = 'ENG' #Harry Wood of club Hull City is from England

champ22_23.at[322, 'Nation'] = 'ENG' #Joel Holvey of club Rotherham Utd is from England

champ22_23.at[483, 'Nation'] = 'ENG' #Nathan Lowe of club Stoke City is from England

champ22_23.at[557, 'Nation'] = 'ENG' #Sai Sachdev of club Sheffield Utd is from England

champ22_23.isna().sum().sum() #0 missing values 

champ22_23.insert(6, 'Comp', 'Championship')

champ22_23.to_csv('champ22_23.csv', index=False)

