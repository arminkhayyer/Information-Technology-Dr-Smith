import numpy as np
import pandas as pd
import glob
path =r'C:\Users\oguzt\Desktop\to be done'
allFiles = glob.glob(path + "/*.csv")
list = [pd.read_csv(file,index_col = None, header = 0) for file in allFiles] 
#df = pd.concat(list, axis = 0, ignore_index = True)
#####################################################################
def convert_to_float(row):
    string = str(row["AMOUNT"]).replace(",", "")
    return float(string)
#####################################################################
def split_strings(row):
    string = row["PAYEE"].rsplit( "  ", maxsplit=3)
    return string[-1]
#df.dropna()
#f.dropna(subset=['PAYEE'], inplace=True)
#####################################################################
def split_strings2(row):
    string2 = row["OFFICE"]
    if string2[0:3]=='HON':
        ret = string2[5:]
    else:
        ret = string2
    return ret  
#####################################################################
def year_finder(row):
    string = row.QUARTER[0:4]
    return int(string)
#####################################################################
df = list[1]
df = df.loc[df["START DATE"] != '   ']
df['START DATE'].replace('', np.nan, inplace=True)
df.dropna(subset=['START DATE'], inplace=True)
df["START DATE"] = pd.to_datetime(df["START DATE"])
df = df.loc[df["END DATE"] != '   ']
df['END DATE'].replace('', np.nan, inplace=True)
df.dropna(subset=['END DATE'], inplace=True)
df["END DATE"] = pd.to_datetime(df["END DATE"])
df["AMOUNT"] = df.apply(lambda row: convert_to_float(row), axis =1)
df["PAYEE"] = df.apply(lambda row: split_strings(row), axis= 1)
df["YEAR"] = df.apply(lambda row: year_finder(row), axis= 1)
df["OFFICE"] = df.apply(lambda row: split_strings2(row), axis=1)
df.to_csv('2010 Q2.csv')
#####################################################################