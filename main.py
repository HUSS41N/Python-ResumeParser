import os
from pyresparser import ResumeParser
path = 'socialmedia'
files = os.listdir(path)
excelData= [];

for file in files:
    data = ResumeParser(f"socialmedia/{file}").get_extracted_data()
    dict = {};
    dict["name"] = data['name']
    dict["email"] = data['email']
    dict["mobile_number"] = data['mobile_number']
    dict["total_experience"] = data['total_experience']
    excelData.append(dict)

import pandas as pd
df = pd.DataFrame.from_dict(excelData)
print (df)
df.to_excel('socialmedia.xlsx')
