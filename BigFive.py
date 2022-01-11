# -*- coding: utf-8 -*-
"""
@author: MWatson717
"""

import fifa_funcs as f

##### Data for 2017-2018 season #####
url = 'https://fbref.com/en/comps/Big5/2017-2018/2017-2018-Big-5-European-Leagues-Stats'

links, nxt = f.get_all_links(url)

links.sort()

for l in links:
    print(l)
    
print(nxt)
    
standard, shooting, passing, misc, pos, defense = f.get_data(links)

standard, shooting, passing, misc, pos, defense = f.clean_all(standard, shooting, passing, 
                                                              misc, pos, defense, comp = 'League')

data17_18 = f.merge_all(standard, shooting, passing, misc, pos, defense)

data17_18 = f.edit_pos(data17_18)

data17_18['Nation'] = data17_18['Nation'].str.split().str[1] #removing 2 letter abreviation
data17_18['Comp'] = data17_18['Comp'].str.split(' ', 1).str[1] #removing abbreviation

data17_18 = f.dup_players(data17_18) 

data17_18.isna().sum().sum() 

data17_18.to_csv('data17_18.csv', index=False)


##### Data for 2018-2019 season #####
links2, nxt2 = f.get_all_links(nxt)

links2.sort()

for l in links2:
    print(l) 
    
print(nxt2)

standard2, shooting2, passing2, misc2, pos2, defense2 = f.get_data(links2)

standard2, shooting2, passing2, misc2, pos2, defense2 = f.clean_all(standard2, shooting2, passing2, 
                                                                    misc2, pos2, defense2, comp = 'League')

data18_19 = f.merge_all(standard2, shooting2, passing2, misc2, pos2, defense2)

data18_19 = f.edit_pos(data18_19)

data18_19['Nation'] = data18_19['Nation'].str.split().str[1] 
data18_19['Comp'] = data18_19['Comp'].str.split(' ', 1).str[1]

#lets look at where there is a row with more than one missing column

missing = data18_19.loc[data18_19.isnull().sum(1) > 1]

print(missing)

idx = missing.index #want to drop player with index 1303 due to many missing values 

data18_19 = data18_19.drop(idx) 

data18_19 = f.dup_players(data18_19) 

data18_19.isna().sum().sum() 

data18_19.to_csv('data18_19.csv', index=False)


##### Data for 2019-2020 season #####
links3, nxt3 = f.get_all_links(nxt2)

links3.sort()

for l in links3:
    print(l) 
    
print(nxt3)

standard3, shooting3, passing3, misc3, pos3, defense3 = f.get_data(links3)

standard3, shooting3, passing3, misc3, pos3, defense3 = f.clean_all(standard3, shooting3, passing3, 
                                                                    misc3, pos3, defense3, comp = 'League')

data19_20 = f.merge_all(standard3, shooting3, passing3, misc3, pos3, defense3)

data19_20 = f.edit_pos(data19_20)

data19_20['Nation'] = data19_20['Nation'].str.split().str[1] 
data19_20['Comp'] = data19_20['Comp'].str.split(' ', 1).str[1]

data19_20 = f.dup_players(data19_20) 

data19_20.isna().sum().sum()

data19_20.to_csv('data19_20.csv', index=False)


##### Data for 2020-2021 season #####
links4, nxt4 = f.get_all_links(nxt3)

links4.sort()

for l in links4:
    print(l) 
    
print(nxt4)    
    
standard4, shooting4, passing4, misc4, pos4, defense4 = f.get_data(links)

standard4, shooting4, passing4, misc4, pos4, defense4 = f.clean_all(standard4, shooting4, passing4,
                                                                    misc4, pos4, defense4, comp = 'League')

data20_21 = f.merge_all(standard4, shooting4, passing4, misc4, pos4, defense4) 

data20_21 = f.edit_pos(data20_21) 

data20_21['Nation'] = data20_21['Nation'].str.split().str[1]

data20_21['Comp'] = data20_21['Comp'].str.split(' ', 1).str[1]

data20_21 = f.dup_players(data20_21) 

data20_21.isna().sum().sum()

data20_21.to_csv('data20_21.csv', index=False)
