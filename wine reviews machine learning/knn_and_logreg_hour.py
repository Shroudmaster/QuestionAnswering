from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

#wine = datasets.load_wine()
#X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.2)

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = [4.1, 6.6, 8.7, 9.2, 11.1, 10.9, 8.3, 8.2, 7.6, 6.4, 5.2, 4.7, 4.8, 4.9, 5.1, 5.3, 6.9, 5.1, 6.7, 8.1, 9.5, 9.4, 9.9, 11.2, 11.8, 11.4, 7.4, 4.9, 6.3, 8.0, 9.5, 10.3, 9.5, 7.9, 7.7, 8.3, 8.5, 8.5, 7.4, 8.7, 7.8, 8.1, 8.3, 8.3, 8.4, 9.3, 11.0, 12.1, 13.1, 13.7, 15.3, 16.8, 15.6, 11.0, 3.4, 3.8, 5.3, 5.9, 7.0, 7.4, 6.2, 6.5, 6.7, 7.7, 8.7, 8.2, 8.0, 6.2, 6.8, 8.0, 9.2, 10.1, 12.2, 13.9, 15.0, 17.1, 19.6, 20.2, 22.6, 23.4, 19.3, 4.0, 5.0, 5.7, 5.6, 8.5, 7.6, 7.6, 6.6, 7.4, 7.7, 7.7, 7.9]

line = list()
train = list()
for x in t:
    line.append(x)
    train.append(line)

for x in range(len(target)):
    target[x] = float(target[x])
    target[x] = int(target[x])
    

X_train, X_test, y_train, y_test = train_test_split(train, target, test_size=0.2)

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=3)

#Train the model using the training sets
#knn.fit(X_train, y_train)

#Predict the response for test dataset
#y_pred = knn.predict(X_test)

knn_scores = cross_val_score(knn, train, target, cv = 10, scoring='accuracy')

knn = KNeighborsClassifier(n_neighbors=3)
knn_scores_precision = cross_val_score(knn,  train, target, cv = 10, scoring ='precision_micro')

knn = KNeighborsClassifier(n_neighbors=3)
knn_scores_f1 = cross_val_score(knn,  train, target, cv = 10, scoring ='f1_micro')



# Model Accuracy, how often is the classifier correct?
print("Accuracy:",knn_scores.mean())
print("Precision:",knn_scores_precision.mean())
print("F1:",knn_scores_f1.mean())

logreg = LogisticRegression()

#logreg.fit(X_train, y_train)

#logreg_predict = logreg.predict(X_test)

logreg_scores = cross_val_score(logreg, train, target, cv = 10, scoring='accuracy')
logreg_scores_precision = cross_val_score(logreg,  train, target, cv = 10, scoring ='precision_micro') 
logreg_scores_f1 = cross_val_score(logreg,  train, target, cv = 10, scoring ='f1_micro')

print("Accuracy:",logreg_scores.mean())
print("Precision:",logreg_scores_precision.mean())
print("F1:",logreg_scores_f1.mean())
a = input("Enter to close")
