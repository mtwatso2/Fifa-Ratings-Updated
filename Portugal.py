# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:56:02 2023

@author: MWatson717
"""

import fifa_funcs_2623 as f

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4') #to ignore warning about using a list of links


##### Primeira Liga (Portugal) 2018-2019 #####
url1 = 'https://fbref.com/en/comps/32/2018-2019/2018-2019-Primeira-Liga-Stats'

links = f.get_all_links(url1, other=True)
    
st, sh, ps, ms, pos, df = f.get_data(links[0], league = False) #need league = False here to get the player data instead of team 

st, sh, ps, ms, pos, df = f.clean_all(st, sh, ps, ms, pos, df, comp = 'Club Cup') #because there is no 'league' variable like BIG 5 has

primeira18_19 = f.merge_all(st, sh, ps, ms, pos, df)

primeira18_19 = f.edit_pos(primeira18_19)

primeira18_19['Nation'] = primeira18_19['Nation'].str.split().str[1] #removing 2 letter abreviation

primeira18_19 = f.dup_players(primeira18_19)

primeira18_19.isna().sum().sum() #1 missing

missing = primeira18_19.loc[primeira18_19.isnull().sum(1) > 0]

print(missing) # a quick google search shows that this player is from Brazil; index 68

primeira18_19.at[68, 'Nation'] = 'BRA'

primeira18_19.isna().sum().sum() #no more missing values

primeira18_19.insert(6, 'Comp', 'Primeira Liga')

primeira18_19.to_csv('primeira18_19.csv', index=False)


##### Primeira Liga (Portugal) 2019-2020 #####
st2, sh2, ps2, ms2, pos2, df2 = f.get_data(links[1], league = False) #need league = False here to get the player data instead of team 

st2, sh2, ps2, ms2, pos2, df2 = f.clean_all(st2, sh2, ps2, ms2, pos2, df2, comp = 'Club Cup') #because there is no 'league' variable like BIG 5 has

primeira19_20 = f.merge_all(st2, sh2, ps2, ms2, pos2, df2)

primeira19_20 = f.edit_pos(primeira19_20)

primeira19_20['Nation'] = primeira19_20['Nation'].str.split().str[1] #removing 2 letter abreviation

primeira19_20 = f.dup_players(primeira19_20)

primeira19_20.isna().sum().sum()

missing2 = primeira19_20.loc[primeira19_20.isnull().sum(1) > 0]

print(missing2)#same player as last year is missing nation again, he is index 63 this year 

primeira19_20.at[63, 'Nation'] = 'BRA'

primeira19_20.isna().sum().sum() #fixed the missing value 

primeira19_20.insert(6, 'Comp', 'Primeira Liga')

primeira19_20.to_csv('primeira19_20.csv', index=False)


##### Primeira Liga (Portugal) 2020-2021 #####
st3, sh3, ps3, ms3, pos3, df3 = f.get_data(links[2], league = False) #need league = False here to get the player data instead of team 

st3, sh3, ps3, ms3, pos3, df3 = f.clean_all(st3, sh3, ps3, ms3, pos3, df3, comp = 'Club Cup') #because there is no 'league' variable like BIG 5 has

primeira20_21 = f.merge_all(st3, sh3, ps3, ms3, pos3, df3)

primeira20_21 = f.edit_pos(primeira20_21)

primeira20_21['Nation'] = primeira20_21['Nation'].str.split().str[1] #removing 2 letter abreviation

primeira20_21 = f.dup_players(primeira20_21)

primeira20_21.isna().sum().sum() #1 missing value, probably the same guy again

missing3 = primeira20_21.loc[primeira20_21.isnull().sum(1) > 0]

print(missing3)#same player as last year is missing nation again, he is index 62 this year 

primeira20_21.at[62, 'Nation'] = 'BRA'

primeira20_21.isna().sum().sum() #fixed the missing value 

primeira20_21.insert(6, 'Comp', 'Primeira Liga')

primeira20_21.to_csv('primeira20_21.csv', index=False)


##### Primeira Liga (Portugal) 2021-2022 #####
st4, sh4, ps4, ms4, pos4, df4 = f.get_data(links[3], league = False) #need league = False here to get the player data instead of team 

st4, sh4, ps4, ms4, pos4, df4 = f.clean_all(st4, sh4, ps4, ms4, pos4, df4, comp = 'Club Cup') #because there is no 'league' variable like BIG 5 has

primeira21_22 = f.merge_all(st4, sh4, ps4, ms4, pos4, df4)

primeira21_22 = f.edit_pos(primeira21_22)

primeira21_22['Nation'] = primeira21_22['Nation'].str.split().str[1] #removing 2 letter abreviation

primeira21_22 = f.dup_players(primeira21_22)

primeira21_22.isna().sum().sum() #1 missing value, probably the same guy again

missing4 = primeira21_22.loc[primeira21_22.isnull().sum(1) > 0]

print(missing4)#same player as last year is missing nation again, he is index 70 this year 

primeira21_22.at[70, 'Nation'] = 'BRA'

primeira21_22.isna().sum().sum() #fixed the missing value 

primeira21_22.insert(6, 'Comp', 'Primeira Liga')

primeira21_22.to_csv('primeira21_22.csv', index=False)


##### Primeira Liga (Portugal) 2022-2023 #####
st5, sh5, ps5, ms5, pos5, df5 = f.get_data(links[4], league = False) #need league = False here to get the player data instead of team 

st5, sh5, ps5, ms5, pos5, df5 = f.clean_all(st5, sh5, ps5, ms5, pos5, df5, comp = 'Club Cup') #because there is no 'league' variable like BIG 5 has

primeira22_23 = f.merge_all(st5, sh5, ps5, ms5, pos5, df5)

primeira22_23 = f.edit_pos(primeira22_23)

primeira22_23['Nation'] = primeira22_23['Nation'].str.split().str[1] #removing 2 letter abreviation

primeira22_23 = f.dup_players(primeira22_23)

primeira22_23.isna().sum().sum() #No missing values 

primeira22_23.insert(6, 'Comp', 'Primeira Liga')

primeira22_23.to_csv('primeira22_23.csv', index=False)

