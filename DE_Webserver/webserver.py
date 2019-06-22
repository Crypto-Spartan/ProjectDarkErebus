from flask import Flask, render_template, url_for
import pandas as pd

def pred_to_teamname(teams, location):
  teams = game.split(' @ ')

  if location == 'Away':
    winner = teams[0]
  elif location == 'Home':
    winner = teams[1]
  else:
    print('An error occurred')

  if winner == 'New England Patriots':
    winner = 'NE'
  elif winner == 'Miami Dolphins':
    winner = 'MIA'
  elif winner == 'Buffalo Bills':
    winner = 'BUF'
  elif winner == 'New York Jets':
    winner = 'NYJ'
  elif winner == 'Cincinnati Bengals':
    winner = 'CIN'
  elif winner == 'Baltimore Ravens':
    winner = 'BAL'
  elif winner == 'Pittsburgh Steelers':
    winner = 'PIT'
  elif winner == 'Cleveland Browns':
    winner = 'CLE'
  elif winner == 'Tennessee Titans':
    winner = 'TEN'
  elif winner == 'Jacksonville Jaguars':
    winner = 'JAX'
  elif winner == 'Houston Texans':
    winner = 'HOU'
  elif winner == 'Indianapolis Colts':
    winner = 'IND'
  elif winner == 'Kansas City Chiefs':
    winner = 'KC'
  elif winner == 'Los Angeles Chargers':
    winner = 'LAC'
  elif winner == 'Denver Broncos':
    winner = 'DEN'
  elif winner == 'Oakland Raiders':
    winner = 'OAK'
  elif winner == 'Washington Redskins':
    winner = 'WAS'
  elif winner == 'Dallas Cowboys':
    winner = 'DAL'
  elif winner == 'Philadelphia Eagles':
    winner = 'PHI'
  elif winner == 'New York Giants':
    winner = 'NYG'
  elif winner == 'Chicago Bears':
    winner = 'CHI'
  elif winner == 'Green Bay Packers':
    winner = 'GB'
  elif winner == 'Minnesota Vikings':
    winner = 'MIN'
  elif winner == 'Detroit Lions':
    winner = 'DET'
  elif winner == 'New Orleans Saints':
    winner = 'NO'
  elif winner == 'Carolina Panthers':
    winner = 'CAR'
  elif winner == 'Tampa Bay Buccaneers':
    winner = 'TB'
  elif winner == 'Atlanta Falcons':
    winner = 'ATL'
  elif winner == 'Los Angeles Rams':
    winner = 'LAR'
  elif winner == 'Seattle Seahawks':
    winner = 'SEA'
  elif winner == 'Arizona Cardinals':
    winner = 'ARI'
  elif winner == 'San Francisco 49ers':
    winner = 'SF'
  else:
    winner = 'N/A'
  
  return winner

all_predictions = pd.read_csv('final_predictions_week8.csv', index_col=0)

pred_for_chart = []
log_predictions = []
svm_lin_predictions = []
rf_predictions = []
xgb_predictions = []
svm_rbf_predictions = []
knn_predictions = []
gnb_predictions = []

for index, row in all_predictions.iterrows():
  game = str(row['Away Team']+' @ '+row['Home Team'])
  log_pred = row['Logistic Pred']
  log_prob = str(round(row['Logistic Prob'], 2))+'%'
  rf_pred = row['RF Pred']
  rf_prob = str(round(row['RF Prob'], 2))+'%'
  xgb_pred = row['XGB Pred']
  xgb_prob = str(round(row['XGB Prob'], 2))+'%'
  svm_lin_pred = row['SVM Linear Pred']
  svm_lin_prob = str(round(row['SVM Linear Prob'], 2))+'%'
  svm_rbf_pred = row['SVM RBF Pred']
  svm_rbf_prob = str(round(row['SVM RBF Prob'], 2))+'%'
 # knn_pred = row['KNN Pred']
 # knn_prob = str(round(row['KNN Prob'], 2))+'%'
 # gnb_pred = row['GNB Pred']
 # gnb_prob = str(round(row['GNB Prob'], 2))+'%'
 # ann_pred = row['ANN Pred']
 # ann_prob = str(round(row['ANN Prob'], 2))+'%'
  

  log_dict = {'Game':game, 'Prediction':pred_to_teamname(game, log_pred), 'Probability':log_prob}
  log_predictions.append(log_dict)

  rf_dict = {'Game':game, 'Prediction':pred_to_teamname(game, rf_pred), 'Probability':rf_prob}
  rf_predictions.append(rf_dict)

  xgb_dict = {'Game':game, 'Prediction':pred_to_teamname(game, xgb_pred), 'Probability':xgb_prob}
  xgb_predictions.append(xgb_dict)

  svm_lin_dict = {'Game':game, 'Prediction':pred_to_teamname(game, svm_lin_pred), 'Probability':svm_lin_prob}
  svm_lin_predictions.append(svm_lin_dict)

  svm_rbf_dict = {'Game':game, 'Prediction':pred_to_teamname(game, svm_rbf_pred), 'Probability':svm_rbf_prob}
  svm_rbf_predictions.append(svm_rbf_dict)

  pred_for_chart_dict = {'Game':game, 'Log_Pred':pred_to_teamname(game, log_pred), 'Log_Prob':log_prob, 'RF Pred':pred_to_teamname(game, rf_pred), 'RF Prob':rf_prob, 'XGB Pred':pred_to_teamname(game, xgb_pred), 'XGB Prob':xgb_prob, 'SVM Lin Pred':pred_to_teamname(game, svm_lin_pred), 'SVM Lin Prob':svm_lin_prob, 'SVM RBF Pred':pred_to_teamname(game, svm_rbf_pred), 'SVM RBF Prob':svm_rbf_prob}
  pred_for_chart.append(pred_for_chart_dict)

  
print (pred_for_chart)

#start of flask app
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('homepage.html', title='Home')

@app.route('/predictions')
def predictions():
	return render_template('predictions.html', title='Predictions', log_predictions=log_predictions, rf_predictions=rf_predictions, xgb_predictions=xgb_predictions, svm_lin_predictions=svm_lin_predictions, svm_rbf_predictions=svm_rbf_predictions)

@app.route('/predictions-chart')
def predictions_chart():
  return render_template('predictions-chart.html', title='Predictions Chart', pred_for_chart=pred_for_chart)

@app.route('/about')
def about():
  return render_template('about.html', title='About')



app.run('0.0.0.0',8080)
