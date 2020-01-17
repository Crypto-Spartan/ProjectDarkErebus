import pandas as pd
import os
import re
import requests
from operator import itemgetter
from statistics import mode
from bs4 import BeautifulSoup

current_weeknum = '12'
current_year = '2018'




def teamname_to_abbreviation(teamname):
  
  if teamname == 'New England Patriots':
    teamname = 'NE'
  elif teamname == 'Miami Dolphins':
    teamname = 'MIA'
  elif teamname == 'Buffalo Bills':
    teamname = 'BUF'
  elif teamname == 'New York Jets':
    teamname = 'NYJ'
  elif teamname == 'Cincinnati Bengals':
    teamname = 'CIN'
  elif teamname == 'Baltimore Ravens':
    teamname = 'BAL'
  elif teamname == 'Pittsburgh Steelers':
    teamname = 'PIT'
  elif teamname == 'Cleveland Browns':
    teamname = 'CLE'
  elif teamname == 'Tennessee Titans':
    teamname = 'TEN'
  elif teamname == 'Jacksonville Jaguars':
    teamname = 'JAX'
  elif teamname == 'Houston Texans':
    teamname = 'HOU'
  elif teamname == 'Indianapolis Colts':
    teamname = 'IND'
  elif teamname == 'Kansas City Chiefs':
    teamname = 'KC'
  elif teamname == 'Los Angeles Chargers':
    teamname = 'LAC'
  elif teamname == 'Denver Broncos':
    teamname = 'DEN'
  elif teamname == 'Oakland Raiders':
    teamname = 'OAK'
  elif teamname == 'Washington Redskins':
    teamname = 'WAS'
  elif teamname == 'Dallas Cowboys':
    teamname = 'DAL'
  elif teamname == 'Philadelphia Eagles':
    teamname = 'PHI'
  elif teamname == 'New York Giants':
    teamname = 'NYG'
  elif teamname == 'Chicago Bears':
    teamname = 'CHI'
  elif teamname == 'Green Bay Packers':
    teamname = 'GB'
  elif teamname == 'Minnesota Vikings':
    teamname = 'MIN'
  elif teamname == 'Detroit Lions':
    teamname = 'DET'
  elif teamname == 'New Orleans Saints':
    teamname = 'NO'
  elif teamname == 'Carolina Panthers':
    teamname = 'CAR'
  elif teamname == 'Tampa Bay Buccaneers':
    teamname = 'TB'
  elif teamname == 'Atlanta Falcons':
    teamname = 'ATL'
  elif teamname == 'Los Angeles Rams':
    teamname = 'LAR'
  elif teamname == 'Seattle Seahawks':
    teamname = 'SEA'
  elif teamname == 'Arizona Cardinals':
    teamname = 'ARI'
  elif teamname == 'San Francisco 49ers':
    teamname = 'SF'
  else:
    teamname = 'N/A'

  return teamname




def pred_to_abbreviation(teams, location):
  teams = teams.split(' @ ')

  if location == 'Away':
    predicted_winner = teams[0]
  elif location == 'Home':
    predicted_winner = teams[1]
  else:
    print('An error occurred')

  predicted_winner = teamname_to_abbreviation(predicted_winner)
  
  return predicted_winner



def pull_data_for_outcome(weeknum=None, year=None):
  global current_weeknum
  global current_year
  weeknum = weeknum or current_weeknum
  year = year or current_year

  url = f"https://www.pro-football-reference.com/years/{year}/week_{weeknum}.htm"
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  games_tables = soup.findAll('table', class_='teams')

  return games_tables




def check_game_outcome(weeknum=None, year=None):
  global current_weeknum
  global current_year
  weeknum = weeknum or current_weeknum
  year = year or current_year
  
  loser_list = []
  winner_list = []

  url = f"https://www.pro-football-reference.com/years/{year}/week_{weeknum}.htm"
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  games_tables = soup.findAll('table', class_='teams')

  try:
    for table in games_tables:
      real_winner = table.find('tr', class_='winner').td.string
      real_loser = table.find('tr', class_='loser').td.string

      real_winner = teamname_to_abbreviation(real_winner)
      real_loser = teamname_to_abbreviation(real_loser)

      winner_list.append(real_winner)
      loser_list.append(real_loser)      
  except:
    pass

  winners_losers_dict = {'Winners':winner_list, 'Losers':loser_list}

  return winners_losers_dict
  



def check_archive_folder():
  archive_list = []

  for (root,dirs,files) in os.walk('archive', topdown=True):
    root = root.split('/')

    if len(root) > 1:
      year = root[1]
    else:
      continue

    if len(files) > 0:
      renamed_files = []
      
      for i in files:
        file_dict = {}
        year_dict = {}
        regex = re.compile('week[0-9]{1,2}')
        weekname = regex.findall(i)

        if len(weekname) > 0:
          weekname = weekname[0]
          num = re.compile('[0-9]{1,2}').findall(weekname)[0]
          weekname = 'Week ' + num
          file_dict['week'] = weekname
          file_dict['num'] = num
          renamed_files.append(file_dict)
        else: 
          continue
            
      year_dict['year'] = year 
      renamed_files = sorted(renamed_files, key=lambda x: (int(x['num'])), reverse=True)
      year_dict['files'] = renamed_files
      archive_list.append(year_dict)
    else:
      continue

  archive_list.sort(key=itemgetter('year'), reverse=True)
  return(archive_list)




def create_pred_tables(weeknum=None, year=None):
  global current_weeknum
  global current_year
  weeknum = weeknum or current_weeknum
  year = year or current_year
  filename = f'archive/{year}/final_predictions_week{weeknum}.csv'
  all_predictions = pd.read_csv(filename, index_col=0)
  
  log_predictions = []
  svm_lin_predictions = []
  rf_predictions = []
  xgb_predictions = []
  svm_rbf_predictions = []
  knn_predictions = []
  gnb_predictions = []

  for index, row in all_predictions.iterrows():
    game = str(row['Away Team']+' @ '+row['Home Team'])    
    
    # ann_pred = row['ANN Pred']
    # ann_prob = str(round(row['ANN Prob'], 2))+'%'
    
    try:
      log_pred = row['Logistic Pred']
      log_prob = str(round(row['Logistic Prob'], 2))+'%'
      log_dict = {'Game':game, 'Prediction':pred_to_abbreviation(game, log_pred), 'Probability':log_prob}
      log_predictions.append(log_dict)
    except:
      pass

    try:
      rf_pred = row['RF Pred']
      rf_prob = str(round(row['RF Prob'], 2))+'%'
      rf_dict = {'Game':game, 'Prediction':pred_to_abbreviation(game, rf_pred), 'Probability':rf_prob}
      rf_predictions.append(rf_dict)
    except:
      pass

    try:
      xgb_pred = row['XGB Pred']
      xgb_prob = str(round(row['XGB Prob'], 2))+'%'
      xgb_dict = {'Game':game, 'Prediction':pred_to_abbreviation(game, xgb_pred), 'Probability':xgb_prob}
      xgb_predictions.append(xgb_dict)
    except:
      pass

    try:
      svm_lin_pred = row['SVM Linear Pred']
      svm_lin_prob = str(round(row['SVM Linear Prob'], 2))+'%'
      svm_lin_dict = {'Game':game, 'Prediction':pred_to_abbreviation(game, svm_lin_pred), 'Probability':svm_lin_prob}
      svm_lin_predictions.append(svm_lin_dict)
    except:
      pass

    try:
      svm_rbf_pred = row['SVM RBF Pred']
      svm_rbf_prob = str(round(row['SVM RBF Prob'], 2))+'%'
      svm_rbf_dict = {'Game':game, 'Prediction':pred_to_abbreviation(game, svm_rbf_pred), 'Probability':svm_rbf_prob}
      svm_rbf_predictions.append(svm_rbf_dict)
    except:
      pass

    try:
      knn_pred = row['KNN Pred']
      knn_prob = str(round(row['KNN Prob'], 2))+'%'
      knn_dict = {'Game':game, 'Prediction':pred_to_abbreviation(game, knn_pred), 'Probability':knn_prob}
      knn_predictions.append(knn_dict)
    except:
      pass

    try:
      gnb_pred = row['GNB Pred']
      gnb_prob = str(round(row['GNB Prob'], 2))+'%'
      gnb_dict = {'Game':game, 'Prediction':pred_to_abbreviation(game, gnb_pred), 'Probability':gnb_prob}
      gnb_predictions.append(gnb_dict)
    except:
      pass 

  full_prediction_list = [{'Name':'Logistic Regression Predictions', 'Algorithm':log_predictions}, {'Name':'Random Forrest Predictions', 'Algorithm':rf_predictions}, {'Name':'XGBoost Predictions', 'Algorithm':xgb_predictions}, {'Name':'Linear SVM Predictions', 'Algorithm':svm_lin_predictions}, {'Name':'RBF SVM Predictions', 'Algorithm':svm_rbf_predictions}, {'Name':'K Nearest Neighbor Predictions', 'Algorithm':knn_predictions}, {'Name':'Gaussian Naive Bayes Predictions', 'Algorithm':gnb_predictions}]

  result_prediction_list = []

  for i in full_prediction_list:
    if len(i['Algorithm']) != 0:
      result_prediction_list.append(i)


  return result_prediction_list




def create_full_chart(weeknum=None, year=None):
  global current_weeknum
  global current_year
  weeknum = weeknum or current_weeknum
  year = year or current_year
  filename = f'archive/{year}/final_predictions_week{weeknum}.csv'
  pred_for_chart = []

  try:
    all_predictions = pd.read_csv(filename, index_col=0)
  except:
    full_pred_for_chart_dict = {'Game':'No Data', 'Majority':'N/A'}
    pred_for_chart.append(full_pred_for_chart_dict)
    return pred_for_chart


  for index, row in all_predictions.iterrows():
    game = str(row['Away Team']+' @ '+row['Home Team'])
    full_pred_for_chart_dict = {'Game':game}
    majority_list = []
    
    try:
      log_pred = row['Logistic Pred']
      log_prob = str(round(row['Logistic Prob'], 2))+'%'
      full_pred_for_chart_dict['Log_Pred'] = pred_to_abbreviation(game, log_pred)
      full_pred_for_chart_dict['Log_Prob'] = log_prob
      majority_list.append(full_pred_for_chart_dict['Log_Pred'])
    except:
      pass

    try:
      rf_pred = row['RF Pred']
      rf_prob = str(round(row['RF Prob'], 2))+'%'
      full_pred_for_chart_dict['RF_Pred'] = pred_to_abbreviation(game, rf_pred)
      full_pred_for_chart_dict['RF_Prob'] = rf_prob
      majority_list.append(full_pred_for_chart_dict['RF_Pred'])
    except:
      pass

    try:
      xgb_pred = row['XGB Pred']
      xgb_prob = str(round(row['XGB Prob'], 2))+'%'
      full_pred_for_chart_dict['XGB_Pred'] = pred_to_abbreviation(game, xgb_pred)
      full_pred_for_chart_dict['XGB_Prob'] = xgb_prob
      majority_list.append(full_pred_for_chart_dict['XGB_Pred'])
    except:
      pass

    try:  
      svm_lin_pred = row['SVM Linear Pred']
      svm_lin_prob = str(round(row['SVM Linear Prob'], 2))+'%'
      full_pred_for_chart_dict['SVM_Lin_Pred'] = pred_to_abbreviation(game, svm_lin_pred)
      full_pred_for_chart_dict['SVM_Lin_Prob'] = svm_lin_prob
      majority_list.append(full_pred_for_chart_dict['SVM_Lin_Pred'])
    except:
      pass

    try:
      svm_rbf_pred = row['SVM RBF Pred']
      svm_rbf_prob = str(round(row['SVM RBF Prob'], 2))+'%'
      full_pred_for_chart_dict['SVM_RBF_Pred'] = pred_to_abbreviation(game, svm_rbf_pred)
      full_pred_for_chart_dict['SVM_RBF_Prob'] = svm_rbf_prob
      majority_list.append(full_pred_for_chart_dict['SVM_RBF_Pred'])
    except:
      pass

    try:
      knn_pred = row['KNN Pred']
      knn_prob = str(round(row['KNN Prob'], 2))+'%'
      full_pred_for_chart_dict['KNN_Pred'] = pred_to_abbreviation(game, knn_pred)
      full_pred_for_chart_dict['KNN_Prob'] = knn_prob
      majority_list.append(full_pred_for_chart_dict['KNN_Pred'])
    except:
      pass
    
    try:
      gnb_pred = row['GNB Pred']
      gnb_prob = str(round(row['GNB Prob'], 2))+'%'
      full_pred_for_chart_dict['GNB_Pred'] = pred_to_abbreviation(game, gnb_pred)
      full_pred_for_chart_dict['GNB_Prob'] = gnb_prob
      majority_list.append(full_pred_for_chart_dict['GNB_Pred'])
    except:
      pass

    
    # ann_pred = row['ANN Pred']
    # ann_prob = str(round(row['ANN Prob'], 2))+'%'  

    try:  
      majority = mode(majority_list)
    except:
      majority = 'N/A'
    
    full_pred_for_chart_dict['Majority'] = majority
    
    pred_for_chart.append(full_pred_for_chart_dict)
  
  return pred_for_chart
