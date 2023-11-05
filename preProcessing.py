import pandas as pd
import numpy as np
from IPython.display import display


dfProducts = pd.read_csv('amazon_products.csv')
dfCategories = pd.read_csv('amazon_categories.csv')

# pd.set_option('display.max_rows', 100)

# print(dfProducts.to_string())

with pd.option_context('display.max_rows', 200, 'display.max_columns', None):  # more options can be specified also
    display(dfCategories)
    
with pd.option_context('display.max_rows', 200, 'display.max_columns', None):  # more options can be specified also
    display(dfProducts)
    
dfProducts.drop(['asin', 'imgUrl', 'productURL'], axis=1, inplace=True)

dfProducts['category_id'] = dfProducts['category_id'].map(dfCategories.set_index('id')['category_name'])

dfProducts.rename(columns={"category_id": "category"}, inplace=True)

with pd.option_context('display.max_rows', 200, 'display.max_columns', 8):  # more options can be specified also
    display(dfProducts)
    
dfProducts.to_csv('processedFile.csv')
print("hi")
