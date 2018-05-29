import numpy as np
#import pandas as pd

import csv
with open('data/child-mortality.csv', 'rb') as f:
    sr = csv.reader(f, delimiter=',')
    data = []
    for e in sr:
        data.append(e)

# data is data of all countries
country = 'Sri Lanka'
mort = []

years = [2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004]
years = years[::-1]
for i in range(len(data)):
    if len(data[i]) >=3 and country == data[i][0] and data[i][2] == str(years[0]):
        for j in range(len(years)):
            mort.append(float(data[i+j][3]))
        break

mort = np.array(mort)


with open('data/World_Bank_Data.csv', 'rb') as f:
    sr = csv.reader(f, delimiter=',')
    data = []
    for e in sr:
        data.append(e)
        break
    for e in sr:
        if e[0] == country:
            data.append(e)


print len(data)
print data[0]

# index 1 is access to electricity !!!
feature_index = [1, 42, 2, 26, 146, 160, 47]
feature_vector = []
feature_name = []
for index in feature_index:
    feature_vector.append([])
    feature_name.append(data[index][2])
    for year in years:
        j = year-1990+4
        feature_vector[-1].append(float(data[index][j]))


print 'Debug statistics'
print len(mort)#, mort
print len(feature_name), feature_name
print len(feature_vector), len(feature_vector[0])#, feature_vector


from scipy.stats.stats import pearsonr

cors = []
for i in range(len(feature_vector)):
    cors.append(pearsonr(mort, feature_vector[i])[0])

import matplotlib.pyplot as plt
plt.bar(np.arange(len(cors)), cors, align='center', alpha=0.5)
plt.xticks(np.arange(len(cors)), feature_name, rotation=-8, size='small', horizontalalignment='left')
plt.ylabel('Correlation')
plt.show()
