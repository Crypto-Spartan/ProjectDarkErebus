#### Planned Changes
* Continue development of Neural Network
* Rework the file structure (folders for each week instead of data type)
* Automate the accuracy checking process
* Build a GUI (web app)
    * Run python scripts that periodically update a website
    * Figure out where/best way to host the website
    * Website will launch v1.0.0
    * Each algorithm will be a named "bot" for competition among bots
        * Keep a record for each of the bots for fans to follow
* automate the webscraping and prediction tasks (should come when webapp is built)

#### v0.4.6.1 - 06/19/19
* Re-evaluating project for upcoming season
* Added new neural_net_visualized.py script, imported from the old repl.it project
    * Evaluating when neural net visualization was built in, looking to add visualization for other algorithms if possible
* Slight changes to changelog disclaimer about changes prior to v0.4.2
* Slightly modified changelog's 'planned changes'
* Fix typos in changelog 

#### v0.4.6 - 11/21/18
* Added week 12 predictions
* Moved files into data folder for cleanup
* Slightly modified changelog's 'planned changes'

#### v0.4.5 - 11/15/18
* **Found mistake in machine_learning.py, all SVM RBF predictions before week 11 are inaccurate, will take out all SVM RBF predictions from previous csv and Accuracy files (week 7-10)**
    * also fixed 'Majority Acc' in the Accuracy files
* Consider RBF SVM added on week 11's predictions
* Fixed a bug causing empty space to be displayed for their rank when 2 teams had the same yardage (offensive and defensive)
* added week 11 predictions
* added week 10 accuracy report

#### v0.4.4 - 11/7/18
* Created separate get_winners file for added functionality
    * modified build_table.py and get_winners.py
* Added week 9 winners
* Added week 9 accuracy report
* started work on web ui
* started work on file restructure
    * turned single digit numbers into 2 digit numbers for numerical order going into week 10
        * (instead of week1.csv, it will read as week01.csv)
    * put files into data folder
    * added 'placeholder.txt' to show file structure for some folders

#### v0.4.3 - 11/1/18
* Added Naive Bayes Classifier (GaussianNB)
* Added K Nearest Neighbor machine learning predictions
* Included week 9 predictions (With new classifiers included)

#### v0.4.2 - 11/1/18
* Added project to GitLab, imported from repl.it
* Continued development of Neural Networks
* Added week 8 accuracy spreadsheet
* Created CHANGELOG.md

**_(Everything prior to v0.4.2 was before the creation of the changelog. The changes listed here are not as detailed as later revisions.)_**

##### v0.4.0 - 10/26/18
* Introduction of Nerual Networks, first time ran with actual predictions

##### v0.3.1 - 10/24/18
* Included week 8 predictions

##### v0.3.0 - 10/24/18
* Added 3 prediction algorithms 
    * Added RBF SVM, Random Forest, and XGBoost (GradientBoostClassifier in SKLearn) 
    * Even though week7 was over, predictions were made with week 5 & 6 stats
* Restructed the way that final_predictions was built
    * Fixed a bug that caused the probability to appear as below 50%

##### v0.2.6 - 10/17/18
* Introduced multiple bug fixes to get_stats.py
    * Had issues with some input on websites, get_stats.py got confused  

##### v0.2.5
* Created final_predictions csv document (Week 7)
    * First real predictions (rather than running tests on available data)
    * Predictions from 2 algorithms (Started with Logistic Regression & Linear SVM)

##### v0.2.4
* Introduction of final_matchups csv document
    * Allowed for much easier predictions (was previously prediction each game twice, once for each team)
    * Predictions can now deicde on home or away team winning
    * Used dummy variables/OneHotEncoding to account for the home/away teams

##### v0.2.2
* Introduced get_winners.py
    * created the function to allow for input of the weeknumber across the whole program

##### v0.2.1
* Created files with the week number attached to them so that further weeks could be added without confusion
* Created build_table.py to get the stats and finalize table for predictions
    * moved the get_weeknum function to build_table.py
* I figured out what dummy variables were, later used this as "OneHotEncoding" for predictions 

##### v0.2.0
* Overhaul of how compiled_stats csv was made
* Creation of get_weeknum function, placed in compile_stats.py

##### v0.1.2
* Creation of get_stats.py
    * Took the job of 5 different scripts and put them together into 1 script 

##### v0.1.1
* Created bulk of webscraping/formatting scripts
    * format_injuries.py
    * format_lines.py
    * get_espn_lines.py
    * get_espn_stats.py
    * get_injuries_stats.py

##### v0.1.0
* Birth of project under codename ProjectDarkErebus
* Only had 1 script
* Scraped statistics for team's offenses, put the data in a csv
    