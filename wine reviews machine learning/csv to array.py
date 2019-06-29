import numpy as np
import pandas as pd
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

file = "training_utf8.csv"

df = pd.read_csv(file, header = 0)

original_headers = list(df.columns.values)

interested_headers = ['country', 'designation', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery']

points = list(df['points'])

target = list()
for p in points:
    plist = list()
    plist.append(p)
    target.append(plist)

dataset = list()

dataset.append(list(df['index']))

for header in interested_headers:
    #column = list()
    column = le.fit_transform(list(df[header]))
    dataset.append(column)

organized_dataset = list()

for i in range(len(dataset[0])):
    line = list()
    for j in range(len(dataset)):
        line.append(dataset[j][i])
    organized_dataset.append(line)

with open('organized_dataset.csv','w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(organized_dataset)
writeFile.close()

with open('target.csv','w') as targetFile:
    writer = csv.writer(targetFile)
    writer.writerows(target)
    
x = input("Enter to close")
               
    


