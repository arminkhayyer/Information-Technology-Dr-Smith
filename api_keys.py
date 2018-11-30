from congress import Congress
import numpy as np
import pandas as pd
import time



api_key = 'Z7cnuQ3cufA08VfbWOoqURVpeSUuyT8QQazVwAGY'
congress = Congress(api_key)

print(congress.members.get("R000575"))

'''
df = pd.read_csv("../cleaned-data.csv")
bio_guides_ID= df["BIOGUIDE_ID"].unique()[1:]




dflegis = pd.read_csv("../legislators.csv")
dflegis = dflegis[["title", "firstname", "middlename", "lastname", "party", "state", "in_office", "gender", "bioguide_id", "govtrack_id"]]
# get member by bioguide ID
print(dflegis)
bios = list(dflegis.bioguide_id)



outof_bio = []
for i in bio_guides_ID:
    if not i in bios:
        outof_bio.append(i)
print(outof_bio)

legislators = []
for i in outof_bio[1:]:
    try:
        legislators.append(congress.members.get(i) )
        print(i,congress.members.get(i))
    except:
        pass


newdf = pd.DataFrame.from_dict(legislators)

newdf = newdf[[ "first_name",	"middle_name",	"last_name","in_office", "gender"	,"member_id",	"govtrack_id"]]


newdf.to_csv("../newdf.csv")'''
