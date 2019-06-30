import numpy as np
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.neural_network import MLPClassifier

v = True
training_dataset = list()
with open('organized_dataset.csv') as readFile:
    reader = csv.reader(readFile)
    training_dataset = list(reader)

for i in range(len(training_dataset)):
    for j in range(len(training_dataset[0])):
        training_dataset[i][j] = int(training_dataset[i][j])
               

print(training_dataset)

training_dataset = np.asarray(training_dataset,np.float64)
readFile.close()


#print(training_dataset[0],training_dataset[1])

training_target = list()
with open('target.csv') as readTarget:
    reader = csv.reader(readTarget)
    for row in reader:
        content = list(row)
        training_target = training_target + content

print(training_target)
for i in range(len(training_target)):
    training_target[i] = float(training_target[i])
    training_target[i] = int(training_target[i])
    

training_target = np.asarray(training_target)
readTarget.close()
#print(target[0],target[1])

testing_dataset = list()
with open('test_dataset.csv') as readFile:
    reader = csv.reader(readFile)
    testing_dataset = list(reader)

for i in range(len(testing_dataset)):
    for j in range(len(testing_dataset[0])):
        testing_dataset[i][j] = int(testing_dataset[i][j])

print(testing_dataset)

testing_dataset = np.asarray(testing_dataset)

readFile.close()



test_target = list()
with open('test_target.csv') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        content = list(row)
        test_target = test_target + content

#print(test_target)
for i in range(len(test_target)):
    test_target[i] = float(test_target[i])
    test_target[i] = int(test_target[i])

readFile.close()

neighbors = 10

knn = KNeighborsClassifier(n_neighbors=neighbors)

knn.fit(training_dataset,training_target)

target_predicted = knn.predict(testing_dataset)

for item in target_predicted:
    item = int(item)

accuracy = metrics.accuracy_score(test_target,target_predicted)

print(accuracy)
print(len(test_target))
print(len(target_predicted))
acu_list = []
acu_list.append(accuracy)

with open('predicted_knn_n=10.csv','w',newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(acu_list)
    writer.writerow(target_predicted)



clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(3, 10), momentum=0.75)
clf.fit(training_dataset,training_target)

target_predicted_clf = clf.predict(testing_dataset)
print(target_predicted_clf)

for item in target_predicted_clf:
    item = int(item)

accuracy = metrics.accuracy_score(test_target,target_predicted_clf)

print(accuracy)
print(test_target)
print(target_predicted_clf)
acu_list = []
acu_list.append(accuracy)

with open('predicted_mlp.csv','w',newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(acu_list)
    writer.writerow(target_predicted)

x = input("Enter to close")

