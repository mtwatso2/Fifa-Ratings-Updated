# Fifa-Ratings-Updated
Predicting FIFA player ratings using real life data

Real life data from fbref.com, FIFA Player rating data from fifaindex.com

## Files
- fifa_funcs.py: contains functions used in other python files
- BigFive.py: code for getting game data for the 'Big Five' leagues: England, Spain, France, Italy and Germany
- Tournament.py: code for getting game data for Club (Europa and Champions League) and International (Euro Cup, Copa America and World Cup) Tournaments
- Ratings.py: code for getting FIFA player ratings
- merge.py: code for merging all data together to be used for analysis
- FUT_data.csv: data created from merge.py, used in fifa.ipynd/fifa.pdf and Fifa 23 Update; contains data through the 2021-2022 season
- Variable Descriptions.pdf: contains descriptions of all variables in fut_data.csv
- FIFA.ipynb: Jupyter Notebook containing EDA and models
- FIFA.pdf: pdf version of Jupyter Notebook 
- Big Five Data: Folder containing data generated from BigFive.py
- Tournament Data: Folder containing data generated from Tournament.py
- FIFA 23 update.ipynb/.pdf: models predicting 'Overall' rating using most up to date data 
