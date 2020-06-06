import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        except:
            print('Something went wrong. Please try again!')
        if city.lower() in CITY_DATA.keys():
            return city.lower()
        else:
            print('That is not a valid city. Please try again!')

def get_month():
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        try:
            month = input('For which month would you like to see results - All, January, February, March, April, May, or June?\n')
        except:
            print('Something went wrong. Please try again!')
        if month.lower() in months:
            return month.lower()
        else:
            print('That is not a valid answer. Please try again and type "All", "January", "February", "March", "April", "May", or "June"!')

def get_day():
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        try:
            day = input('For which day would you like to see results - All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n')
        except:
            print('Something went wrong. Please try again!')
        if day.lower() in days:
            return day.lower()
        else:
            print('That is not a valid answer. Please try again and type "All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", or "Sunday"!')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city = get_city()

    # get user input for month (all, january, february, ... , june)
    month = get_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day()

    print('-'*40)
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
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Station Combination'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Station Combination'].mode()[0]
    print('Most Popular Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time in minutes:', round(df['Trip Duration'].sum() / 60))


    # display mean travel time
    print('Mean travel time in minutes:', round(df['Trip Duration'].mean() / 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df:
        print('Counts of genders:\n', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())
        most_common_year = df['Birth Year'].mode()[0]
        print('Most common year of birth:', most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def req_five_lines(df):
    valid_answer_lines = ['yes', 'no']
    line_start = 0
    while True:
        try:
            five_lines = input('Would you like to see five lines of raw data? Please enter "yes" or "no".\n')
        except:
            print('Something went wrong. Please try again!')
        if five_lines.lower() in valid_answer_lines:
            while five_lines.lower() == 'yes':
                print(df[line_start:line_start+5])
                five_lines = input('Would you like to see five more lines of raw data? Please enter "yes" or "no".\n')
                line_start += 5
            break
        else:
            print('That is not a valid answer. Please try again and type "yes" or "no"!')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        req_five_lines(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
