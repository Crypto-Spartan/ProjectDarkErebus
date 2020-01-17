from flask import Flask, render_template, url_for
import pandas as pd
import website_functions as wf


current_weeknum = '12'
current_year = '2018'



#start of flask app
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('homepage.html', title='Home')



@app.route('/predictions')
def predictions():
  return render_template('predictions.html', title='Predictions', weeknum=current_weeknum, year=current_year, prediction_list=wf.create_pred_tables(), game_outcomes=wf.check_game_outcome(current_weeknum, current_year))

@app.route('/predictions-chart')
def predictions_chart():
  return render_template('predictions-chart.html', title='Predictions Chart', weeknum=current_weeknum, year=current_year, pred_for_chart=wf.create_full_chart(), game_outcomes=wf.check_game_outcome(current_weeknum, current_year))

@app.route('/predictions-archive')
def predictions_archive_select():
  return render_template('predictions-archive.html', title='Predictions Archive', files_list=wf.check_archive_folder())

@app.route('/archive/predictions/<int:year>/<int:week>')
def archive_predictions_render(week, year):
  return render_template('predictions.html', title=f'Archive - Predictions - Week {week}, {year}', prediction_list=wf.create_pred_tables(week, year), weeknum=week, year=year, game_outcomes=wf.check_game_outcome(week, year), archive=True)

@app.route('/archive/predictions-chart/<int:year>/<int:week>')
def archive_predictions_chart_render(week, year):
  return render_template('predictions-chart.html', title=f'Archive - Chart - Week {week}, {year}', pred_for_chart=wf.create_full_chart(week, year), weeknum=week, year=year, game_outcomes=wf.check_game_outcome(week, year), archive=True)

@app.route('/statistics')
def statistics():
  return render_template('statistics.html', title='Statistics')

@app.route('/about-our-bots')
def about_our_bots():
  return render_template('about-our-bots.html', title='About Our Bots')

@app.route('/about-us')
def about():
  return render_template('about-us.html', title='About Us')

@app.route('/contact-us')
def contact():
  return render_template('contact-us.html', title='Contact Us')


# testing pages
@app.route('/test')
def test():
  return render_template('test.html', title='Test')

@app.route('/test2')
def test2():
  return render_template('test2.html', title='Test2', weeknum=current_weeknum, prediction_list=wf.create_pred_tables())

@app.route('/test3')
def test3():
  return render_template('test3.html', title='Test3')

@app.route('/test4')
def test4():
  return render_template('test4.html', title='Test4')


#app.jinja_env.add_extension('jinja2.ext.loopcontrols')

if __name__ == '__main__':
  app.run('0.0.0.0',8080, debug=False)

