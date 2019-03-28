#!/usr/bin/env python
# coding: utf-8

# In[12]:


import json
import csv
headers = True
review_file = './data/yelp-dataset/data_CSV/yelp_academic_dataset_review.json'
review_output='./data/yelp-dataset/data_CSV/review.csv'




with open(review_file,encoding="utf-8" ) as jsonf, open(review_output,"w",encoding="utf-8") as csvf:
    for line in jsonf:
        data = json.loads(line)
        if headers:
            keys =[]
            for k,v in data.items():
                keys.append(k)
                writer = csv.DictWriter(csvf,fieldnames=keys,lineterminator = '\n')
            writer.writeheader()
            headers=False
        else:        
            writer.writerow(data)
                
        


# In[1]:


import pandas as pd
import numpy as np

business_df = pd.read_csv('./data/yelp-dataset/data_CSV/business.csv')
#business_df=business_df.apply(lambda x: x.astype(str).str.lower())
business_df=business_df.dropna(how='any')
business_df=business_df[business_df['categories'].str.contains("Restaurants")]
business_df=business_df[~business_df['city'].str.contains("Toronto")]
 
business_df=business_df[:75000]
#business_df.to_csv('./data/yelp-dataset/data_CSV/Restaurant_business.csv')


# In[3]:


import pandas as pd
import numpy as np

list=business_df['business_id']
newList = []
for value in list:
    newList.append(value)

#print(newList)    
#review_df = pd.read_csv('./data/yelp-dataset/data_CSV/review.csv')
#review_df=review_df.dropna(how='any')

#print(list)
#review_dtaframe= review_df[review_df['business_id'].isin(newList)]
#print(review_dtaframe.head())
#review_dtaframe =review_dtaframe[:100000]
#review_dtaframe.to_csv('./data/yelp-dataset/data_CSV/review_compressed.csv')



tip_df = pd.read_csv('./data/yelp-dataset/data_CSV/checkin.csv')
tip_df=tip_df.dropna(how='any')
tip_df= tip_df[tip_df['business_id'].isin(newList)]
tip_df.to_csv('./data/yelp-dataset/data_CSV/checkin_compressed.csv')




# In[5]:



list=review_dtaframe['user_id']
newList = []
for value in list:
    newList.append(value)


user_df = pd.read_csv('./data/yelp-dataset/data_CSV/user.csv')
user_df=user_df.dropna(how='any')
user_df= user_df[user_df['user_id'].isin(newList)]
user_df.to_csv('./data/yelp-dataset/data_CSV/user_compressed.csv')


# 
# 
