def ask_user_for_weeknum():
  weeknum = 0
      
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
  print()

  weeknum = str(weeknum)
  if len(weeknum) == 1:
      weeknum = '0'+weeknum
  return weeknum

def ask_user_for_season():
  season = 0
      
  while season not in range(2018,2021):
    try:
      season = int(input('Please enter the year of the season that we\'re in:'))
      if season in range(2018,2021):
        break
      else:
        print('You did not enter a valid season year')
    except ValueError or UnboundLocalError:
      print('You did not enter a valid season year')
  print()

  season = str(season)
  return season

# automate the weeknum instead of user input
def pull_weeknum():
