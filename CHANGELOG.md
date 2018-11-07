#### Planned Changes
* Continue development of Neural Network
* Rework the file structure
* Automate the accuracy checking process
* Build a GUI (much later, regular app or web app?)
* automate the webscraping and prediction tasks

#### v0.4.4 - 11/7/18
* Created separate get_winners file for added functionality
    * modified build_table.py and get_winners.py
* Added week 9 winners
* Added week 9 accuracy report
* started work on web ui
* started work on file restructure
    * added 'placeholder.txt' to show file structure

#### v0.4.3 - 11/1/18
* Added Naive Bayes Classifier (GaussianNB)
* Added K Nearest Neighbor machine learning predictions
* Included week 9 predictions (With new classifiers included)

#### v0.4.2 - 11/1/18
* Added project to GitLab
* Continued development of Neural Networks
* Added week 8 accuracy spreadsheet
* Created CHANGELOG.md

**_(Everything past this point was before the creation of the changelog. The changes listed here are not very detailed compared to v0.4.2 and on.)_**

##### v0.4.0 - 10/26/18
* Introduction of Nerual Networks, first time ran with actual predictions

##### v0.3.1 - 10/24/18
* Included week8 predictions

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
    * Allowed for muuch easier predictions (was previously prediction each game twice, once for each team)
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
* Birth of project
* Only had 1 script
* Scraped statistics for team's offenses, put the data in a csv
    