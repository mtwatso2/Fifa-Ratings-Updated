# -*- coding: utf-8 -*-
"""
@author: MWatson717
"""

import fifa_funcs as f

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4') #to ignore warning about using a list of links


##### Europa League 2018-2019 #####
url_eur = 'https://fbref.com/en/comps/19/2103/2018-2019-Europa-League-Stats'

links_europa = f.get_all_links(url_eur, lst=[], league = False)

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


##### Europa League 2021-2022 #####
standard4, shooting4, passing4, misc4, pos4, defense4 = f.get_data(links_europa[3], league = False) 

standard4, shooting4, passing4, misc4, pos4, defense4 = f.clean_all(standard4, shooting4, passing4, misc4,
                                                                    pos4, defense4, comp = 'Club Cup')

europa21_22 = f.merge_all(standard4, shooting4, passing4, misc4, pos4, defense4)

europa21_22 = f.edit_pos(europa21_22)

europa21_22['Nation'] = europa21_22['Nation'].str.split().str[1] 
europa21_22['Squad'] = europa21_22['Squad'].str.split().str[1]

europa21_22 = f.dup_players(europa21_22)

europa21_22.isna().sum().sum()

europa21_22.to_csv('europa21_22.csv', index=False)


##### Europa League 2022-2023 #####
standard5, shooting5, passing5, misc5, pos5, defense5 = f.get_data(links_europa[4], league = False)

standard5, shooting5, passing5, misc5, pos5, defense5 = f.clean_all(standard5, shooting5, passing5, misc5,
                                                                    pos5, defense5, comp = 'Club Cup')

europa22_23 = f.merge_all(standard5, shooting5, passing5, misc5, pos5, defense5)

europa22_23 = f.edit_pos(europa22_23)

europa22_23['Nation'] = europa22_23['Nation'].str.split().str[1] 
europa22_23['Squad'] = europa22_23['Squad'].str.split().str[1]

europa22_23 = f.dup_players(europa22_23)

europa22_23.isna().sum().sum() #no missing values 

europa22_23.to_csv('europa22_23.csv', index=False)



##### Champions League 2018-2019 ##### 
url_champ = 'https://fbref.com/en/comps/8/2102/2018-2019-Champions-League-Stats'

links_champ = f.get_all_links(url_champ, lst=[], league = False)

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

champ18_19.to_csv('ucl18_19.csv', index=False)


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

champ19_20.to_csv('ucl19_20.csv', index=False)


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

champ20_21.to_csv('ucl20_21.csv', index=False)


##### Champions League 2021-2022 #####
standard_cl4, shooting_cl4, passing_cl4, misc_cl4, pos_cl4, defense_cl4 = f.get_data(links_champ[3], league = False)
    
standard_cl4, shooting_cl4, passing_cl4, misc_cl4, pos_cl4, defense_cl4 = f.clean_all(standard_cl4, shooting_cl4,
                                                                                      passing_cl4, misc_cl4, pos_cl4, 
                                                                                      defense_cl4, comp='Club Cup')

champ21_22 = f.merge_all(standard_cl4, shooting_cl4, passing_cl4, misc_cl4, pos_cl4, defense_cl4)

champ21_22 = f.edit_pos(champ21_22)

champ21_22['Nation'] = champ21_22['Nation'].str.split().str[1] 
champ21_22['Squad'] = champ21_22['Squad'].str.split().str[1]

champ21_22 = f.dup_players(champ21_22)

champ21_22.isna().sum().sum()

champ21_22.to_csv('ucl21_22.csv', index=False)


##### Champions League 2022-2023 #####
standard_cl5, shooting_cl5, passing_cl5, misc_cl5, pos_cl5, defense_cl5 = f.get_data(links_champ[4], league = False)
    
standard_cl5, shooting_cl5, passing_cl5, misc_cl5, pos_cl5, defense_cl5 = f.clean_all(standard_cl5, shooting_cl5,
                                                                                      passing_cl5, misc_cl5, pos_cl5, 
                                                                                      defense_cl5, comp='Club Cup')

champ22_23 = f.merge_all(standard_cl5, shooting_cl5, passing_cl5, misc_cl5, pos_cl5, defense_cl5)

champ22_23 = f.edit_pos(champ22_23)

champ22_23['Nation'] = champ22_23['Nation'].str.split().str[1] 
champ22_23['Squad'] = champ22_23['Squad'].str.split().str[1]

champ22_23 = f.dup_players(champ22_23)

champ22_23.isna().sum().sum() # no missing values 

champ22_23.to_csv('ucl22_23.csv', index=False)



##### Conference League 2021-2022 #####
url_con = 'https://fbref.com/en/comps/882/2021-2022/stats/2021-2022-Europa-Conference-League-Stats'

links_con = f.get_all_links(url_con, lst=[], league = False)

st_cl, sh_cl, ps_cl, ms_cl, pos_cl, df_cl = f.get_data(links_con[0], league = False) 

st_cl, sh_cl, ps_cl, ms_cl, pos_cl, df_cl = f.clean_all(st_cl, sh_cl, ps_cl, ms_cl, pos_cl, df_cl, comp = 'Club Cup')

conference21_22 = f.merge_all(st_cl, sh_cl, ps_cl, ms_cl, pos_cl, df_cl)

conference21_22 = f.edit_pos(conference21_22)

conference21_22['Nation'] = conference21_22['Nation'].str.split().str[1]
conference21_22['Squad'] = conference21_22['Squad'].str.split().str[1]

conference21_22 = f.dup_players(conference21_22)  #2 missing values

missing = conference21_22.loc[conference21_22.isnull().sum(1) > 0]

print(missing) #2 players both missing country, lets find it

conference21_22.at[383, 'Nation'] = 'KAZ' #Jurij Medvedev of club Slovan is from Kazakhstan 

conference21_22.at[775, 'Nation'] = 'CZE' #Tomas Hajek of club Vitesse is from Czechia

conference21_22.isna().sum().sum()

conference21_22.to_csv('conference21_22.csv', index=False)



##### Conference League 2022-2023 #####
st_cl2, sh_cl2, ps_cl2, ms_cl2, pos_cl2, df_cl2 = f.get_data(links_con[1], league = False) 

st_cl2, sh_cl2, ps_cl2, ms_cl2, pos_cl2, df_cl2 = f.clean_all(st_cl2, sh_cl2, ps_cl2, 
                                                              ms_cl2, pos_cl2, df_cl2, comp = 'Club Cup')

conference22_23 = f.merge_all(st_cl2, sh_cl2, ps_cl2, ms_cl2, pos_cl2, df_cl2)

conference22_23 = f.edit_pos(conference22_23)

conference22_23['Nation'] = conference22_23['Nation'].str.split().str[1]
conference22_23['Squad'] = conference22_23['Squad'].str.split().str[1]

conference22_23 = f.dup_players(conference22_23)

conference22_23.isna().sum().sum() #No missing values 

missing2 = conference22_23.loc[conference22_23.isnull().sum(1) > 0]

print(missing2)

conference22_23.at[399, 'Nation'] = 'KAZ' #Jurij Medvedev of club Slovan is from Kazakhstan 

conference22_23.to_csv('conference22_23.csv', index=False)



##### 2021 Euro Cup #####
url_ec = 'https://fbref.com/en/comps/676/stats/UEFA-Euro-Stats'

links_ec = f.get_all_links(url_ec, lst=[], league = False)

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

ec_2021.isnull().sum().sum() 

ec_2021.to_csv('euro_cup_2021.csv', index=False)



##### 2021 Copa America #####
url_ca = 'https://fbref.com/en/comps/685/Copa-America-Stats'

links_ca = f.get_all_links(url_ca, lst=[], league = False)

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
url_wc = 'https://fbref.com/en/comps/1/2018/2018-World-Cup-Stats' 

links_wc = f.get_all_links(url_wc, [], league=False)

st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc = f.get_data(links_wc[0], league = False)

st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc = f.clean_all(st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc, comp='Int')

wc_2018 = f.merge_all(st_wc, sh_wc, pa_wc, mi_wc, po_wc, df_wc)

wc_2018 = f.edit_pos(wc_2018)

wc_2018 = wc_2018.rename(columns={'Squad':'Nation'})
wc_2018['Nation'] = wc_2018['Nation'].str.split().str[1] 

wc_2018 = f.dup_players(wc_2018)

wc_2018.isnull().sum().sum()

wc_2018.to_csv('world_cup_2018.csv', index = False)



##### 2022 World Cup #####
st_wc22, sh_wc22, pa_wc22, mi_wc22, po_wc22, df_wc22 = f.get_data(links_wc[1], league = False)

st_wc22, sh_wc22, pa_wc22, mi_wc22, po_wc22, df_wc22 = f.clean_all(st_wc22, sh_wc22, pa_wc22, mi_wc22,
                                                                   po_wc22, df_wc22, comp='Int', is22=True) 

wc_2022 = f.merge_all(st_wc22, sh_wc22, pa_wc22, mi_wc22, po_wc22, df_wc22)

wc_2022 = f.edit_pos(wc_2022)

wc_2022 = wc_2022.rename(columns={'Squad':'Nation'})
wc_2022['Nation'] = wc_2022['Nation'].str.split().str[1] 

wc_2022 = f.dup_players(wc_2022)

wc_2022.isnull().sum().sum()

wc_2022.to_csv('world_cup_2022.csv', index = False)
