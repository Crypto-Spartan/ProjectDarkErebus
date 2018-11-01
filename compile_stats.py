# compile team rankings and add to compiled_stats.csv

import csv
import pandas as pd


# build entire pandas table
def build_table(weeknum):
  print('building table')
  print('compiling stats')
  #creating compiled_stats object
  compiled_stats = compile_w_standings(compile_off_def_inj(weeknum), weeknum)
  print('fixing team names')
  rename_games(compiled_stats, weeknum)
  print('finding opponents')
  drop_bye_weeks(get_opponent(compiled_stats, weeknum), weeknum)
  print('creating matchups')
  setup_matchup(compiled_stats, weeknum)
  print()
  print('table build complete')
  


# put together offensive stats, defensive stats, and injury stats
def compile_off_def_inj(weeknum):
  rownum = 0
  lines = pd.read_csv('nfl_lines_week'+weeknum+'.csv')
  lines.rename(columns={'Unnamed: 0':'Team Name'}, inplace=True)
  team = lines.iloc[rownum]
  df_off_stats = pd.read_csv('nfl_stats_off_week'+weeknum+'.csv')
  df_def_stats = pd.read_csv('nfl_stats_def_week'+weeknum+'.csv')
  df_injury_stats = pd.read_csv('injuries_stats_week'+weeknum+'.csv', index_col=0)

  try:
    while team.empty == False:
      #team = team.to_frame()
      #print(team.get('Team Name'))
      try:
        team = lines.iloc[rownum,:]
        teamname_line = team.get('Team Name')
      except IndexError:
        break

      iterrow_count = 0
      for index, row in df_off_stats.iterrows():
        #print (row['RK'], row['TEAM'], row['YDS/G'], row['PTS/G'])
        teamrk_offyds = row['RK']
        teamname_off = str(row['TEAM'])
        teamoffydsg = row['YDS/G']
        teamoffptsg = row['PTS/G']
        
        test_empty_string = str(row['RK']).replace(u'\xa0', u' ')
        if test_empty_string == ' ' and iterrow_count > 0:
          teamrk_offyds = df_off_stats.loc[iterrow_count-1, 'RK']
          
        if teamname_off == str(teamname_line):
          lines.loc[rownum, 'OFF RK (YDS)'] = int(teamrk_offyds)
          lines.loc[rownum, 'OFF YDS/G'] = teamoffydsg
          lines.loc[rownum, 'POINTS FOR'] = teamoffptsg
        
        iterrow_count += 1

      
      iterrow_count = 0
      for index, row in df_def_stats.iterrows():
        #print (row['RK'], row['TEAM'], row['YDS/G'], row['PTS/G']
        teamname_def = str(row['TEAM'])
        teamrk_defyds = row['RK']
        teamdefydsg = row['YDS/G']
        teamdefptsg = row['PTS/G']
        
        test_empty_string = str(row['RK']).replace(u'\xa0', u' ')
        if test_empty_string == ' ' and iterrow_count > 0:
          teamrk_defyds = df_def_stats.loc[iterrow_count-1, 'RK']
        
        if teamname_def == str(teamname_line):
          lines.loc[rownum, 'DEF RK (YDS)'] = int(teamrk_defyds)
          lines.loc[rownum, 'DEF YDS/G'] = teamdefydsg
          lines.loc[rownum, 'POINTS ALWD'] = teamdefptsg

        iterrow_count += 1

      if rownum % 2 == 1:
        lines.loc[rownum, 'H/A'] = 1
      elif rownum % 2 == 0:
        lines.loc[rownum, 'H/A'] = 0
    
      for index, row in df_injury_stats.iterrows():
        teamname_inj = str(row['Team'])

        if teamname_inj == str(teamname_line):
          lines.loc[rownum, 'Total Injured'] = row['Total Injured']
          lines.loc[rownum, 'Non-IR'] = row['Non-IR']
          lines.loc[rownum, 'IR'] = row['IR']

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
  games.to_csv('games_week'+weeknum+'.csv')
  return lines


# put everything together with the standings
def compile_w_standings(team_stats, weeknum):
  rownum = 0
  standings = pd.read_csv('standings_week'+weeknum+'.csv', index_col=0)
  team = standings.iloc[rownum]

  while team.empty == False:
    
    try:
      team = standings.iloc[rownum,:]
      team_strk = team.get('STRK')
    except IndexError:
      break

    if team_strk[0] == 'W':
      team_strk = int(team_strk[1:])
    elif team_strk[0] == 'L':
      team_strk = int(team_strk[1:]) * -1
    elif '-' in team_strk:
      team_strk = 0
    else:
      print(team_strk)
      print('TEAM STRK ERROR')
      break
    
    standings.loc[rownum, 'STRK'] = team_strk
    rownum += 1

  rownum = 0
  while team.empty == False:
    
    try:
      team = standings.iloc[rownum,:]
      teamname_standings = team.get('Teamname')
      home = team.get('HOME')
      away = team.get('AWAY')
      div = team.get('DIV')
      conf = team.get('CONF')
    except IndexError:
      break

    if int(home[2]) == 0:
      home = float(1)
    elif int(home[0]) == 0:
      home = float(0)
    else:
      home = float(home[0]) / (float(home[0]) + float(home[2])) 
    
    if int(away[2]) == 0:
      away = float(1)
    elif int(away[0]) == 0:
      away = float(0)
    else:
      away = float(away[0]) / (float(away[0]) + float(away[2]))

    if int(div[2]) == 0:
      div = float(1)
    elif int(div[0]) == 0:
      div = float(0)
    else:
      div = float(div[0]) / (float(div[0]) + float(div[2]))

    if int(conf[2]) == 0:
      conf = float(1)
    elif int(conf[0]) == 0:
      conf = float(0)
    else:
      conf = float(conf[0]) / (float(conf[0]) + float(conf[2]))

    standings.loc[rownum, 'HOME'] = home
    standings.loc[rownum, 'AWAY'] = away
    standings.loc[rownum, 'DIV'] = div
    standings.loc[rownum, 'CONF'] = conf
    rownum += 1

  #print (standings.to_string())

  rownum = 0
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
def rename_games(compiled_stats, weeknum):
  rownum = 0
  games_list = pd.read_csv('games_week'+weeknum+'.csv', index_col=0)
  game = games_list.iloc[rownum]

  while game.empty == False:
    
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
  games_list.to_csv('games_week'+weeknum+'.csv')


# find each team's opponent, add it in a column
def get_opponent(compiled_stats, weeknum):
  rownum = 0
  row_start = 0
  row_end = 1
  games_list = pd.read_csv('games_week'+weeknum+'.csv', index_col=0)
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

       
  #print(compiled_stats.to_string())
  #compiled_stats.to_csv('compiled_stats_week'+weeknum+'.csv')
  return(compiled_stats)


def drop_bye_weeks(compiled_stats, weeknum):
  print('removing teams on bye')
  rownum = 0
  stats_list = compiled_stats
  game = stats_list.iloc[rownum]

  while game.empty == False:
    
    try:
      game = stats_list.iloc[rownum,:]
      teamname = game.get('Teamname')
      opp = game.get('Opp')
      line = game.get('AVG LINE')
      #print(game)
    except IndexError:
      break
    
    if type(opp) != str:
      stats_list = stats_list.drop(stats_list.index[rownum])
      stats_list = stats_list.reset_index(drop=True)
      rownum -= 1
      #print(teamname)
      
    rownum += 1
  
  #create winner column
  stats_list['Winner'] = ''
  
  #put it in a csv
  stats_list.to_csv('compiled_stats_week'+weeknum+'.csv')


def setup_matchup(compiled_stats, weeknum):
  stats_list = compiled_stats
  rownum = 0
  row_start = 0
  row_end = 1
  team = stats_list.iloc[rownum]
  games = pd.read_csv('games_week'+weeknum+'.csv', index_col=0)
  final_matchups = games[['Team Name', 'Avg Line']]
  final_matchups = final_matchups.rename(columns={'Team Name':'Away Team'})
  final_matchups = final_matchups.rename(columns={'Avg Line':'AT'})
  matchup = final_matchups.loc[row_start:row_end]
  #print(final_matchups)

  while matchup.empty == False:

    try:
      matchup = final_matchups.loc[row_start:row_end]
      away_team = games.loc[row_start]
      home_team = games.loc[row_end]
      teamname_away = matchup.loc[row_start, 'Away Team']
      teamname_home = matchup.loc[row_end, 'Away Team']
      away_line = matchup.loc[row_start, 'AT']
      home_line = matchup.loc[row_end, 'AT']
      print('Setting up %s AT %s' % (teamname_away, teamname_home))
    except:
      break
    
    #print(final_matchups)
    final_matchups.loc[row_start, 'Home Team'] = teamname_home
    final_matchups.loc[row_start, 'Away Line'] = away_line
    final_matchups.loc[row_start, 'Home Line'] = home_line
    final_matchups = final_matchups.drop(final_matchups.index[row_end])
    final_matchups = final_matchups.reset_index(drop=True)
    final_matchups.loc[row_start, 'AT'] = 'AT'
    
    #print(final_matchups.to_string())
    row_start += 1
    row_end += 1
    matchup = games.loc[row_start:row_end]
  
  
  
  matchup = final_matchups.loc[rownum]
  while matchup.empty == False:
    rownum_stats = 0
    stat_line = stats_list.loc[rownum_stats]
    
    try:
      matchup = final_matchups.loc[rownum]
      away_team = matchup.get('Away Team')
      home_team = matchup.get('Home Team')
    except:
      break

    
    while stat_line.empty == False:

      try:
        stat_line = stats_list.loc[rownum_stats]
        teamname_stats = stat_line.get('Teamname')
      except:
        break
      #print(stat_line)
      #print(teamname_stats)

      if teamname_stats == away_team:
        final_matchups.loc[rownum, 'AwT_W'] = stat_line.get('W')
        final_matchups.loc[rownum, 'AwT_L'] = stat_line.get('L')
        final_matchups.loc[rownum, 'AwT_T'] = stat_line.get('T')
        final_matchups.loc[rownum, 'AwT_Pct'] = stat_line.get('PCT')
        final_matchups.loc[rownum, 'AwT_HmPct'] = stat_line.get('HOME')
        final_matchups.loc[rownum, 'AwT_AwPct'] = stat_line.get('AWAY')
        final_matchups.loc[rownum, 'AwT_DvPct'] = stat_line.get('DIV')
        final_matchups.loc[rownum, 'AwT_CnfPct'] = stat_line.get('CONF')
        final_matchups.loc[rownum, 'AwT_PF'] = stat_line.get('PF')
        final_matchups.loc[rownum, 'AwT_PA'] = stat_line.get('PA')
        final_matchups.loc[rownum, 'AwT_PtDiff'] = stat_line.get('DIFF')
        final_matchups.loc[rownum, 'AwT_Strk'] = stat_line.get('STRK')
        final_matchups.loc[rownum, 'AwT_OffRk(yds)'] = stat_line.get('OFF RK (YDS)')
        final_matchups.loc[rownum, 'AwT_OffYds/G'] = stat_line.get('OFF YDS/G')
        final_matchups.loc[rownum, 'AwT_PF/G'] = stat_line.get('PTS FOR/G')
        final_matchups.loc[rownum, 'AwT_DefRk(yds)'] = stat_line.get('DEF RK (YDS)')
        final_matchups.loc[rownum, 'AwT_YdsAlwd/G'] = stat_line.get('YDS ALWD/G')
        final_matchups.loc[rownum, 'AwT_PtsAlwd/G'] = stat_line.get('PTS ALWD/G')
        final_matchups.loc[rownum, 'AwT_TotInj'] = stat_line.get('Total Inj')
        final_matchups.loc[rownum, 'AwT_NonIR'] = stat_line.get('Non-IR')
        final_matchups.loc[rownum, 'AwT_IR'] = stat_line.get('IR')
      
      rownum_stats += 1
      
    rownum_stats = 0
    while stat_line.empty == False:

      try:
        stat_line = stats_list.loc[rownum_stats]
        teamname_stats = stat_line.get('Teamname')
      except:
        break
      #print(stat_line)
      #print(teamname_stats)

      if teamname_stats == home_team:
        final_matchups.loc[rownum, 'HmT_W'] = stat_line.get('W')
        final_matchups.loc[rownum, 'HmT_L'] = stat_line.get('L')
        final_matchups.loc[rownum, 'HmT_T'] = stat_line.get('T')
        final_matchups.loc[rownum, 'HmT_Pct'] = stat_line.get('PCT')
        final_matchups.loc[rownum, 'HmT_HmPct'] = stat_line.get('HOME')
        final_matchups.loc[rownum, 'HmT_AwPct'] = stat_line.get('AWAY')
        final_matchups.loc[rownum, 'HmT_DvPct'] = stat_line.get('DIV')
        final_matchups.loc[rownum, 'HmT_CnfPct'] = stat_line.get('CONF')
        final_matchups.loc[rownum, 'HmT_PF'] = stat_line.get('PF')
        final_matchups.loc[rownum, 'HmT_PA'] = stat_line.get('PA')
        final_matchups.loc[rownum, 'HmT_PtDiff'] = stat_line.get('DIFF')
        final_matchups.loc[rownum, 'HmT_Strk'] = stat_line.get('STRK')
        final_matchups.loc[rownum, 'HmT_OffRk(yds)'] = stat_line.get('OFF RK (YDS)')
        final_matchups.loc[rownum, 'HmT_OffYds/G'] = stat_line.get('OFF YDS/G')
        final_matchups.loc[rownum, 'HmT_PF/G'] = stat_line.get('PTS FOR/G')
        final_matchups.loc[rownum, 'HmT_DefRk(yds)'] = stat_line.get('DEF RK (YDS)')
        final_matchups.loc[rownum, 'HmT_YdsAlwd/G'] = stat_line.get('YDS ALWD/G')
        final_matchups.loc[rownum, 'HmT_PtsAlwd/G'] = stat_line.get('PTS ALWD/G')
        final_matchups.loc[rownum, 'HmT_TotInj'] = stat_line.get('Total Inj')
        final_matchups.loc[rownum, 'HmT_NonIR'] = stat_line.get('Non-IR')
        final_matchups.loc[rownum, 'HmT_IR'] = stat_line.get('IR')


      rownum_stats += 1
    
    rownum += 1

  print('setting dummy variables')

  for team in stats_list.iterrows():
    teamname = team[1].get('Teamname')
    final_matchups.loc[:, 'Away Team_'+teamname] = 0
    final_matchups.loc[:, 'Home Team_'+teamname] = 0

  rownum = 0
  for game in final_matchups.iterrows():
    home_team = game[1].get('Home Team')
    away_team = game[1].get('Away Team')
    final_matchups.loc[rownum, 'Away Team_'+away_team] = 1
    final_matchups.loc[rownum, 'Home Team_'+home_team] = 1

    rownum += 1
    

  #print(final_matchups.to_string())
  final_matchups.to_csv('final_matchups_week'+weeknum+'.csv')
  return final_matchups
  

