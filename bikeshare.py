import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago','new york city','washington']
        city = input("\nWhich city would you like to consider? (Chicago, New York City or Washington)\n(Please enter full name; not case sensitive)\n").lower()
        if city in cities:
            break
        else:
            print("\nPlease enter a valid city name")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['january','february','march','april','may','june','all']
        month = input("\nWhich month would you like to consider? (January to June)\n(Please enter full name or Type 'all' for no month filter; not case sensitive)\n").lower()
        if month in months:
            break
        else:
            print("\nPlease enter a valid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        day = input("\nWhich day of the week would you like to consider?\n(Please enter full name or Type 'all' for no day filter; not case sensitive)\n").lower()
        if day in days:
            break
        else:
            print("\nPlease enter a valid day")

    print('-'*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        popular_month = df['month'].mode()[0]
        months = ['january','february','march','april','may','june']
        popular_month = months[popular_month-1]
        print("The most popular month is {} ".format(popular_month))

    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print("The most popular day of the week is",popular_day)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['Start Hour'].mode()[0]
    print("The most popular start hour is {}:00 hrs ".format(popular_start_hour))


    print("\nThis took {:.2f} seconds.".format(time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end Station is {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+" "+"to"+" "+ df['End Station']
    popular_combination = df['combination'].mode()[0]
    print("The most frequent combination of start and end Station is {}".format(popular_combination))


    print("\nThis took {:.2f} seconds.".format(time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = round(df['Trip Duration'].sum())
    #Total trip duration in minutes and seconds
    minute, second = divmod(total_trip_duration, 60)
    #Total trip duration in hour and minutes
    hour, minute = divmod(minute, 60)
    print("The total trip duration is {} hour(s), {} minutes and {} seconds".format(hour, minute, second))

    # TO DO: display mean travel time
    average_trip_duration = round(df['Trip Duration'].mean())
    #Average trip duration in minutes and seconds
    minutes, seconds = divmod(average_trip_duration, 60)
    #Print average trip duration in hours, minutes and seconds if minutes exceed 60
    if minutes > 60:
        hours, minutes = divmod(minutes, 60)
        print("\nThe average trip duration is {} hours, {} minutes and {} seconds".format(hours, minutes, seconds))
    else:
        print("\nThe average trip duration is {} minutes and {} seconds".format(minutes, seconds))


    print("\nThis took {:.2f} seconds.".format(time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("The count of each user type is:\n", user_type_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("\nThe count of each gender is:\n", gender_count)
    except:
        print("Sorry, there is no gender information for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print("\nThe earliest birth year is",earliest_year_of_birth)
        most_recent_year_of_birth = int(df['Birth Year'].max())
        print("\nThe most recent birth year is",most_recent_year_of_birth)
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("\nThe most common birth year is",most_common_year_of_birth)
    except:
        print("Sorry, there is no birth year information for this city.")

    print("\nThis took {:.2f} seconds.".format(time.time() - start_time))
    print('-'*60)

def display_data(df):
    """Displays five rows of individual trip data from the csv file of the city selected."""

    while True:
        response = ['yes','no']
        choice = input("Would you like to view individual trip data (5 entries)? Type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice == 'yes':
                start = 0
                end = 5
                data = df.iloc[start:end,:9]
                pd.set_option('display.max_columns',200)
                print(data)
            break
        else:
            print("Please enter a valid response")
    if choice == 'yes':
            while True:
                choice_2 = input("Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
                if choice_2 in response:
                    if choice_2 =='yes':
                        start += 5
                        end += 5
                        data = df.iloc[start:end,:9]
                        pd.set_option('display.max_columns',200)
                        print(data)
                    else:
                        break
                else:
                    print("Please enter a valid response")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no'.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
