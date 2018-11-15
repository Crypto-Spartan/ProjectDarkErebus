#getting data from the internet

import sys
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
pd.set_option('max_columns', 50)

def get_all(weeknum):
  print('getting stats')
  print('pulling ESPN lines')
  get_espn_lines(weeknum)
  print('pulling ESPN team stats')
  get_espn_stats(weeknum)
  print('pulling ESPN team standings')
  get_espn_standings(weeknum)
  print('pulling NFL injury data')
  get_injuries_stats(weeknum)
  print('finished pulling data')

#get the NFL lines from espn (point favorites)
def get_espn_lines(weeknum):
  url = "http://www.espn.com/nfl/lines"
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  lines_table = soup.find('table', class_='tablehead')

  # take the data from the html table, add it to the python list
  list_of_rows = []
  labels_of_frame = ['Name of Game','Betting Source', 'Team Line', 'Raw Line']
  list_of_rows.append(labels_of_frame)

  for row in lines_table.findAll('tr'):
    # list of attributes for one row/game
    list_of_cells = []
    for cell in row.findAll(["th","td"]):
      # individual stats/cells
      text = cell.text
      # trying to fix formatting for later
      #if text == 'POINT SPREAD' or text == 'TOTAL' or text == 'MONEY LINE' or text == 'N/A':
      #list_of_cells.append(text)   
      list_of_cells.append(text)
  
    # remove the '\xa0' that was being produced in the list
    #list_of_cells = [el.replace('\xa0','BETTING SOURCE') for el in list_of_cells]
    # remove the 'PickCenter  » ' at the end of each game
    #list_of_cells = [el.replace('PickCenter  » ','-------------------------------------------------') for el in list_of_cells]
  
    # take out unneeded data
    if list_of_cells[0] == 'Westgate' or list_of_cells[0] == 'Caesar\'s' or list_of_cells[0] == 'William Hill' or list_of_cells[0] == 'Wynn' or list_of_cells[0] == 'Unibet':
      list_of_cells = list_of_cells[0:4]
      list_of_cells = [list_of_cells[-1]] + list_of_cells[:-1]
      list_of_cells[0] = '' 
    elif len(list_of_cells[0]) < 25:
      continue 
    # add in name of each game, as well as labels for data
    elif len(list_of_cells) == 1:
      game_name = [list_of_cells[0],'','','']
      list_of_rows.append(game_name)
      continue

    # append row/game attributes to main list
    list_of_rows.append(list_of_cells)
    #print(list_of_cells)
    

  # printing if needed
  #for item in list_of_rows:
    #print(' '.join(item)) #print it pretty
    #print(item) #print it less pretty

  df_raw_lines = pd.DataFrame(list_of_rows) 
  df_raw_lines = df_raw_lines[1:] #take the data less the header row
  df_raw_lines.columns = ['Name of Game', 'Betting Source', 'Team Line', 'Raw Line']
  #print(df_raw_lines)

  # assign variables to count row numbers
  row_start = 1
  row_end = 6
  row_count_line = 1
  # find the line data from the dataframe
  game = df_raw_lines.loc[row_start:row_end]
  # dictionary to add team and line info to
  team_lines = {}

  # loop to go through every game
  while game.empty == False:
    # set the variables
    team1_avg_line = 0
    team2_avg_line = 0
    count = 0
    #print(game)

    # for each line per game
    for numset in game.loc[:, 'Raw Line']:
    
      # first line is 'NaN', so only do if a string
      if numset != '':
        if len(numset) == 4:
          count += 1
          team1_line = float(numset[:2])
          team2_line = float(numset[2:])
          #print(str(team1_line)+' team1 line')
          #print(str(team2_line)+' team2 line')
          #print('')
          team1_avg_line += team1_line
          team2_avg_line += team2_line
      
        elif len(numset) == 8:
          count += 1
          team1_line = float(numset[:4])
          team2_line = float(numset[4:])
          #print(str(team1_line)+' team1 line')
          #print(str(team2_line)+' team2 line')
          #print('')
          team1_avg_line += team1_line
          team2_avg_line += team2_line
      
        elif len(numset) == 6:
          count += 1
          team1_line = float(numset[:3])
          team2_line = float(numset[3:])
          #print(str(team1_line)+' team1 line')
          #print(str(team2_line)+' team2 line')
          #print('')
          team1_avg_line += team1_line
          team2_avg_line += team2_line

        elif len(numset) == 10:
          count += 1
          team1_line = float(numset[:5])
          team2_line = float(numset[5:])
          #print(str(team1_line)+' team1 line')
          #print(str(team2_line)+' team2 line')
          #print('')
          team1_avg_line += team1_line
          team2_avg_line += team2_line

        elif numset == 'N/A':
          pass

        elif numset == 'EVEN':
          print(game)
          print(numset)
          count += 1

        else:
          if df_raw_lines.loc[row_count_line, 'Team Line'] == 'EVEN':
            count += 1
            pass
          else:
            print(row_count_line)
            print (df_raw_lines.loc[row_count_line, 'Team Line'])
            print (numset)
            print(game.to_string())
            sys.exit('ERROR: UNKNOWN AVG LINE LENGTH')
      
      row_count_line += 1    
  
    #print (game.loc[:, 'Raw Line'])
  
    if count != 0:
      team1_avg_line = team1_avg_line / count
      team2_avg_line = team2_avg_line / count
    elif count == 0:
      team1_avg_line = 'N/A'
      team2_avg_line = 'N/A'
    #print(str(team1_avg_line)+' team1 avg')
    #print(str(team2_avg_line)+' team2 avg')
  
    # find each teamname
    for gamename in game.loc[:, 'Name of Game']:    
      if gamename != '':
        teams = (gamename.split(' - '))[0]
        teams = teams.split(' at ')
        team1 = str(teams[0])
        team2 = str(teams[1])
        if team1 == 'Bears':
          team1 = 'Chicago'
        elif team2 == 'Bears':
          team2 = 'Chicago'
        #print(team2)

    # add teamname and their associated line to the dictionary
    team_lines[team1] = team1_avg_line
    team_lines[team2] = team2_avg_line

    # go to next game for each loop
    row_start += 6
    row_end += 6
    # restate game variable for looping
    game = df_raw_lines.loc[row_start:row_end]

  #print(team_lines)

  # create dataframe and put data into csv
  df_format_lines = pd.DataFrame.from_dict(team_lines, orient='index', columns=['Avg Line'])
  #print(df_format_lines)
  df_format_lines.to_csv('nfl_lines_week'+weeknum+'.csv')
  return df_format_lines

#get offense and defense statistics from espn
#does not have a return, just puts data into csv's
def get_espn_stats(weeknum):
  # get the stats for offense of each team
  url_off = "http://www.espn.com/nfl/statistics/team/_/stat/total"
  req_off = requests.get(url_off)
  soup_off = BeautifulSoup(req_off.content, 'html.parser')
  stats_table_off = soup_off.find('table', class_='tablehead')

  # take the data from the html table, add it to the python list
  list_of_rows = []
  for row in stats_table_off.findAll('tr'):
      #list of attributes for one row/team
      list_of_cells = []
      for cell in row.findAll(["th","td"]):
        #individual stats/cells
        text = cell.text
        list_of_cells.append(text)
      #append row/team attributes to main list
      list_of_rows.append(list_of_cells)

  # printing if needed
  #for item in list_of_rows:
    #print(' '.join(item)) #print it pretty
    #print(item) #print it less pretty
  
  off_headers = list_of_rows[0]
  df_offense_stats = pd.DataFrame(list_of_rows, columns=off_headers)
  df_offense_stats = df_offense_stats.drop(0)
  
  iterrow_count = 1
  for index, row in df_offense_stats.iterrows():
    test_empty_string = str(row['RK']).replace(u'\xa0', u' ')
    if test_empty_string == ' ' and iterrow_count > 1:
      df_offense_stats.loc[iterrow_count, 'RK'] = iterrow_count-1
    iterrow_count += 1

  df_offense_stats = df_offense_stats.set_index('RK')
  df_offense_stats.to_csv('nfl_stats_off_week'+weeknum+'.csv')


  # get the stats for defense of each team
  url_def = "http://www.espn.com/nfl/statistics/team/_/stat/total/position/defense"
  req_def = requests.get(url_def)
  soup_def = BeautifulSoup(req_def.content, 'html.parser')
  stats_table_def = soup_def.find('table', class_='tablehead')

  # take the data from the html table, add it to the python list
  list_of_rows = []
  for row in stats_table_def.findAll('tr'):
    #list of attributes for one row/team
    list_of_cells = []
    for cell in row.findAll(["th","td"]):
      #individual stats/cells
      text = cell.text
      list_of_cells.append(text)
    #append row/team attributes to main list
    list_of_rows.append(list_of_cells)

  # printing if needed
  #for item in list_of_rows:
    #print(' '.join(item)) #print it pretty
    #print(item) #print it less pretty

  def_headers = list_of_rows[0]
  df_defense_stats = pd.DataFrame(list_of_rows, columns=off_headers)
  df_defense_stats = df_defense_stats.drop(0)
  
  iterrow_count = 1
  for index, row in df_defense_stats.iterrows():
    test_empty_string = str(row['RK']).replace(u'\xa0', u' ')
    if test_empty_string == ' ' and iterrow_count > 1:
      df_defense_stats.loc[iterrow_count, 'RK'] = iterrow_count-1
    iterrow_count += 1
  
  df_defense_stats = df_defense_stats.set_index('RK')
  df_defense_stats.to_csv('nfl_stats_def_week'+weeknum+'.csv')

#get the current records/standings from espn
def get_espn_standings(weeknum):

  url = "http://www.espn.com/nfl/standings"
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')

  team_table = soup.find_all('table', class_='Table2__right-aligned Table2__table-fixed Table2__Table--fixed--left Table2__table')
  stats_table = soup.find_all('table', class_='Table2__table-scroller Table2__right-aligned Table2__table')

  def get_afc_stats(soup, team_table, stats_table):
    stats_table_afc_teams = team_table[0]
    stats_table_afc_stats = stats_table[0]

    list_of_afc_teams = []
    for row in stats_table_afc_teams.findAll('tr'):
      #list of attributes for one row/team
      list_of_cells = []
      for cell in row.findAll(["th","td"]):
        #individual stats/cells
        text = cell.text
        if text == 'AFC East' or text == 'AFC North' or text == 'AFC South' or text == 'AFC West':
          continue
        else:
          if text[:4].isupper() == True:
            text = text[3:]
          elif text[:3].isupper() == True:
            text = text[2:]
          else:
            print('BROKEN')
          list_of_cells.append(text)
        #append row/team attributes to main list
        list_of_afc_teams.append(list_of_cells)

    #print(list_of_rows)

    #for item in list_of_afc_teams:
      #print(' '.join(item)) #print it pretty
      #print(item) #print it less pretty

    count = 0
    list_of_afc_stats = []
    for row in stats_table_afc_stats.findAll('tr'):
      #list of attributes for one row/team
      list_of_cells = []
      for cell in row.findAll(["th","td"]):
        #individual stats/cells
        text = cell.text
        list_of_cells.append(text)
      #append row/team attributes to main list
      if count > 1 and list_of_cells[0] == 'W':
        continue
      else:
        list_of_afc_stats.append(list_of_cells)
      count += 1

    #for item in list_of_afc_stats:
      #print(' '.join(item)) #print it pretty
      #print(item) #print it less pretty

    afc_teams = pd.DataFrame(list_of_afc_teams)
    afc_stats = pd.DataFrame(list_of_afc_stats[1:], columns=['W','L','T','PCT','HOME','AWAY','DIV','CONF','PF','PA','DIFF','STRK'])
    #print(afc_teams)
    #print(afc_stats.to_string())

    afc = pd.concat([afc_teams, afc_stats], axis=1)
    afc = afc.rename(columns={0:'Teamname'})
    #print(afc.to_string())
    return afc

  def get_nfc_stats(soup, team_table, stats_table):
    stats_table_nfc_teams = team_table[1]
    stats_table_nfc_stats = stats_table[1]

    list_of_nfc_teams = []
    for row in stats_table_nfc_teams.findAll('tr'):
      #list of attributes for one row/team
      list_of_cells = []
      for cell in row.findAll(["th","td"]):
        #individual stats/cells
        text = cell.text
        if text == 'NFC East' or text == 'NFC North' or text == 'NFC South' or text == 'NFC West':
          continue
        else:
          if text[:4].isupper() == True:
            text = text[3:]
          elif text[:3].isupper() == True:
            text = text[2:]
          else:
            print('BROKEN')
          list_of_cells.append(text)
        #append row/team attributes to main list
        list_of_nfc_teams.append(list_of_cells)

    #print(list_of_rows)

    #for item in list_of_nfc_teams:
      #print(' '.join(item)) #print it pretty
      #print(item) #print it less pretty

    count = 0
    list_of_nfc_stats = []
    for row in stats_table_nfc_stats.findAll('tr'):
      #list of attributes for one row/team
      list_of_cells = []
      for cell in row.findAll(["th","td"]):
        #individual stats/cells
        text = cell.text
        list_of_cells.append(text)
      #append row/team attributes to main list
      if count > 1 and list_of_cells[0] == 'W':
        continue
      else:
        list_of_nfc_stats.append(list_of_cells)
      count += 1

    #for item in list_of_nfc_stats:
      #print(' '.join(item)) #print it pretty
      #print(item) #print it less pretty

    nfc_teams = pd.DataFrame(list_of_nfc_teams)
    nfc_stats = pd.DataFrame(list_of_nfc_stats[1:], columns=['W','L','T','PCT','HOME','AWAY','DIV','CONF','PF','PA','DIFF','STRK'])
    #print(nfc_teams)
    #print(nfc_stats.to_string())

    nfc = pd.concat([nfc_teams, nfc_stats], axis=1)
    nfc = nfc.rename(columns={0:'Teamname'})
    #print(nfc.to_string())
    return nfc

  afc_teams = get_afc_stats(soup, team_table, stats_table)
  nfc_teams = get_nfc_stats(soup, team_table, stats_table)
  all_teams = afc_teams.append(nfc_teams)
  all_teams = all_teams.reset_index(drop=True)

  all_teams.to_csv('standings_week'+weeknum+'.csv')
  return all_teams

#get the current injury statistics from pro-football-reference.com
def get_injuries_stats(weeknum):
  url = "https://www.pro-football-reference.com/players/injuries.htm"
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')
  injuries_table = soup.find('table')

  # take the data from the html table, add it to the python list
  list_of_rows = []
  for row in injuries_table.findAll('tr'):
      #list of attributes for one row/team
      list_of_cells = []
      for cell in row.findAll(["th","td"]):
        #individual stats/cells
        text = cell.text
        list_of_cells.append(text)
      #append row/team attributes to main list
      list_of_rows.append(list_of_cells)

  # printing if needed
  #for item in list_of_rows:
      #print(' '.join(item)) #print it pretty
      #print(item) #print it less pretty

  # write data to a csv file
  with open('nfl_injuries_raw_week'+weeknum+'.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(list_of_rows)

  # read data from .csv file, put it in a dataframe
  df_all_injured = pd.read_csv('nfl_injuries_raw_week'+weeknum+'.csv')

  # find only the ir players
  df_ir_players = df_all_injured[df_all_injured['Class'] == 'I-R']

  # find players not on the ir
  df_non_ir_injured = df_all_injured[df_all_injured['Class'] != 'I-R']

  # count the number of injuries per team with .value_counts, put counts in a dataframe 
  df_count_all = df_all_injured['Tm'].value_counts().rename_axis('Tm').reset_index(name='Total Injured')
  df_count_non_ir = df_non_ir_injured['Tm'].value_counts().rename_axis('Tm').reset_index(name='Non-IR')
  df_count_ir = df_ir_players['Tm'].value_counts().rename_axis('Tm').reset_index(name='IR')

  # merge all of the dataframes
  df_partial_combined = pd.merge(left=df_count_all,right=df_count_non_ir, on=['Tm'], how='outer')
  df_combined = pd.merge(left=df_partial_combined,right=df_count_ir, on=['Tm'], how='outer')
  df_combined = df_combined.rename(index=str, columns={"Tm": "Team"})

  rownum = 0
  team = df_combined.iloc[rownum]


  while team.empty == False:
      
    try:
      team = df_combined.iloc[rownum,:]
      teamname = team.get('Team')
    except IndexError:
      break
      
    #print(teamname)  
    
    if teamname == 'NWE':
      df_combined.iloc[rownum, 0] = 'New England'
    elif teamname == 'MIA':
      df_combined.iloc[rownum, 0] = 'Miami'
    elif teamname == 'BUF':
      df_combined.iloc[rownum, 0] = 'Buffalo'
    elif teamname == 'NYJ':
      df_combined.iloc[rownum, 0] = 'NY Jets'
    elif teamname == 'CIN':
      df_combined.iloc[rownum, 0] = 'Cincinnati'
    elif teamname == 'BAL':
      df_combined.iloc[rownum, 0] = 'Baltimore'
    elif teamname == 'PIT':
      df_combined.iloc[rownum, 0] = 'Pittsburgh'
    elif teamname == 'CLE':
      df_combined.iloc[rownum, 0] = 'Cleveland' 
    elif teamname == 'TEN':
      df_combined.iloc[rownum, 0] = 'Tennessee'
    elif teamname == 'JAX':
      df_combined.iloc[rownum, 0] = 'Jacksonville'
    elif teamname == 'HOU':
      df_combined.iloc[rownum, 0] = 'Houston'
    elif teamname == 'IND':
      df_combined.iloc[rownum, 0] = 'Indianapolis'
    elif teamname == 'KAN':
      df_combined.iloc[rownum, 0] = 'Kansas City'
    elif teamname == 'LAC':
      df_combined.iloc[rownum, 0] = 'LA Chargers'
    elif teamname == 'DEN':
      df_combined.iloc[rownum, 0] = 'Denver'
    elif teamname == 'OAK':
      df_combined.iloc[rownum, 0] = 'Oakland'
    elif teamname == 'WAS':
      df_combined.iloc[rownum, 0] = 'Washington'
    elif teamname == 'DAL':
      df_combined.iloc[rownum, 0] = 'Dallas'
    elif teamname == 'PHI':
      df_combined.iloc[rownum, 0] = 'Philadelphia'
    elif teamname == 'NYG':
      df_combined.iloc[rownum, 0] = 'NY Giants'
    elif teamname == 'CHI':
      df_combined.iloc[rownum, 0] = 'Chicago'
    elif teamname == 'GNB':
      df_combined.iloc[rownum, 0] = 'Green Bay'
    elif teamname == 'MIN':
      df_combined.iloc[rownum, 0] = 'Minnesota'
    elif teamname == 'DET':
      df_combined.iloc[rownum, 0] = 'Detroit'
    elif teamname == 'NOR':
      df_combined.iloc[rownum, 0] = 'New Orleans'
    elif teamname == 'CAR':
      df_combined.iloc[rownum, 0] = 'Carolina'
    elif teamname == 'TAM':
      df_combined.iloc[rownum, 0] = 'Tampa Bay'
    elif teamname == 'ATL':
      df_combined.iloc[rownum, 0] = 'Atlanta'
    elif teamname == 'LAR':
      df_combined.iloc[rownum, 0] = 'LA Rams'
    elif teamname == 'SEA':
      df_combined.iloc[rownum, 0] = 'Seattle'
    elif teamname == 'ARI':
      df_combined.iloc[rownum, 0] = 'Arizona'
    elif teamname == 'SFO':
      df_combined.iloc[rownum, 0] = 'San Francisco'

    rownum += 1


  #print(df_combined.to_string())

  # output to .csv
  df_combined.to_csv('injuries_stats_week'+weeknum+'.csv')
  return df_combined
