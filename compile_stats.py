# compile team rankings and add to compiled_stats.csv

import csv
import pandas as pd


# build entire pandas table
def build_table():
  print('building table')
  print('compiling stats')
  #creating compiled_stats object
  compiled_stats = compile_w_standings(compile_off_def_inj())
  print('fixing team names')
  rename_games(compiled_stats)
  print('finding opponents, finishing table')
  get_opponent(compiled_stats)
  print()
  print('table build complete')
  print('full data available in "compiled_stats_week<#>.csv"')


# put together offensive stats, defensive stats, and injury stats
def compile_off_def_inj():
  rownum = 0
  lines = pd.read_csv('nfl_lines.csv')
  lines.rename(columns={'Unnamed: 0':'Team Name'}, inplace=True)
  team = lines.iloc[rownum]
  df_off_stats = pd.read_csv('nfl_stats_off.csv')
  df_def_stats = pd.read_csv('nfl_stats_def.csv')
  df_injury_stats = pd.read_csv('injuries_stats.csv')

  try:
    while team.empty == False:
      #team = team.to_frame()
      #print(team.get('Team Name'))
      try:
        team = lines.iloc[rownum,:]
        teamname_line = team.get('Team Name')
      except IndexError:
        break

      for index, row in df_off_stats.iterrows():
        #print (row['RK'], row['TEAM'], row['YDS/G'], row['PTS/G'])
      
        teamrk_offyds = str(row['RK'])
        teamname_off = str(row['TEAM'])
        teamoffydsg = str(row['YDS/G'])
        teamoffptsg = str(row['PTS/G'])

        #print(teamname + ' teamname')
        #print(team + ' team')
      
        if teamname_off == str(teamname_line):
          lines.loc[rownum, 'OFF RK (YDS)'] = teamrk_offyds
          lines.loc[rownum, 'OFF YDS/G'] = teamoffydsg
          lines.loc[rownum, 'POINTS FOR'] = teamoffptsg
          #print('IT WORKED')
        else:
          pass
          #print(teamname + ' teamname')
          #print(team + ' team')

      for index, row in df_def_stats.iterrows():
        #print (row['RK'], row['TEAM'], row['YDS/G'], row['PTS/G']
        teamname_def = str(row['TEAM'])

        if teamname_def == str(teamname_line):
          lines.loc[rownum, 'DEF RK (YDS)'] = str(row['RK'])
          lines.loc[rownum, 'DEF YDS/G'] = str(row['YDS/G'])
          lines.loc[rownum, 'POINTS ALWD'] = str(row['PTS/G'])

      if rownum % 2 == 1:
        lines.loc[rownum, 'H/A'] = 'Home'
      elif rownum % 2 == 0:
        lines.loc[rownum, 'H/A'] = 'Away'
    
      for index, row in df_injury_stats.iterrows():
        teamname_inj = str(row['Team'])

        if teamname_inj == str(teamname_line):
          lines.loc[rownum, 'Total Injured'] = str(row['Total Injured'])
          lines.loc[rownum, 'Non-IR'] = str(row['Non-IR'])
          lines.loc[rownum, 'IR'] = str(row['IR'])

      rownum += 1

  except AttributeError as Error:
    print('I BROKE')
    print(Error)  

  #print(lines.to_string())
  #lines.to_csv('compiled_stats.csv')

  games_tn = lines['Team Name']
  games_al = lines['Avg Line']
  games_ha = lines['H/A']
  games = pd.concat([games_tn, games_al, games_ha], axis=1, join_axes=[games_tn.index])
  #print(games.to_string())
  games.to_csv('games.csv')
  return lines


# put everything together with the standings
def compile_w_standings(team_stats):
  rownum = 0
  standings = pd.read_csv('standings.csv', index_col=0)
  team = standings.iloc[rownum]

  while team.empty == False: #and rownum < 1:
  
    try:
      team = standings.iloc[rownum,:]
      teamname_standings = team.get('Teamname')
    except IndexError:
      break

    for index, row in team_stats.iterrows():
    
      teamname = str(row['Team Name'])
      avg_line = str(row['Avg Line'])
      off_rk = str(row['OFF RK (YDS)'])
      off_yds = str(row['OFF YDS/G'])
      pf = str(row['POINTS FOR'])
      def_rk = str(row['DEF RK (YDS)'])
      def_yds = str(row['DEF YDS/G'])
      pa = str(row['POINTS ALWD'])
      h_a = str(row['H/A'])
      inj = str(row['Total Injured'])
      non_ir = str(row['Non-IR'])
      ir = str(row['IR'])

      if 'NY' in teamname or 'LA' in teamname:
        teamname = teamname.split()
        teamname = teamname[1]

      if teamname in teamname_standings:
        #print(teamname)
        #print(teamname_standings,' ***')
        standings.loc[rownum, 'AVG LINE'] = avg_line
        standings.loc[rownum, 'OFF RK (YDS)'] = off_rk
        standings.loc[rownum, 'OFF YDS/G'] = off_yds
        standings.loc[rownum, 'PTS FOR/G'] = pf
        standings.loc[rownum, 'DEF RK (YDS)'] = def_rk
        standings.loc[rownum, 'YDS ALWD/G'] = def_yds
        standings.loc[rownum, 'PTS ALWD/G'] = pa
        standings.loc[rownum, 'H/A'] = h_a
        standings.loc[rownum, 'Total Inj'] = inj
        standings.loc[rownum, 'Non-IR'] = non_ir
        standings.loc[rownum, 'IR'] = ir

    rownum += 1

  #print(standings.to_string())
  #standings.to_csv('compiled_stats.csv')
  return standings


#put full team names in games.csv
def rename_games(compiled_stats):
  rownum = 0
  games_list = pd.read_csv('games.csv', index_col=0)
  game = games_list.iloc[rownum]

  while game.empty == False and rownum < 35:
    
    try:
      game = games_list.iloc[rownum,:]
      teamname_game = game.get('Team Name')
    except IndexError:
      break
    
    if 'NY' in teamname_game or 'LA' in teamname_game:
      teamname_game = teamname_game.split()
      teamname_game = teamname_game[1] 
      #print (both_teams)

    for index, row in compiled_stats.iterrows():
      teamname_compiled = row['Teamname']
      #print(teamname_compiled)
        
      if teamname_game in teamname_compiled:
        games_list.loc[rownum, 'Team Name'] = teamname_compiled
        #print(teamname_compiled)
      
    rownum += 1
  #print(games_list.to_string())
  games_list.to_csv('games.csv')


# find each team's opponent, add it in a column
def get_opponent(compiled_stats):
  rownum = 0
  row_start = 0
  row_end = 1
  games_list = pd.read_csv('games.csv', index_col=0)
  game = games_list.loc[row_start:row_end]
  

  while game.empty == False and rownum < 35:
    row_count = 0
    both_teams = []
    #print (game.to_string())

    for team in game.loc[:, 'Team Name']:
      
      if 'NY' in team or 'LA' in team:
        team = team.split()
        team = team[1]
      both_teams.append(team)

    for index, row in compiled_stats.iterrows():
      teamname_compiled = row['Teamname']
      count = 0
      
      #print(teamname_compiled)
      for team in both_teams:
        
        if team in teamname_compiled:
          if count == 0:
            compiled_stats.loc[row_count, 'Opp'] = both_teams[1]
            #print(row_count)
          elif count == 1:
            compiled_stats.loc[row_count, 'Opp'] = both_teams[0]
            #print(row_count)
          else:
            print('what happened')
            break
          #print (teamname_compiled)
          #print (team)
        count += 1
      row_count += 1

    rownum += 1
    row_start += 2
    row_end += 2
    game = games_list.loc[row_start:row_end]

  def get_weeknum():
    weeknum = 0
    
    print()
      
    while weeknum not in range(1,23):
      try:
        weeknum = int(input('Please enter the number of the week that we\'re in:'))
        if weeknum in range(1,23):
          break
        else:
          print('You did not enter a valid week number')
          #weeknum = int(input('Please enter the number of the week that we\'re in:'))
      except ValueError or UnboundLocalError:
        print('You did not enter a valid week number')
    return weeknum

  weeknum = str(get_weeknum())     
  #print(compiled_stats.to_string())
  compiled_stats.to_csv('compiled_stats_week'+weeknum+'.csv')
