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
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city\'s data do you want to search for? Enter[chicago, new york city, washington]: ').lower() 
        if city in CITY_DATA.keys():
            break
        print('Once again')
        
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('What month\'s data do you want to search for? Enter[all, january, february, ... , june]: ').lower()
        month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if month in month_list:
            break
        print('Once again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('What day of the week do you want to search for? Enter[all, monday, tuesday, ... sunday]: ').lower() 
        day_list = ['all', 'monday', 'tuesday', 'Wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day in day_list:
            break
        print('Once again')
    

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
    
    # extract month and day of week from Start Time to create new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
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
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('The most common month is {}. '.format(months[popular_month - 1]))

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is {}. '.format(popular_day_of_week))

    # display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is {}. '.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}. '.format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end Station is {}. '.format(end_station))

    # display most frequent combination of start station and end station trip
    combination_station = df[['Start Station','End Station']].mode()
    print('The most frequent combination of start station and end station trip is to {} from {}. '.format(
        combination_station['Start Station'][0], combination_station['End Station'][0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_travel_time = df['Trip Duration'].sum()
    print('Total travel time is {}[sec].'.format(sum_travel_time))

    # display mean travel time
    ave_travel_time = df['Trip Duration'].mean()
    print('Average travel time is {}[sec].'.format(ave_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('** Counts of user types')
    print(df['User Type'].value_counts(),'\n')

    # Display counts of gender
    print('** Counts of gender')
    try:
        print(df['Gender'].value_counts(),'\n')
        
    except KeyError as e:
        print('KeyError:{}'.format(e))

    # Display earliest, most recent, and most common year of birth
    try:
        birth_year = df['Birth Year']
        common_birth = birth_year.mode()[0]
        ealiest_birth = birth_year.min()
        most_recent_birth = birth_year.max()
        print('Most common year of birth is {} .'.format(common_birth))
        print('Ealist year of birth is {} .'.format(ealiest_birth))
        print('Most revent year of birth is {} .'.format(most_recent_birth))
        
    except KeyError as e:
        print('KeyError:{}'.format(e))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """Displays rows of data"""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no: ').lower()
    start_loc = 0
    
    while view_data == 'yes' and True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5 
        view_display = input("Do you wish to continue? Enter yes or no: ").lower()                  
        if view_display == 'no':
            break
            
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
