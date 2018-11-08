# get all of the data, compile it nice and pretty
import compile_stats as compiler
import get_stats as stats
import get_weeknum

weeknum = get_weeknum.ask_user_for_weeknum()

# get all of the stats
#stats.get_all(weeknum)

# build the pandas table
compiler.build_table(weeknum)
print('full matchup data available in "final_matchups_week%s.csv"' % (weeknum))
