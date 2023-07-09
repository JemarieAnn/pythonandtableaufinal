# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:20:58 2023

@author: user
"""
import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv', sep=';')

# summary of data
data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberofItemsPurchases
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
SellingPricePerItem = data['SellingPricePerItem']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding new column to a dataframe
data['CostPerTransaction'] = CostPerTransaction

#Sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Mark Up Calculation (Sales - Cost) / Cost
data['MarkUp'] = (data['ProfitPerTransaction'] / data['CostPerTransaction'])

#Rounding Marking
roundMarkup = round(data['MarkUp'], 2)
data['MarkUp'] = round(data['MarkUp'], 2)

#Combining data fields
my_name = 'jemarie'+'ann'

#my_date = data['Day'] + '-'

#checking columns data type
print(data['Day'].dtype)

#change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['Date'] = my_date

#using iloc to view specific columns/rows
data.iloc[0] #views the rows with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows in the 2nd column
data.iloc[4,2] #brings in 4th row, 2nd column

#using split to split the client_keywords field
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns
# df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Year', axis = 1)
data = data.drop(['Month', 'Day'] , axis = 1)

#Export into csv

data.to_csv('ValueInc_Cleaned.csv', index = False)














