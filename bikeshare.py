import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
cities = ['chicago', 'new york', 'washington']

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = ['all','sunday', 'monday', 'tuesday', 'wednesday', 
        'thursday', 'friday', 'saturday' ]

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
    
    # TO DO: get user input for month (all, january, february, ... , june)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    while True:
        city = input("Which city do you want to explore? (chicago, new york city, washington)")
        city = city.lower()
        if city in cities:
            month = input ("Which month do you want to explore (all, january, february, ... , june)?")
            day = input("Which day do you want to analyze (all, monday, tuesday, ... sunday) ? ")
            break
        else:
            city = input("Invalid city! Please Re-enter (chicago, new york city, washington)")


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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    print(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month =  months.index(month)
        df = df[ df['month'] == month ]
    
    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print("The most common month: " , month)
    
    # TO DO: display the most common day of week
    day = df['day_of_week'].value_counts().mode()[0]
    print("The most common day of week: " , day)
    
    # TO DO: display the most common start hour
    hour = df['hour'].value_counts().mode()[0]
    print("The most common start hour: " , hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode().to_string(index = False)
    print("The most common start station: " , start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode().to_string(index = False)
    print("The most common end station: " , end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most common start and end station combination" ,start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts = df['User Type'].value_counts()
    print("Counts of user types: " , counts)
    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("Counts of gender: " , gender_counts)
    # TO DO: Display earliest, most recent, and most common year of birth
    common = df['Birth Year'].value_counts().idxmax()
    print("The most common birth year: " , common)
    recent = df['Birth Year'].max()
    print("The most recent birth year: " , recent)
    earliest = df['Birth Year'].min()
    print("The most earliest birht year: " , earliest)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
