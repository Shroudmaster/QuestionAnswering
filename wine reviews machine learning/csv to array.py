import numpy as np
import pandas as pd
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

file = "train_set.csv"

df = pd.read_csv(file, header = 0, delimiter = ";")

original_headers = list(df.columns.values)

interested_headers = ['Hour (Coded)','Immobilized bus','Broken Truck','Vehicle excess','Accident victim','Running over','Fire vehicles','Occurrence involving freight','Incident involving dangerous freight','Lack of electricity','Fire','Point of flooding','Manifestations','Defect in the network of trolleybuses','Tree on the road','Semaphore off','Intermittent Semaphore']

points = list(df['Slowness in traffic (%)'])

target = list()
for p in points:
    plist = list()
    plist.append(p)
    target.append(plist)

dataset = list()


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
print(organized_dataset[0])
print(organized_dataset[1])
with open('organized_dataset.csv','w',newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(organized_dataset)
writeFile.close()

with open('target.csv','w',newline='') as targetFile:
    writer = csv.writer(targetFile)
    writer.writerows(target)
    
x = input("Enter to close")
