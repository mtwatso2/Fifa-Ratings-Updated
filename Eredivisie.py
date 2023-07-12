# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:31:08 2023

@author: MWatson717
"""

import fifa_funcs_2623 as f

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4') #to ignore warning about using a list of links


##### Eredivisie 2018-2019 #####
url = 'https://fbref.com/en/comps/23/2018-2019/2018-2019-Eredivisie-Stats'

links = f.get_all_links(url, other=True)
    
st, sh, ps, ms, pos, df = f.get_data(links[0], league = False) #need league = False here to get the player data instead of team 

st, sh, ps, ms, pos, df = f.clean_all(st, sh, ps, ms, pos, df, comp = 'Club Cup') #because there is no 'league' variable like BIG 5 has

data18_19 = f.merge_all(st, sh, ps, ms, pos, df)

data18_19 = f.edit_pos(data18_19)

data18_19['Nation'] = data18_19['Nation'].str.split().str[1] #removing 2 letter abreviation

data18_19 = f.dup_players(data18_19)

data18_19.isna().sum().sum() #0 missing

data18_19.insert(6, 'Comp', 'Eredivisie')

data18_19.to_csv('eridivisie18_19.csv', index=False)


##### Eredivisie 2019-2020 #####
st2, sh2, ps2, ms2, pos2, df2 = f.get_data(links[1], league = False) #need league = False here to get the player data instead of team 

st2, sh2, ps2, ms2, pos2, df2 = f.clean_all(st2, sh2, ps2, ms2, pos2, df2, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

data19_20 = f.merge_all(st2, sh2, ps2, ms2, pos2, df2)

data19_20 = f.edit_pos(data19_20)

data19_20['Nation'] = data19_20['Nation'].str.split().str[1] #removing 2 letter abreviation

data19_20 = f.dup_players(data19_20)

data19_20.isna().sum().sum() #0 missing

data19_20.insert(6, 'Comp', 'Eredivisie')

data19_20.to_csv('eridivisie19_20.csv', index=False)


##### Eredivisie 2020-2021 #####
st3, sh3, ps3, ms3, pos3, df3 = f.get_data(links[2], league = False) #need league = False here to get the player data instead of team 

st3, sh3, ps3, ms3, pos3, df3 = f.clean_all(st3, sh3, ps3, ms3, pos3, df3, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

data20_21 = f.merge_all(st3, sh3, ps3, ms3, pos3, df3)

data20_21 = f.edit_pos(data20_21)

data20_21['Nation'] = data20_21['Nation'].str.split().str[1] #removing 2 letter abreviation

data20_21 = f.dup_players(data20_21)

data20_21.isna().sum().sum() #2 missing

missing = data20_21.loc[data20_21.isnull().sum(1) > 0]

print(missing) 

data20_21.at[15, 'Nation'] = 'NED' #Alessio da Cruz of club Groningen is from the Netherlands

data20_21.at[439, 'Nation'] = 'CZE' #Tomas Hajek of club Vitesse is from Czechia

data20_21.isna().sum().sum() #0 missing now 

data20_21.insert(6, 'Comp', 'Eredivisie')

data20_21.to_csv('eridivisie20_21.csv', index=False)


##### Eredivisie 2021-2022 #####
st4, sh4, ps4, ms4, pos4, df4 = f.get_data(links[3], league = False) #need league = False here to get the player data instead of team 

st4, sh4, ps4, ms4, pos4, df4 = f.clean_all(st4, sh4, ps4, ms4, pos4, df4, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

data21_22 = f.merge_all(st4, sh4, ps4, ms4, pos4, df4)

data21_22 = f.edit_pos(data21_22)

data21_22['Nation'] = data21_22['Nation'].str.split().str[1] #removing 2 letter abreviation

data21_22 = f.dup_players(data21_22)

data21_22.isna().sum().sum() #1 missing

missing2 = data21_22.loc[data21_22.isnull().sum(1) > 0]

print(missing2)

data21_22.at[446, 'Nation'] = 'CZE' #Tomas Hajek of club Vitesse is from Czechia

data21_22.isna().sum().sum() # 0 missing now 

data21_22.insert(6, 'Comp', 'Eredivisie')

data21_22.to_csv('eridivisie21_22.csv', index=False)


##### Eredivisie 2022-2023 #####
st5, sh5, ps5, ms5, pos5, df5 = f.get_data(links[4], league = False) #need league = False here to get the player data instead of team 

st5, sh5, ps5, ms5, pos5, df5 = f.clean_all(st5, sh5, ps5, ms5, pos5, df5, comp = 'Club Cup') #club cup because there is no 'league' variable like BIG 5 has

data22_23 = f.merge_all(st5, sh5, ps5, ms5, pos5, df5)

data22_23 = f.edit_pos(data22_23)

data22_23['Nation'] = data22_23['Nation'].str.split().str[1] #removing 2 letter abreviation

data22_23 = f.dup_players(data22_23)

data22_23.isna().sum().sum() # 2 missing values 

missing3 = data22_23.loc[data22_23.isnull().sum(1) > 0]

print(missing3)

data22_23.at[142, 'Nation'] = 'NED' #Givario Read of club Volendam is from the Netherlands 

data22_23.at[440, 'Nation'] = 'CZE' #Tomas Hajek of club Vitesse is from Czechia

data22_23.isna().sum().sum() #0 missing values 

data22_23.insert(6, 'Comp', 'Eredivisie')

data22_23.to_csv('eridivisie22_23.csv', index=False)
