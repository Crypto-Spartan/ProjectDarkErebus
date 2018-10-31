
import pandas as pd
#import build_table
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn import svm

np.set_printoptions(suppress=True)
pd.set_option('max_columns', 50)


week5 = pd.read_csv('final_matchups_week5.csv', index_col=0)
week6 = pd.read_csv('final_matchups_week6.csv', index_col=0)
week7 = pd.read_csv('final_matchups_week7.csv', index_col=0)

matchup_data = pd.concat([week5, week6])
matchup_data = matchup_data.reset_index()
#print(matchup_data.to_string())
#print(week7[['AwT_TotInj','AwT_NonIR','AwT_IR']].isnull())
#print(matchup_data.isstring().sum().to_string())


#dummy = pd.get_dummies(matchup_data)
#dummy.to_csv('dummy.csv')
#print(dummy)



x_data = matchup_data[['Away Line','Home Line','AwT_W','AwT_L','AwT_T','AwT_Pct','AwT_PF','AwT_PA','AwT_PtDiff','AwT_Strk','AwT_OffRk(yds)','AwT_OffYds/G','AwT_PF/G','AwT_DefRk(yds)','AwT_YdsAlwd/G','AwT_PtsAlwd/G','AwT_TotInj','AwT_NonIR','AwT_IR','HmT_W','HmT_L','HmT_T','HmT_Pct','HmT_PF','HmT_PA','HmT_PtDiff','HmT_Strk','HmT_OffRk(yds)','HmT_OffYds/G','HmT_PF/G','HmT_DefRk(yds)','HmT_YdsAlwd/G','HmT_PtsAlwd/G','HmT_TotInj','HmT_NonIR','HmT_IR','Away Team_New England Patriots','Home Team_New England Patriots','Away Team_Miami Dolphins','Home Team_Miami Dolphins','Away Team_New York Jets','Home Team_New York Jets','Away Team_Buffalo Bills','Home Team_Buffalo Bills','Away Team_Cincinnati Bengals','Home Team_Cincinnati Bengals','Away Team_Baltimore Ravens','Home Team_Baltimore Ravens','Away Team_Pittsburgh Steelers','Home Team_Pittsburgh Steelers','Away Team_Cleveland Browns','Home Team_Cleveland Browns','Away Team_Tennessee Titans','Home Team_Tennessee Titans','Away Team_Houston Texans','Home Team_Houston Texans','Away Team_Jacksonville Jaguars','Home Team_Jacksonville Jaguars','Away Team_Indianapolis Colts','Home Team_Indianapolis Colts','Away Team_Kansas City Chiefs','Home Team_Kansas City Chiefs','Away Team_Los Angeles Chargers','Home Team_Los Angeles Chargers','Away Team_Denver Broncos','Home Team_Denver Broncos','Away Team_Oakland Raiders','Home Team_Oakland Raiders','Away Team_Washington Redskins','Home Team_Washington Redskins','Away Team_Dallas Cowboys','Home Team_Dallas Cowboys','Away Team_Philadelphia Eagles','Home Team_Philadelphia Eagles','Away Team_New York Giants','Home Team_New York Giants','Away Team_Chicago Bears','Home Team_Chicago Bears','Away Team_Green Bay Packers','Home Team_Green Bay Packers','Away Team_Minnesota Vikings','Home Team_Minnesota Vikings','Away Team_Detroit Lions','Home Team_Detroit Lions','Away Team_New Orleans Saints','Home Team_New Orleans Saints','Away Team_Carolina Panthers','Home Team_Carolina Panthers','Away Team_Tampa Bay Buccaneers','Home Team_Tampa Bay Buccaneers','Away Team_Atlanta Falcons','Home Team_Atlanta Falcons','Away Team_Los Angeles Rams','Home Team_Los Angeles Rams','Away Team_Seattle Seahawks','Home Team_Seattle Seahawks','Away Team_Arizona Cardinals','Home Team_Arizona Cardinals','Away Team_San Francisco 49ers','Home Team_San Francisco 49ers']]
#x_data = matchup_data[['W', 'L', 'PCT', 'PF', 'PA', 'DIFF', 'AVG LINE', 'OFF RK (YDS)', 'OFF YDS/G', 'PTS FOR/G', 'DEF RK (YDS)', 'YDS ALWD/G', 'PTS ALWD/G', 'H/A', 'Total Inj', 'Non-IR', 'IR']]
y_data = matchup_data['Winner']

x_train = x_data
y_train = y_data
x_test = week7[['Away Line','Home Line','AwT_W','AwT_L','AwT_T','AwT_Pct','AwT_PF','AwT_PA','AwT_PtDiff','AwT_Strk','AwT_OffRk(yds)','AwT_OffYds/G','AwT_PF/G','AwT_DefRk(yds)','AwT_YdsAlwd/G','AwT_PtsAlwd/G','AwT_TotInj','AwT_NonIR','AwT_IR','HmT_W','HmT_L','HmT_T','HmT_Pct','HmT_PF','HmT_PA','HmT_PtDiff','HmT_Strk','HmT_OffRk(yds)','HmT_OffYds/G','HmT_PF/G','HmT_DefRk(yds)','HmT_YdsAlwd/G','HmT_PtsAlwd/G','HmT_TotInj','HmT_NonIR','HmT_IR','Away Team_New England Patriots','Home Team_New England Patriots','Away Team_Miami Dolphins','Home Team_Miami Dolphins','Away Team_New York Jets','Home Team_New York Jets','Away Team_Buffalo Bills','Home Team_Buffalo Bills','Away Team_Cincinnati Bengals','Home Team_Cincinnati Bengals','Away Team_Baltimore Ravens','Home Team_Baltimore Ravens','Away Team_Pittsburgh Steelers','Home Team_Pittsburgh Steelers','Away Team_Cleveland Browns','Home Team_Cleveland Browns','Away Team_Tennessee Titans','Home Team_Tennessee Titans','Away Team_Houston Texans','Home Team_Houston Texans','Away Team_Jacksonville Jaguars','Home Team_Jacksonville Jaguars','Away Team_Indianapolis Colts','Home Team_Indianapolis Colts','Away Team_Kansas City Chiefs','Home Team_Kansas City Chiefs','Away Team_Los Angeles Chargers','Home Team_Los Angeles Chargers','Away Team_Denver Broncos','Home Team_Denver Broncos','Away Team_Oakland Raiders','Home Team_Oakland Raiders','Away Team_Washington Redskins','Home Team_Washington Redskins','Away Team_Dallas Cowboys','Home Team_Dallas Cowboys','Away Team_Philadelphia Eagles','Home Team_Philadelphia Eagles','Away Team_New York Giants','Home Team_New York Giants','Away Team_Chicago Bears','Home Team_Chicago Bears','Away Team_Green Bay Packers','Home Team_Green Bay Packers','Away Team_Minnesota Vikings','Home Team_Minnesota Vikings','Away Team_Detroit Lions','Home Team_Detroit Lions','Away Team_New Orleans Saints','Home Team_New Orleans Saints','Away Team_Carolina Panthers','Home Team_Carolina Panthers','Away Team_Tampa Bay Buccaneers','Home Team_Tampa Bay Buccaneers','Away Team_Atlanta Falcons','Home Team_Atlanta Falcons','Away Team_Los Angeles Rams','Home Team_Los Angeles Rams','Away Team_Seattle Seahawks','Home Team_Seattle Seahawks','Away Team_Arizona Cardinals','Home Team_Arizona Cardinals','Away Team_San Francisco 49ers','Home Team_San Francisco 49ers']]
y_test = week7['Winner']



#rownum = 0
#game = x_test.iloc[rownum]
#while game.empty == False:
#  game = x_test.iloc[rownum]
#  for item in game:
#    print(item)
#    item = float(item)
#    print(type(item))
#  rownum += 1

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.14)

print()
#print(x_train.to_string())
#print(y_train.to_string())
#print(x_test.to_string())
print(y_test.to_string())

model = LogisticRegression()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
probability = model.predict_proba(x_test)
print()
print('logistic regression:')
print(prediction)
print(probability)
#print(model.prect_proba(x_test))
#print('Log: ',metrics.accuracy_score(y_test, prediction['Logistic']))
#print(model.coef_)

#conf_mat_logist = metrics.confusion_matrix(y_test, prediction['Logistic'])
#print('Logist \r', conf_mat_logist)

svm_model = svm.SVC(kernel='linear', probability=True)
clf = svm_model.fit(x_train,y_train)
svm_pred = clf.predict(x_test)
svm_prob = svm_model.predict_proba(x_test)
print('\n \n')
print('svm:')
print(svm_pred)
print(svm_prob)

#prediction_final = week7[['Away Team','AT','Home Team']]

#rownum = 0
#for predic in prediction:
#  if predic == 1:
#    prediction_final.loc[rownum, 'Logistic Pred'] = 'HmT W'
#    prediction_final.loc[rownum, 'Logistic Prob'] = probability[rownum][1] * 100
#  elif predic == -1:
#    prediction_final.loc[rownum, 'Logistic Pred'] = 'AwT W'
#    prediction_final.loc[rownum, 'Logistic Prob'] = probability[rownum][0] * 100
#  rownum += 1

#rownum = 0
#for pred in svm_pred:
#  if pred == 1:
#    prediction_final.loc[rownum, 'SVM Pred'] = 'HmT W'
#    prediction_final.loc[rownum, 'SVM Prob'] = svm_prob[rownum][1] * 100
#  elif pred == -1:
#    prediction_final.loc[rownum, 'SVM Pred'] = 'AwT W'
#    prediction_final.loc[rownum, 'SVM Prob'] = svm_prob[rownum][1] * 100
#
#  rownum += 1


#print(prediction_final) 
#prediction_final.to_csv('final_predictions_week7.csv') 

print("Accuracy:",metrics.accuracy_score(y_test, svm_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, svm_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, svm_pred))
print('Score:',clf.score(x_data,y_data))
print('Confusion Matrix:\n', metrics.confusion_matrix(y_test, svm_pred))
print(clf.coef_)


