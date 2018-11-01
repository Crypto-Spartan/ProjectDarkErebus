
from mlxtend.plotting import plot_decision_regions

import pandas as pd
import numpy as np
#pd.set_option('max_columns', 50)
#import build_table
import get_winners as winners
pd.set_option('max_columns', 50)
np.set_printoptions(suppress=True)

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.decomposition import PCA as sklearnPCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

#winners.ask_user_for_winners('8')

#import machine_learning

from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import svm

scaler = StandardScaler()

week5 = pd.read_csv('final_matchups_week5.csv', index_col=0)
week6 = pd.read_csv('final_matchups_week6.csv', index_col=0)
week7 = pd.read_csv('final_matchups_week7.csv', index_col=0)
week8 = pd.read_csv('final_matchups_week8.csv', index_col=0)
#print(week8)

matchup_data = pd.concat([week5, week6, week7, week8])
matchup_data = matchup_data.reset_index()
#print(matchup_data)

x_data = matchup_data[['Away Line','Home Line','AwT_W','AwT_L','AwT_T','AwT_Pct','AwT_PF','AwT_PA','AwT_PtDiff','AwT_Strk','AwT_OffRk(yds)','AwT_OffYds/G','AwT_PF/G','AwT_DefRk(yds)','AwT_YdsAlwd/G','AwT_PtsAlwd/G','AwT_TotInj','AwT_NonIR','AwT_IR','HmT_W','HmT_L','HmT_T','HmT_Pct','HmT_PF','HmT_PA','HmT_PtDiff','HmT_Strk','HmT_OffRk(yds)','HmT_OffYds/G','HmT_PF/G','HmT_DefRk(yds)','HmT_YdsAlwd/G','HmT_PtsAlwd/G','HmT_TotInj','HmT_NonIR','HmT_IR','Away Team_New England Patriots','Home Team_New England Patriots','Away Team_Miami Dolphins','Home Team_Miami Dolphins','Away Team_New York Jets','Home Team_New York Jets','Away Team_Buffalo Bills','Home Team_Buffalo Bills','Away Team_Cincinnati Bengals','Home Team_Cincinnati Bengals','Away Team_Baltimore Ravens','Home Team_Baltimore Ravens','Away Team_Pittsburgh Steelers','Home Team_Pittsburgh Steelers','Away Team_Cleveland Browns','Home Team_Cleveland Browns','Away Team_Tennessee Titans','Home Team_Tennessee Titans','Away Team_Houston Texans','Home Team_Houston Texans','Away Team_Jacksonville Jaguars','Home Team_Jacksonville Jaguars','Away Team_Indianapolis Colts','Home Team_Indianapolis Colts','Away Team_Kansas City Chiefs','Home Team_Kansas City Chiefs','Away Team_Los Angeles Chargers','Home Team_Los Angeles Chargers','Away Team_Denver Broncos','Home Team_Denver Broncos','Away Team_Oakland Raiders','Home Team_Oakland Raiders','Away Team_Washington Redskins','Home Team_Washington Redskins','Away Team_Dallas Cowboys','Home Team_Dallas Cowboys','Away Team_Philadelphia Eagles','Home Team_Philadelphia Eagles','Away Team_New York Giants','Home Team_New York Giants','Away Team_Chicago Bears','Home Team_Chicago Bears','Away Team_Green Bay Packers','Home Team_Green Bay Packers','Away Team_Minnesota Vikings','Home Team_Minnesota Vikings','Away Team_Detroit Lions','Home Team_Detroit Lions','Away Team_New Orleans Saints','Home Team_New Orleans Saints','Away Team_Carolina Panthers','Home Team_Carolina Panthers','Away Team_Tampa Bay Buccaneers','Home Team_Tampa Bay Buccaneers','Away Team_Atlanta Falcons','Home Team_Atlanta Falcons','Away Team_Los Angeles Rams','Home Team_Los Angeles Rams','Away Team_Seattle Seahawks','Home Team_Seattle Seahawks','Away Team_Arizona Cardinals','Home Team_Arizona Cardinals','Away Team_San Francisco 49ers','Home Team_San Francisco 49ers']]
y_data = matchup_data['Winner']

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.12)
print(y_test.to_string())

scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#model_nn = MLPClassifier(hidden_layer_sizes=(113,56,28),max_iter=1000)
#model_nn = MLPClassifier(hidden_layer_sizes=(50,25),max_iter=500)
model_nn = MLPClassifier(hidden_layer_sizes=(28,7),max_iter=650)
#model_nn = MLPClassifier(hidden_layer_sizes=(28,28),max_iter=500)
#model_nn = MLPClassifier(hidden_layer_sizes=(57),max_iter=500)
nn_model = model_nn.fit(x_train, y_train)
predict_train_nn = nn_model.predict(x_train)
predict_test_nn = nn_model.predict(x_test)
predict_test_nn_proba = model_nn.predict_proba(x_test)
print('Neural Network:')
print('Predictions:', predict_test_nn)
print(predict_test_nn_proba)
print('Training Accuracy:', metrics.accuracy_score(y_train, predict_train_nn))
print('Validation Accuracy:', metrics.accuracy_score(y_test, predict_test_nn))
print('Classification Report:','\n',metrics.classification_report(y_test, predict_test_nn))
print('\n')


pca = sklearnPCA(n_components=2) #2-dimensional PCA
transformed = pca.fit_transform(x_train)

model_nn.fit(transformed, y_train)
plot_decision_regions(X=transformed, y=y_train.astype(np.integer).values, clf=model_nn, legend=2)

#plt.savefig('data.png')
plt.show()