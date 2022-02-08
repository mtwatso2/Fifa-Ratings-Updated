# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:51:04 2022

@author: MWatson717
"""

import fifa_funcs as f

########## FIFA 2019 Data ##########

url  = 'https://www.fifaindex.com/players/fifa19_282/?page=1'       #September 27 2018
last = 'https://www.fifaindex.com/players/fifa19_282/?page=604'

df19 = f.get_fut(url, last)

df19.to_csv('fifa19.csv', index=False)



########## FIFA 2020 Data ##########

url_20  = 'https://www.fifaindex.com/players/fifa20_358/?page=1'    #September 26 2019
last_20 = 'https://www.fifaindex.com/players/fifa20_358/?page=620'

df20 = f.get_fut(url_20, last_20) 

df20.to_csv('fifa20.csv', index=False)



########## FIFA 2021 Data ##########

url_21 = 'https://www.fifaindex.com/players/fifa21_423/?page=1'     #October 5 2020 

last_21 = 'https://www.fifaindex.com/players/fifa21_423/?page=633'

df21 = f.get_fut(url_21, last_21)

df21.to_csv('fifa21.csv', index=False)



########## FIFA 2022 Data ##########

url_22 = 'https://www.fifaindex.com/players/fifa22_490/?page=1'     #September 27 2021

last_22 = 'https://www.fifaindex.com/players/fifa22_490/?page=618'

df22 = f.get_fut(url_22, last_22)

df22.to_csv('fifa22.csv', index=False)