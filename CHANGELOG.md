#### Planned Changes
* Continue development of Neural Network
* Rework the file structure
* Automate the accuracy checking process
* Build a GUI (much later, regular app or web app?)
* automate the webscraping and prediction tasks

#### v0.4.2 - 11/1/18
* Added project to GitLab
* Added K Nearest Neighbor machine learning predictions
* Continued development of Neural Networks
* Added week 8 accuracy spreadsheet

**_(Everything past this point was before the creation of the changelog. The changes listed here are not very detailed compared to v0.4.2 and on.)_**

##### v0.4.0 - 10/26/18
* Introduction of Nerual Networks, first time ran with actual predictions

##### v0.3.0 - 10/24/18
* Added 3 prediction algorithms
    * Added RBF SVM, Random Forest, and XGBoost (GradientBoostClassifier in SKLearn)  

##### v0.2.6 - 10/17/18
* Introduced bug fixes to get_stats.py
    * Had issues with some input on websites, get_stats.py got confused  

##### v0.2.5 - N/A
* First week of real predictions
    * Predictions from 2 algorithms (Started with Logistic Regression & Linear SVM)

##### v0.2.4 - N/A
* Introduction of final_matchups csv document
    * Allowed for muuch easier predictions (was previously prediction each game twice, once for each team)
    * Predictions can now deicde on home or away team winning

##### v0.2.2 - N/A
* Introduced get_winners.py
    * created the function to allow for input of the weeknumber across the whole program

##### v0.2.1 - N/A
* Created files with the week number attached to them so that further weeks could be added without confusion

##### v0.2.0 - N/A
* Overhaul of how compiled_stats csv was made

##### v0.1.2 - N/A
* Creation of get_stats.py
    * Took the job of 5 different scripts and put them together into 1 script 

##### v0.1.1 - N/A
* Created bulk of webscraping/formatting scripts
    * format_injuries.py
    * format_lines.py
    * get_espn_lines.py
    * get_espn_stats.py
    * get_injuries_stats.py

##### v0.1.0 - N/A
* Birth of project
* Only had 1 script
* Scraped statistics for team's offenses, put the data in a csv
    