import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.ensemble import BaggingClassifier, VotingClassifier
#print(data.Immobilized_bus)
#hour = plt.plot(data.Hour_Coded, ls = '', marker = 'o', label = "hour")
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = [4.1, 6.6, 8.7, 9.2, 11.1, 10.9, 8.3, 8.2, 7.6, 6.4, 5.2, 4.7, 4.8, 4.9, 5.1, 5.3, 6.9, 5.1, 6.7, 8.1, 9.5, 9.4, 9.9, 11.2, 11.8, 11.4, 7.4, 4.9, 6.3, 8.0, 9.5, 10.3, 9.5, 7.9, 7.7, 8.3, 8.5, 8.5, 7.4, 8.7, 7.8, 8.1, 8.3, 8.3, 8.4, 9.3, 11.0, 12.1, 13.1, 13.7, 15.3, 16.8, 15.6, 11.0, 3.4, 3.8, 5.3, 5.9, 7.0, 7.4, 6.2, 6.5, 6.7, 7.7, 8.7, 8.2, 8.0, 6.2, 6.8, 8.0, 9.2, 10.1, 12.2, 13.9, 15.0, 17.1, 19.6, 20.2, 22.6, 23.4, 19.3, 4.0, 5.0, 5.7, 5.6, 8.5, 7.6, 7.6, 6.6, 7.4, 7.7, 7.7, 7.9]

line = list()
train = list()
for x in t:
    line = []
    line.append(x)
    train.append(line)

for x in range(len(target)):
    target[x] = float(target[x])
    target[x] = int(target[x])

X_train, X_test, y_train, y_test = train_test_split(train, target, test_size=0.2)

baggin = BaggingClassifier(KNeighborsClassifier(), n_estimators = 53, max_samples = 0.5, max_features = 0.5)

baggin.fit(X_train, y_train)
voter = VotingClassifier(baggin)

plt.plot(baggin.predict(X_test), marker = 'o', ls = '')
plt.show()
