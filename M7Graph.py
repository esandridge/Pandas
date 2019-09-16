#Eric Sandridge, Module 7: Graphing with Pandas

import pandas as pd
import matplotlib.pyplot as plt

#Input data using pandas dataframe
df_oz = pd.read_csv('ozone.csv')

#Calculate correlation between variables in the ozone data
dfCorr = df_oz.corr()
dfCorr

#Graph variables with high correlation
fig, ax = plt.subplots()
ax.scatter(dfCorr['ozone'], dfCorr['temperature'], c='r', alpha = 0.5,s = 75)
ax.xaxis.set_label_text('Ozone', fontsize = 16)
ax.yaxis.set_label_text('Temperature', fontsize = 16)
ax.xaxis.set_tick_params(labelsize=14)
ax.yaxis.set_tick_params(labelsize=14)

#Title scatterplot and save scatterplot to file
fig.suptitle('Correlation between Ozone and Temperature', fontsize = 20)
fig.set_size_inches(10,7)
fig.savefig('ozHi.jpg')


#Graph variables with low correlation
fig, ax = plt.subplots()
ax.scatter(dfCorr['wind'], dfCorr['radiation'], c='b', alpha = 0.5,s = 75)
ax.xaxis.set_label_text('Wind', fontsize = 16)
ax.yaxis.set_label_text('Radiation', fontsize = 16)
ax.xaxis.set_tick_params(labelsize=14)
ax.yaxis.set_tick_params(labelsize=14)


#Title scatterplot and save scatterplot to file
fig.suptitle('Correlation between Wind and Radiation', fontsize = 20)
fig.set_size_inches(10,7)
fig.savefig('ozLo.jpg')



