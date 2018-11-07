# find the winners each week

import sys
import csv
import pandas as pd
import get_weeknum 

weeknum = get_weeknum.ask_user_for_weeknum()

def ask_user_for_winners(weeknum):
  rownum = 0
  final_matchups = pd.read_csv('final_matchups_week'+weeknum+'.csv', index_col=0)
  matchup = final_matchups.loc[rownum]
  print('As my program is still young, we need help finding the winners')
  print('You may type "home", "away", "tie", "h", "2", "a", "1" or "t"')
  possible_answers = ['home', 'away', 'tie', 'h', 'a', 't', '1', '2']

  while matchup.empty == False:

    try:
      matchup = final_matchups.loc[rownum]
      home_team = matchup.get('Home Team')
      away_team = matchup.get('Away Team')
      #print(away_team+' AT '+home_team)
    except:
      break

    winner = '' 
    while winner not in possible_answers:
      try:
        winner = (str(input('Which team won? %s AT %s:' % (away_team, home_team)))).lower() 
        if winner in possible_answers:
          break
        else:
          print('You did not enter a valid answer')
          print()
      except:
        print('You did not enter a valid answer')
        print()

    if winner == 'home' or winner == 'h' or winner == '2':
      final_matchups.loc[rownum, 'Winner'] = 1
    elif winner == 'away' or winner == 'a' or winner == '1':
      final_matchups.loc[rownum, 'Winner'] = -1
    elif winner == 'tie' or winner == 't':
      final_matchups.loc[rownum, 'Winner'] = 0

    rownum += 1
  
  final_matchups.to_csv('final_matchups_week'+weeknum+'.csv')
  print (final_matchups[['Away Team', 'Home Team', 'Winner']].to_string())

ask_user_for_winners(weeknum)