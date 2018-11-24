import numpy as np
import pandas as pd
import glob
path =r'D:\Auburn University\6 - Fall 2018\1- INSY 6500 Information Technology for Operations\Homeworks\Project\data'
allFiles = glob.glob(path + "/*.csv")
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col = None, header = 0)
    list_.append(df)
frame = pd.concat(list_, axis = 0, ignore_index = True)


k_ = frame.OFFICE
for k in k_:
    if k is str:
        print(1)
    else:
        print(2)
        
