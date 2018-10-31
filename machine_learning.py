import pandas as pd
#import build_table
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn import svm
from sklearn.preprocessing import LabelEncoder


matchup_data = pd.read_csv('compiled_stats_week6.csv', index_col=0)
#print(matchup_data.to_string())

le = LabelEncoder()
matchup_data['opp_enc'] = le.fit_transform(matchup_data['Opp'])
print(matchup_data['opp_enc'].to_string())


x_data = matchup_data[['OFF RK (YDS)', 'OFF YDS/G', 'PTS FOR/G', 'H/A']]
#x_data = matchup_data[['W', 'L', 'T', 'PCT', 'PF', 'PA', 'DIFF', 'AVG LINE', 'OFF RK (YDS)', 'OFF YDS/G', 'PTS FOR/G', 'DEF RK (YDS)', 'YDS ALWD/G', 'PTS ALWD/G', 'H/A']]#, 'Total Inj', 'Non-IR', 'IR']]
y_data = matchup_data[['Winner']]
#y_data = y_data.ravel()

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)

#print(x_train)
#print(y_train)
#print(x_test)
#print(y_test)
clf = svm.SVC(kernel='linear').fit(x_train,y_train)
#clf.fit(x_train,y_train)
#clf.score(x_train,y_train)
y_pred = clf.predict(x_test)
print(y_pred)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))
print(clf.coef_)

