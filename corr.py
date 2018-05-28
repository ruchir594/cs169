import numpy as np
#import pandas as pd

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA

n_samples = 20

import csv
with open('data/child-mortality.csv', 'rb') as f:
    sr = csv.reader(f, delimiter=',')
    data = []
    for e in sr:
        data.append(e)

# data is data of all countries
ignore = []
filter = ['Afghanistan', 'Argentina', 'Australia', 'Bangladesh', 'Bhutan', 'Canada',
        'China', 'Congo', 'Germany', 'India', 'Japan', 'Russia', 'Rwanda','Singapore', 'Sri Lanka', 'Sweden',
        'Switzerland', 'United Kingdom', 'United States']
countries = []
data3years = []
for e in data:
    if len(e) < 3:
        temp = True # Do nothing
        #print e
    if len(e)>=4 and e[2] == '2014' and e[0] in filter:
        data3years.append([float(e[3])])
        countries.append(e[0])

countries.append('placeholder')
print len(countries)

years = ['2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004']
for year in years:
    i=0
    for e in data:
        if len(e) >=3 and e[2] == year and countries[i] == e[0]:
            data3years[i].append(float(e[3]))
            i+=1

data3years = np.array(data3years)
n_components = len(years)+1
print len(countries)
print data3years.shape
#countries = [chr(ord('A')+i) for i in range(20)]



import sys
#sys.exit()

seed = np.random.RandomState(seed=3)

X_true = data3years
n_samples = len(countries)-1

print X_true.shape
# Center the data
X_true -= X_true.mean()

similarities = euclidean_distances(X_true)

# Add noise to the similarities
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise

mds = manifold.MDS(n_components=n_components, max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_

nmds = manifold.MDS(n_components=n_components, metric=False, max_iter=3000, eps=1e-12,
                    dissimilarity="precomputed", random_state=seed, n_jobs=1,
                    n_init=1)
npos = nmds.fit_transform(similarities, init=pos)

# Rescale the data
pos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((pos ** 2).sum())
npos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((npos ** 2).sum())

# Rotate the data
clf = PCA(n_components=2)
X_true = clf.fit_transform(X_true)
print X_true.shape
pos = clf.fit_transform(pos)

npos = clf.fit_transform(npos)

fig = plt.figure(1)
ax = plt.axes([0., 0., 1., 1.])

s = 100
#plt.scatter(X_true[:, 0], X_true[:, 1], color='navy', s=s, lw=0,
#            label='True Position')
plt.scatter(pos[:, 0], pos[:, 1], color='turquoise', s=s, lw=0, label='MDS')
plt.scatter(npos[:, 0], npos[:, 1], color='darkorange', s=s, lw=0, label='NMDS')
plt.legend(scatterpoints=1, loc='best', shadow=False)

for label, x, y in zip(countries, pos[:, 0], pos[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.3', fc='black', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

similarities = similarities.max() / similarities * 100
similarities[np.isinf(similarities)] = 0

# Plot the edges
start_idx, end_idx = np.where(pos)
# a sequence of (*line0*, *line1*, *line2*), where::
#            linen = (x0, y0), (x1, y1), ... (xm, ym)
segments = [[X_true[i, :], X_true[j, :]]
            for i in range(len(pos)) for j in range(len(pos))]
values = np.abs(similarities)
lc = LineCollection(segments,
                    zorder=0, cmap=plt.cm.Blues,
                    norm=plt.Normalize(0, values.max()))
lc.set_array(similarities.flatten())
lc.set_linewidths(0.5 * np.ones(len(segments)))
ax.add_collection(lc)

plt.show()
