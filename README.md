>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date modified
12 June 2021

### Project Title
_Explore US Bikeshare Data_

### Project Description
In this project, Python is used to explore data related to a bikeshare system for three major cities in the United States - **Chicago**, **New York City** and **Washington** towards uncovering the bike usage patterns in these cities.

### Project Details
The project entails building a python script (**bikeshare.py**) that takes in case insensitive user input on the city (**Chicago**, **New York City** or **Washington**) and period - month (**January** to **June**) and day of the week (**Sunday** to **Saturday**) - they would like to analyze.

The user should key in the month and day of the week using the full names. The user should also have the option of selecting **"all"** in regards to the month and day of week in which case the filters for the period will not apply.

Once the correct inputs have been provided, the script should be able to compute the below descriptive statistics:

**#1 Popular times of travel**
* most common month
* most common day of the week
* most common hour of the day

**#2 Popular stations and trip**
* most common start station
* most common end station
* most common combination of start and end station

**#3 Trip duration**
* total travel time
* average travel time

**#4 User information**
* count of each user type
* count of each gender (only available for New York City and Chicago)
* earliest, most recent and most common year of birth (only available for New York City and Chicago)

### Files used
Data files for the three cities:
* *chicago.csv*
* *new_york_city.csv*
* *washington.csv*

All three files contain the same six columns i.e. Start Time, End Time, Trip Duration (seconds), Start Station, End Station and User Type (subscriber or customer).

The _chicago.csv_ and _new_york_city.csv_ files contain two additional columns i.e. Gender and Birth Year.

### Software requirements
* Python 3
* Python libraries - NumPy, Pandas and Time
* A text editor e.g. Atom, Sublime text etc
* A terminal application e.g. Gitbash, Cygwin, Terminal etc

### Credits
[Udacity](https://knowledge.udacity.com) - The knowledge section within Udacity's Programming for Data Science with Python Nanodegree classroom was very useful in searching for answers to questions i had regarding the project.
