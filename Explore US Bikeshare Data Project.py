import time
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Kindly, Choose a city from these 3 cities [chicago, new york city, washington]: ').lower().strip()
        if city not in CITY_DATA:
            print('Please, Enter a city from the available 3 cities!!')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            'Kindly, Choose a month form january to june or type "all" to show all months\' data: ').lower().strip()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months and month != 'all':
            print('Please, Enter a month from the first 6 months of year or Enter all!!')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            'Kindly, Choose a day from sunday to saturday or type "all" to show all days\' data: ').lower().strip()
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if day not in days and day != 'all':
            print('Please, Enter a valid day or Enter all!!')
        else:
            break

    print('-' * 40)
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
    # to load data from csv file to Pandas DataFrame ^--^
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime ^--^
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns ^--^
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable ^--^
    if month != 'all':
        # use the index of the months list to get the corresponding int ^--^
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe ^--^
        df = df[df['month'] == month]

    # filter by day of week if applicable ^--^
    if day != 'all':
        # filter by day of week to create the new dataframe ^--^
        df = df[df['day_of_week'] == day.title()]

    return df


def diaplay_data(df):
    """
    to ask the user whether he/she wants to see first 5 rows of data or not
    :param df: a Pandas DataFrame got from load_data function
    """
    j = 0
    answer = input('Kindly, Decide whether you want to display the first 5 rows of data or not.\nPlease, type "yes" or "no": ').lower().strip()
    pd.set_option("display.max_columns", None)
    while True:
        if answer == 'no':
            break
        print(df.iloc[j : (j+5)])
        answer = input('Kindly, Decide whether you want to display the following 5 rows of data or not.\nPlease, type "yes" or "no": ').lower().strip()
        j = j + 1

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month ^--^
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}.'.format(most_common_month))

    # display the most common day of week ^--^
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of week is {}.'.format(most_common_day_of_week))

    # display the most common start hour ^--^
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is {}.'.format(most_common_start_hour))

    #time_stats_message = 'The most common month is {}.\nThe most_common_day_of_week is {}.\nThe most common start hour is {}.'.format(most_common_month, most_common_day_of_week, most_common_start_hour)
    #print(time_stats_message)
    # return time_stats_message
    # I highlited the above two lines as comments in order not to make a long in-line code

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station ^--^
    most_common_used_start_station = df['Start Station'].mode()[0]
    most_common_used_start_station_count = df['Start Station'].value_counts().max()
    print('The most commonly used start station is {} with count of {}.'.format(most_common_used_start_station, most_common_used_start_station_count))

    # display most commonly used end station ^--^
    most_common_used_end_station = df['End Station'].mode()[0]
    most_common_used_end_station_count = df['End Station'].value_counts().max()
    print('The most commonly used end station is {} with count of {}.'.format(most_common_used_end_station, most_common_used_end_station_count))

    # display most frequent combination of start station and end station trip ^--^
    df['Start / End Station'] = df['Start Station'] + ' ==> ' + df['End Station']
    most_frequent_start_and_end_station = df['Start / End Station'].mode()[0]
    most_frequent_start_and_end_station_count = df['Start / End Station'].value_counts().max()
    print('The most frequent combination of start station and end station trip is {} with count of {}.'.format(most_frequent_start_and_end_station,most_frequent_start_and_end_station_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time ^--^
    total_travel_time = df['Trip Duration'].sum()
    total_trip_count = df['Trip Duration'].count()
    print('The total travel time for trip is {} seconds (or {} hours) for trips count of {}.'.format(total_travel_time, total_travel_time/3600, total_trip_count))

    # display mean travel time ^--^
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is {} seconds (or {} minutes).'.format(mean_travel_time, mean_travel_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types ^--^
    user_types_count = df['User Type'].value_counts().count()
    total_number_of_users = df['User Type'].count()
    print('There are {} user type(s) with total number of users of {}.'.format(user_types_count, total_number_of_users))

    for i in range(user_types_count):
        user_type_name = df['User Type'].value_counts().index[i]
        user_type_number = df['User Type'].value_counts().values[i]
        user_type_percent = user_type_number * 100 / df['User Type'].count()
        print('- a {} is a user type with count of {} of {}%.'.format(user_type_name, user_type_number, user_type_percent))


    # Display counts of gender ^--^
    if 'Gender' in df:
        print('\n')
        user_gender_types_count = df['Gender'].value_counts().count()
        print('There are {} user type(s)'.format(user_gender_types_count))

        for i in range(user_gender_types_count):
            user_gender_type_name = df['Gender'].value_counts().index[i]
            user_gender_type_number = df['Gender'].value_counts().values[i]
            user_gender_type_percent = user_gender_type_number * 100 / df['Gender'].count()
            print('- a {} is a user gender type with count of {} of {}%.'.format(user_gender_type_name, user_gender_type_number, user_gender_type_percent))

    # Display earliest, most recent, and most common year of birth ^--^
    if 'Birth Year' in df:
        print('\n')
        earliest_year_of_birth = df['Birth Year'].min()
        print('The earliest year of birth of a user is {}.'.format(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print('The most recent year of birth of a user is {}.'.format(most_recent_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('The most common year of birth of a user is {}.'.format(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        diaplay_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


