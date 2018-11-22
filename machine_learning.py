
import pandas as pd
#import build_table
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics 


np.set_printoptions(suppress=True)
pd.set_option('max_columns', 50)


week5 = pd.read_csv('final_matchups_week05.csv', index_col=0)
week6 = pd.read_csv('final_matchups_week06.csv', index_col=0)
week7 = pd.read_csv('final_matchups_week07.csv', index_col=0)
week8 = pd.read_csv('final_matchups_week08.csv', index_col=0)
week9 = pd.read_csv('final_matchups_week09.csv', index_col=0)
week10 = pd.read_csv('final_matchups_week10.csv', index_col=0)
week11 = pd.read_csv('final_matchups_week11.csv', index_col=0)
week12 = pd.read_csv('final_matchups_week12.csv', index_col=0)

matchup_data = pd.concat([week5, week6, week7, week8, week9, week10, week11])
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
x_test = week12[['Away Line','Home Line','AwT_W','AwT_L','AwT_T','AwT_Pct','AwT_PF','AwT_PA','AwT_PtDiff','AwT_Strk','AwT_OffRk(yds)','AwT_OffYds/G','AwT_PF/G','AwT_DefRk(yds)','AwT_YdsAlwd/G','AwT_PtsAlwd/G','AwT_TotInj','AwT_NonIR','AwT_IR','HmT_W','HmT_L','HmT_T','HmT_Pct','HmT_PF','HmT_PA','HmT_PtDiff','HmT_Strk','HmT_OffRk(yds)','HmT_OffYds/G','HmT_PF/G','HmT_DefRk(yds)','HmT_YdsAlwd/G','HmT_PtsAlwd/G','HmT_TotInj','HmT_NonIR','HmT_IR','Away Team_New England Patriots','Home Team_New England Patriots','Away Team_Miami Dolphins','Home Team_Miami Dolphins','Away Team_New York Jets','Home Team_New York Jets','Away Team_Buffalo Bills','Home Team_Buffalo Bills','Away Team_Cincinnati Bengals','Home Team_Cincinnati Bengals','Away Team_Baltimore Ravens','Home Team_Baltimore Ravens','Away Team_Pittsburgh Steelers','Home Team_Pittsburgh Steelers','Away Team_Cleveland Browns','Home Team_Cleveland Browns','Away Team_Tennessee Titans','Home Team_Tennessee Titans','Away Team_Houston Texans','Home Team_Houston Texans','Away Team_Jacksonville Jaguars','Home Team_Jacksonville Jaguars','Away Team_Indianapolis Colts','Home Team_Indianapolis Colts','Away Team_Kansas City Chiefs','Home Team_Kansas City Chiefs','Away Team_Los Angeles Chargers','Home Team_Los Angeles Chargers','Away Team_Denver Broncos','Home Team_Denver Broncos','Away Team_Oakland Raiders','Home Team_Oakland Raiders','Away Team_Washington Redskins','Home Team_Washington Redskins','Away Team_Dallas Cowboys','Home Team_Dallas Cowboys','Away Team_Philadelphia Eagles','Home Team_Philadelphia Eagles','Away Team_New York Giants','Home Team_New York Giants','Away Team_Chicago Bears','Home Team_Chicago Bears','Away Team_Green Bay Packers','Home Team_Green Bay Packers','Away Team_Minnesota Vikings','Home Team_Minnesota Vikings','Away Team_Detroit Lions','Home Team_Detroit Lions','Away Team_New Orleans Saints','Home Team_New Orleans Saints','Away Team_Carolina Panthers','Home Team_Carolina Panthers','Away Team_Tampa Bay Buccaneers','Home Team_Tampa Bay Buccaneers','Away Team_Atlanta Falcons','Home Team_Atlanta Falcons','Away Team_Los Angeles Rams','Home Team_Los Angeles Rams','Away Team_Seattle Seahawks','Home Team_Seattle Seahawks','Away Team_Arizona Cardinals','Home Team_Arizona Cardinals','Away Team_San Francisco 49ers','Home Team_San Francisco 49ers']]
y_test = week12['Winner']



#rownum = 0
#game = x_test.iloc[rownum]
#while game.empty == False:
#  game = x_test.iloc[rownum]
#  for item in game:
#    print(item)
#    item = float(item)
#    print(type(item))
#  rownum += 1

#x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.14)

print()
#print(x_train.to_string())
#print(y_train.to_string())
#print(x_test.to_string())
#print(y_test.to_string())

model = LogisticRegression()
model.fit(x_train, y_train)
prediction_train = model.predict(x_train)
prediction = model.predict(x_test)
probability = model.predict_proba(x_test)
print()
print('logistic regression:')
print(prediction)
print(probability)
print('Training Accuracy:', metrics.accuracy_score(y_train, prediction_train))
#print('Validation Accuracy:', metrics.accuracy_score(y_test, prediction))
#print(model.prect_proba(x_test))
#print('Log: ',metrics.accuracy_score(y_test, prediction['Logistic']))
#print(model.coef_)

#conf_mat_logist = metrics.confusion_matrix(y_test, prediction['Logistic'])
#print('Logist \r', conf_mat_logist)

svm_model = svm.SVC(kernel='linear', probability=True)
clf = svm_model.fit(x_train,y_train)
svm_pred_train = clf.predict(x_train)
svm_pred = clf.predict(x_test)
svm_prob = svm_model.predict_proba(x_test)
print('\n')
print('SVM Linear:')
print(svm_pred)
print(svm_prob)
print('Training Accuracy:', metrics.accuracy_score(y_train, svm_pred_train))
#print('Validation Accuracy:', metrics.accuracy_score(y_test, svm_pred))


#print("Accuracy:",metrics.accuracy_score(y_test, svm_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
#print("Precision:",metrics.precision_score(y_test, svm_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
#print("Recall:",metrics.recall_score(y_test, svm_pred))
#print('Score:',clf.score(x_data,y_data))
#print('Confusion Matrix:\n', metrics.confusion_matrix(y_test, svm_pred))
#print(clf.coef_)
print('\n')

model_rf = RandomForestClassifier()
rf_model = model_rf.fit(x_train, y_train)
predict_train_rf = rf_model.predict(x_train)
predict_test_rf = rf_model.predict(x_test)
predict_test_rf_proba = model_rf.predict_proba(x_test)
print('Random Forest:')
print('Predictions:', predict_test_rf)
print(predict_test_rf_proba)
print('Training Accuracy:', metrics.accuracy_score(y_train, predict_train_rf))
#print('Validation Accuracy:', metrics.accuracy_score(y_test, predict_test_rf))
print('\n')

model_xgb = GradientBoostingClassifier()
xgb_model = model_xgb.fit(x_train, y_train)
predict_train_xgb = xgb_model.predict(x_train)
predict_test_xgb = xgb_model.predict(x_test)
predict_test_xgb_proba = model_xgb.predict_proba(x_test)
print('XGBoost:')
print('Predictions:', predict_test_xgb)
print(predict_test_xgb_proba)
print('Training Accuracy:', metrics.accuracy_score(y_train, predict_train_xgb))
#print('Validation Accuracy:', metrics.accuracy_score(y_test, predict_test_xgb))
print('\n')

model_svm_rbf = svm.SVC(probability=True)
svm_rbf_model = model_svm_rbf.fit(x_train, y_train)
predict_train_svm_rbf = svm_rbf_model.predict(x_train)
predict_test_svm_rbf = svm_rbf_model.predict(x_test)
predict_test_svm_rbf_proba = model_svm_rbf.predict_proba(x_test)
print('SVM RBF:')
print('Predictions:', predict_test_svm_rbf)
print(predict_test_svm_rbf_proba)
print('Training Accuracy:', metrics.accuracy_score(y_train, predict_train_svm_rbf))
#print('Validation Accuracy:', metrics.accuracy_score(y_test, predict_test_svm_rbf))
print('\n')

model_knn = KNeighborsClassifier()
knn_model = model_knn.fit(x_train, y_train)
predict_train_knn = knn_model.predict(x_train)
predict_test_knn = knn_model.predict(x_test)
predict_test_knn_proba = model_knn.predict_proba(x_test)
print('K Nearest Neighbors:')
print('Predictions:', predict_test_knn)
print(predict_test_knn_proba)
print('Training Accuracy:', metrics.accuracy_score(y_train, predict_train_knn))
#print('Validation Accuracy:', metrics.accuracy_score(y_test, predict_test_knn))

model_gnb = GaussianNB()
gnb_model = model_gnb.fit(x_train, y_train)
predict_train_gnb = gnb_model.predict(x_train)
predict_test_gnb = gnb_model.predict(x_test)
predict_test_gnb_proba = model_gnb.predict_proba(x_test)
print('Gaussian Naive Bayes:')
print('Predictions:', predict_test_gnb)
print(predict_test_gnb_proba)
print('Training Accuracy:', metrics.accuracy_score(y_train, predict_train_gnb))
#print('Validation Accuracy:', metrics.accuracy_score(y_test, predict_test_gnb))

prediction_final = week12[['Away Team','AT','Home Team']]

rownum = 0
for predic in prediction:
  if predic == 1:
    prediction_final.loc[rownum, 'Logistic Pred'] = 'Home'
    prediction_final.loc[rownum, 'Logistic Prob'] = probability[rownum][1] * 100
  elif predic == -1:
    prediction_final.loc[rownum, 'Logistic Pred'] = 'Away'
    prediction_final.loc[rownum, 'Logistic Prob'] = probability[rownum][0] * 100
  rownum += 1

rownum = 0
for pred in svm_pred:
  if pred == 1:
    prediction_final.loc[rownum, 'SVM Linear Pred'] = 'Home'
  elif pred == -1:
    prediction_final.loc[rownum, 'SVM Linear Pred'] = 'Away'
    
  if svm_prob[rownum][1] * 100 > 50:
    prediction_final.loc[rownum, 'SVM Linear Prob'] = svm_prob[rownum][1] * 100
  elif svm_prob[rownum][1] * 100 < 50:
    prediction_final.loc[rownum, 'SVM Linear Prob'] = svm_prob[rownum][0] * 100
  elif svm_prob[rownum][1] * 100 == 50:
    prediction_final.loc[rownum, 'SVM Linear Prob'] = 50

  rownum += 1

rownum = 0
for predic in predict_test_rf:
  if predic == 1:
    prediction_final.loc[rownum, 'RF Pred'] = 'Home'
    prediction_final.loc[rownum, 'RF Prob'] = predict_test_rf_proba[rownum][1] * 100
  elif predic == -1:
    prediction_final.loc[rownum, 'RF Pred'] = 'Away'
    prediction_final.loc[rownum, 'RF Prob'] = predict_test_rf_proba[rownum][0] * 100
  rownum += 1

rownum = 0
for predic in predict_test_xgb:
  if predic == 1:
    prediction_final.loc[rownum, 'XGB Pred'] = 'Home'
    prediction_final.loc[rownum, 'XGB Prob'] = predict_test_xgb_proba[rownum][1] * 100
  elif predic == -1:
    prediction_final.loc[rownum, 'XGB Pred'] = 'Away'
    prediction_final.loc[rownum, 'XGB Prob'] = predict_test_xgb_proba[rownum][0] * 100
  rownum += 1

rownum = 0
for pred in predict_test_svm_rbf:
  if pred == 1:
    prediction_final.loc[rownum, 'SVM RBF Pred'] = 'Home'
  elif pred == -1:
    prediction_final.loc[rownum, 'SVM RBF Pred'] = 'Away'
    
  if predict_test_svm_rbf_proba[rownum][1] * 100 > 50:
    prediction_final.loc[rownum, 'SVM RBF Prob'] = predict_test_svm_rbf_proba[rownum][1] * 100
  elif predict_test_svm_rbf_proba[rownum][1] * 100 < 50:
    prediction_final.loc[rownum, 'SVM RBF Prob'] = predict_test_svm_rbf_proba[rownum][0] * 100
  elif predict_test_svm_rbf_proba[rownum][1] * 100 == 50:
    prediction_final.loc[rownum, 'SVM RBF Prob'] = 50

  rownum += 1

rownum = 0
for predic in predict_test_knn:
  if predic == 1:
    prediction_final.loc[rownum, 'KNN Pred'] = 'Home'
    prediction_final.loc[rownum, 'KNN Prob'] = predict_test_knn_proba[rownum][1] * 100
  elif predic == -1:
    prediction_final.loc[rownum, 'KNN Pred'] = 'Away'
    prediction_final.loc[rownum, 'KNN Prob'] = predict_test_knn_proba[rownum][0] * 100
  rownum += 1

rownum = 0
for predic in predict_test_gnb:
  if predic == 1:
    prediction_final.loc[rownum, 'GNB Pred'] = 'Home'
    prediction_final.loc[rownum, 'GNB Prob'] = predict_test_gnb_proba[rownum][1] * 100
  elif predic == -1:
    prediction_final.loc[rownum, 'GNB Pred'] = 'Away'
    prediction_final.loc[rownum, 'GNB Prob'] = predict_test_gnb_proba[rownum][0] * 100
  rownum += 1

print(prediction_final) 
prediction_final.to_csv('final_predictions_week12.csv') 
