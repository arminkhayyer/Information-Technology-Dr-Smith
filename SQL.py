import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:arminkhayyer@localhost/infoIt', echo=False)
conn = engine.connect()
conn.execute("SET GLOBAL max_allowed_packet= 1073741824;")
conn.close()


df = pd.read_csv("../cleaned-data.csv")
df.to_sql(name='cleaned_data', con=engine, if_exists = 'replace', index=False)
print ("cleaned data done")
dflegis = pd.read_csv("../legislators_updated.csv")
df.to_sql(name='legislation', con=engine, if_exists = 'replace', index=False)