import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_file_path="/config/workspace/aps_failure_training_set1.csv"
database_name="APS"
Collectiom_name= "sensor"


if __name__=="__main__":
    df= pd.read_csv(data_file_path)
    print(f"Rows and columns: {df.shape}")

#comment dataframe into JSON
df.reset_index(drop=True,inplace=True)

json_record=list(json.loads(df.T.to_json()).values())
print(json_record[0])

#insert converted json record to mongoDB
client[database_name][Collectiom_name].insert_many(json_record)