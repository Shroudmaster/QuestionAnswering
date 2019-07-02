import matplotlib.pyplot as plt


knn_scores_ev = [0.19047619,0.2,0.33333333,0,0.11111111,0.25,0,0.33333333,0,0.33333333]
logreg_scores_ev = [0.19047619,0.2,0.33333333,0.33333333,0.22222222,0.25,0.16666667,0.66666667,0.25,0.33333333]

logreg_scores_sum = [0.047619047619047616, 0.2, 0.08333333333333333, 0.5555555555555556, 0.2222222222222222, 0.375, 0.16666666666666666, 0.5, 0.25, 0.3333333333333333]
knn_scores_sum = [0.14285714285714285, 0.13333333333333333, 0.08333333333333333, 0.1111111111111111, 0.4444444444444444, 0.125, 0.3333333333333333, 0.16666666666666666, 0.25, 0.3333333333333333]

knn_scores_hour = [0.047619047619047616, 0.06666666666666667, 0.08333333333333333, 0.1111111111111111, 0.2222222222222222, 0.375, 0.16666666666666666, 0.0, 0.0, 0.3333333333333333]
logreg_scores_hour = [0.0, 0.2, 0.08333333333333333, 0.3333333333333333, 0.2222222222222222, 0.25, 0.3333333333333333, 0.3333333333333333, 0.25, 0.0]


plt.plot([sum(knn_scores_ev)/len(knn_scores_ev),sum(knn_scores_ev)/len(knn_scores_ev),sum(knn_scores_ev)/len(knn_scores_ev)], marker = '', ls = '--', label = 'knn_scores_ev' )
plt.plot([sum(logreg_scores_ev)/len(logreg_scores_ev),sum(logreg_scores_ev)/len(logreg_scores_ev),sum(logreg_scores_ev)/len(logreg_scores_ev)], marker = '', ls = '--', label = 'logreg_scores_ev')
plt.plot([sum(knn_scores_sum)/len(knn_scores_sum),sum(knn_scores_sum)/len(knn_scores_sum),sum(knn_scores_sum)/len(knn_scores_sum)], marker = '', ls = '--', label = 'knn_scores_sum')
plt.plot([sum(logreg_scores_sum)/len(logreg_scores_sum),sum(logreg_scores_sum)/len(logreg_scores_sum),sum(logreg_scores_sum)/len(logreg_scores_sum)], marker = '', ls = '--', label = 'logreg_scores_sum')
plt.plot([sum(knn_scores_hour)/len(knn_scores_hour),sum(knn_scores_hour)/len(knn_scores_hour),sum(knn_scores_hour)/len(knn_scores_hour)], marker = '', ls = '--', label = 'knn_scores_hour')
plt.plot([sum(logreg_scores_hour)/len(logreg_scores_hour),sum(logreg_scores_hour)/len(logreg_scores_hour),sum(logreg_scores_hour)/len(logreg_scores_hour)], marker = '', ls = '--', label = 'logreg_scores_hour')
plt.title('Accuracy of different parameters choices and methods', loc='center')
plt.legend()
plt.show()
