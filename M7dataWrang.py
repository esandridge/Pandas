#Eric Sandridge, Module 7: Data Wrangling with Pandas
 

import pandas as pd
import numpy as np

#import data file to data frame using pandas data frame   
dfWeather = pd.read_csv('WburgWeather.csv')

#Function to convert Dry bulb temp data and dew point temp data to floating and convert to Celsius
#the function ignores values that cannot be converted by returning np.NaN, which will be removed below
def convertdrybulb(row):
    try:
        return (float(row['HOURLYDRYBULBTEMPF']) - 32) * 5/9
    except:
        return np.NaN
  
def convertdewpt(row):
    try:
        return (float(row['HOURLYDewPointTempF']) - 32) * 5/9
    except:
        return np.NaN

#Function to replace VRB acronym with 'variable direction' for clarity        
def vrb(row):
    if row['HOURLYWindDirection'] == 'VRB':
        return 'variable direction'
    else:
        return row['HOURLYWindDirection']

#apply functions created above to create new columns in Celsius
dfWeather['HOURLYDRYBULBTEMPC'] = dfWeather.apply(convertdrybulb,axis='columns')

dfWeather['HOURLYWETBULBTEMPC'] = (dfWeather['HOURLYWETBULBTEMPF'] - 32) * 5/9

dfWeather['HOURLYDewPointTempC'] = dfWeather.apply(convertdewpt, axis = 'columns')

#apply function to convert 'VRB' acronym to string
dfWeather['HOURLYWindDirection'] = dfWeather.apply(vrb,axis = 'columns')

#delete rows which include missing values
dfWeather.dropna(subset = ['HOURLYDRYBULBTEMPF'],inplace = True)
dfWeather.dropna(subset = ['HOURLYDewPointTempF'],inplace = True)
dfWeather.dropna(subset = ['HOURLYWETBULBTEMPF'],inplace = True)

#export modified data file to new .csv file
dfWeather.to_csv('newWeather.csv',index=False)






