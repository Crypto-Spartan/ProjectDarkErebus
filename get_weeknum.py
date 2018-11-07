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
  #print(weeknum)
  return weeknum

#ask_user_for_weeknum()