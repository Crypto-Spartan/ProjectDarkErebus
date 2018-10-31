# get all of the data, compile it nice and pretty
import compile_stats as compiler
import get_stats as stats

def get_weeknum():
  weeknum = 0
      
  while weeknum not in range(1,23):
    try:
      weeknum = int(input('Please enter the number of the week that we\'re in:'))
      if weeknum in range(1,23):
        print()
        break
      else:
        print('You did not enter a valid week number')
        #weeknum = int(input('Please enter the number of the week that we\'re in:'))
    except ValueError or UnboundLocalError:
      print('You did not enter a valid week number')
  print()
  return str(weeknum)

weeknum = get_weeknum()

# get all of the stats
stats.get_all(weeknum)

# build the pandas table
compiler.build_table(weeknum)
