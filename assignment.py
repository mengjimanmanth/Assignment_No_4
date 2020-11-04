"""
Write python code that loads any dataset from (www.data.gov.in), and does some basic data cleaning. Add component on data set.
Use data Set for e.g. Health Data set
"""
import numpy as npy
import pandas as pand
from matplotlib import pyplot as plpt
import seaborn as seab


#loading the data/ reading the csv file
data_input = pand.read_csv('D:\\seaborn\\covid_dataset.csv')
print(data_input)

df = pand.DataFrame(data_input)

#simple 1 line graph
#title of graph
plpt.title('covid cases');

#ploting x-axis and y-axis
ax = seab.lineplot(x = 'State', y = 'Confirmed', data = data_input)

#increasing graph size
seab.set(rc={'figure.figsize':(12,10)})

#statistical operation
print('\ncomputing the summary of statistics\n',df.describe())

#show count of datset
print('count of dataset\n', df.count(axis=0))

#show shape of dataset
print('\nshape of dataset\n',df.shape)

#datafram converted to numpy array
print('converting the datafram to numpy array',df.to_numpy())

#transpose of matrix
print('\nTranspose of matrix\n',df.T)

print('printing some specific values',df.loc[[1,2],['State','Deaths']])

#modifing values to none
df['Cured'] = None
print(['Cured'])
