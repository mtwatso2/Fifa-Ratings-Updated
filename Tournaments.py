# -*- coding: utf-8 -*-
"""
@author: MWatson717
"""

import fifa_funcs as f

##### Europa League 2018-2019 #####
url = 'https://fbref.com/en/comps/19/2103/2018-2019-Europa-League-Stats'

links_europa = f.get_all_links(url, lst = [], league = False)

standard, shooting, passing, misc, pos, defense = f.get_data(links_europa[0], league = False)

standard, shooting, passing, misc, pos, defense = f.clean_all(standard, shooting, passing, misc, 
                                                              pos, defense, comp = 'Club Cup')

europa18_19 = f.merge_all(standard, shooting, passing, misc, pos, defense)

europa18_19 = f.edit_pos(europa18_19)

europa18_19['Nation'] = europa18_19['Nation'].str.split().str[1] 
europa18_19['Squad'] = europa18_19['Squad'].str.split().str[1]

europa18_19 = f.dup_players(europa18_19)

europa18_19.isna().sum().sum()

europa18_19.to_csv('europa18_19.csv', index=False)


##### Europa League 2019-2020 #####
standard2, shooting2, passing2, misc2, pos2, defense2 = f.get_data(links_europa[1], league = False) 

standard2, shooting2, passing2, misc2, pos2, defense2 = f.clean_all(standard2, shooting2, passing2, misc2,
                                                                    pos2, defense2, comp = 'Club Cup')

europa19_20 = f.merge_all(standard2, shooting2, passing2, misc2, pos2, defense2)

europa19_20 = f.edit_pos(europa19_20)

europa19_20['Nation'] = europa19_20['Nation'].str.split().str[1] 
europa19_20['Squad'] = europa19_20['Squad'].str.split().str[1]

europa19_20 = f.dup_players(europa19_20)

europa19_20.isna().sum().sum()

europa19_20.to_csv('europa19_20.csv', index=False)


##### Europa League 2020-2021 #####
standard3, shooting3, passing3, misc3, pos3, defense3 = f.get_data(links_europa[2], league = False) 

standard3, shooting3, passing3, misc3, pos3, defense3 = f.clean_all(standard3, shooting3, passing3, misc3,
                                                                    pos3, defense3, comp = 'Club Cup')

europa20_21 = f.merge_all(standard3, shooting3, passing3, misc3, pos3, defense3)

europa20_21 = f.edit_pos(europa20_21)

europa20_21['Nation'] = europa20_21['Nation'].str.split().str[1] 
europa20_21['Squad'] = europa20_21['Squad'].str.split().str[1]

europa20_21 = f.dup_players(europa20_21)

europa20_21.isna().sum().sum()

europa20_21.to_csv('europa20_21.csv', index=False)



##### Champions League 2018-2019 ##### 
url_champ = 'https://fbref.com/en/comps/8/2102/2018-2019-Champions-League-Stats'

links_champ = f.get_all_links(url_champ, lst = [], league = False)

standard_cl, shooting_cl, passing_cl, misc_cl, pos_cl, defense_cl = f.get_data(links_champ[0], league = False)    

standard_cl, shooting_cl, passing_cl, misc_cl, pos_cl, defense_cl = f.clean_all(standard_cl, shooting_cl, passing_cl, 
                                                                                misc_cl, pos_cl, defense_cl, 
                                                                                comp='Club Cup')

champ18_19 = f.merge_all(standard_cl, shooting_cl, passing_cl, misc_cl, pos_cl, defense_cl)

champ18_19 = f.edit_pos(champ18_19)

champ18_19['Nation'] = champ18_19['Nation'].str.split().str[1] 
champ18_19['Squad'] = champ18_19['Squad'].str.split().str[1]

champ18_19 = f.dup_players(champ18_19)

champ18_19.isna().sum().sum()

champ18_19.to_csv('champ18_19.csv', index=False)


##### Champions League 2019-2020 #####
standard_cl2, shooting_cl2, passing_cl2, misc_cl2, pos_cl2, defense_cl2 = f.get_data(links_champ[1], league = False)
    
standard_cl2, shooting_cl2, passing_cl2, misc_cl2, pos_cl2, defense_cl2 = f.clean_all(standard_cl2, shooting_cl2,
                                                                                      passing_cl2, misc_cl2, pos_cl2, 
                                                                                      defense_cl2, comp='Club Cup')

champ19_20 = f.merge_all(standard_cl2, shooting_cl2, passing_cl2, misc_cl2, pos_cl2, defense_cl2)

champ19_20 = f.edit_pos(champ19_20)

champ19_20['Nation'] = champ19_20['Nation'].str.split().str[1] 
champ19_20['Squad'] = champ19_20['Squad'].str.split().str[1]

champ19_20 = f.dup_players(champ19_20)

champ19_20.isna().sum().sum()

champ19_20.to_csv('champ19_20.csv', index=False)


##### Champions League 2020-2021 #####
standard_cl3, shooting_cl3, passing_cl3, misc_cl3, pos_cl3, defense_cl3 = f.get_data(links_champ[2], league = False)
    
standard_cl3, shooting_cl3, passing_cl3, misc_cl3, pos_cl3, defense_cl3 = f.clean_all(standard_cl3, shooting_cl3,
                                                                                      passing_cl3, misc_cl3, pos_cl3, 
                                                                                      defense_cl3, comp='Club Cup')

champ20_21 = f.merge_all(standard_cl3, shooting_cl3, passing_cl3, misc_cl3, pos_cl3, defense_cl3)

champ20_21 = f.edit_pos(champ20_21)

champ20_21['Nation'] = champ20_21['Nation'].str.split().str[1] 
champ20_21['Squad'] = champ20_21['Squad'].str.split().str[1]

champ20_21 = f.dup_players(champ20_21)

champ20_21.isna().sum().sum()

champ20_21.to_csv('champ20_21.csv', index=False)



##### 2021 Euro Cup #####
url_ec = 'https://fbref.com/en/comps/676/stats/UEFA-Euro-Stats'

links_ec = f.get_all_links(url_ec, lst = [], league = False)

standard_EC, shooting_EC, passing_EC, misc_EC, pos_EC, defense_EC = f.get_data(links_ec[0], league = False)

standard_EC, shooting_EC, passing_EC, misc_EC, pos_EC, defense_EC = f.clean_all(standard_EC, shooting_EC, 
                                                                                passing_EC, misc_EC, pos_EC, 
                                                                                defense_EC, comp = 'Int')

ec_2021 = f.merge_all(standard_EC, shooting_EC, passing_EC, misc_EC, pos_EC, defense_EC)

ec_2021 = f.edit_pos(ec_2021)

ec_2021 = ec_2021.rename(columns={'Squad':'Nation'})
ec_2021['Nation'] = ec_2021['Nation'].str.split().str[1] 

ec_2021 = f.dup_players(ec_2021)

ec_2021 = ec_2021.fillna(0)

ec_2021.isnull().sum().sum() #just missing values (141) from avg shot distance, fill with 0

ec_2021.to_csv('euro_cup_2021.csv', index=False)



##### 2021 Copa America #####
url_ca = 'https://fbref.com/en/comps/685/Copa-America-Stats'

links_ca = f.get_all_links(url_ca, lst= [], league = False)

standard_CA, shooting_CA, passing_CA, misc_CA, pos_CA, defense_CA = f.get_data(links_ca[0], league = False)

standard_CA, shooting_CA, passing_CA, misc_CA, pos_CA, defense_CA = f.clean_all(standard_CA, shooting_CA, 
                                                                                passing_CA, misc_CA, pos_CA, 
                                                                                defense_CA, comp = 'Int')

ca_2021 = f.merge_all(standard_CA, shooting_CA, passing_CA, misc_CA, pos_CA, defense_CA)

ca_2021 = f.edit_pos(ca_2021)

ca_2021 = ca_2021.rename(columns={'Squad':'Nation'})
ca_2021['Nation'] = ca_2021['Nation'].str.split().str[1] 

ca_2021 = f.dup_players(ca_2021)

ca_2021 = ca_2021.fillna(0)

ca_2021.isnull().sum().sum()

ca_2021.to_csv('copa_america_2021.csv', index = False)



##### 2018 World Cup #####
url_wc = 'https://fbref.com/en/comps/1/FIFA-World-Cup-Stats'

links_wc = f.get_all_links(url_wc, lst = [], league=False)

st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc = f.get_data(links_wc, league = False)

st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc = f.clean_all(st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc, comp='Int') 

wc_2018 = f.merge_all(st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc)

wc_2018 = f.edit_pos(wc_2018)

wc_2018 = wc_2018.rename(columns={'Squad':'Nation'})
wc_2018['Nation'] = wc_2018['Nation'].str.split().str[1] 

wc_2018 = f.dup_players(wc_2018)

wc_2018.isnull().sum().sum()

wc_2018.to_csv('world_cup_2018.csv', index = False)
