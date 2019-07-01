import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.ensemble import BaggingClassifier
trainer = pd.read_csv('organized_dataset.csv')
tester = pd.read_csv('test_dataset.csv')
#print(data.Immobilized_bus)
#hour = plt.plot(data.Hour_Coded, ls = '', marker = 'o', label = "hour")
baggin = BaggingClassifier(n_estimator = 10, KNeighborsClassifier(), max_samples = 0.5, max_features = 0.5)
bagging.fit(trainer, tester)
#plt.plot(data, marker = 'o', ls = '')
#plt.show()
