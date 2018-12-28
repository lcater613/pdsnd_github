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


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    city = input('would you like to see data for chicago, new york city or washington?').lower()
    while True:
        if city not in ('chicago', 'new york city', 'washington'):
            print('invalid input, please try again')
            city = input('would you like to see data for chicago, new york city or washington?').lower()
        else:
            print('you have selected', city)
            break
    month = input('Which month would you like to see data for? Please select a month between January and June, or type all.').lower()
    while True:
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('invalid input, please try again.')
            month = input('Which month would you like to see data for? Please select a month between January and June, or type all.').lower()
        else:
            print('you have selected', month)
            break

    day = input('Which day would you like to see data for? Please select a day of the week, or type all.').lower()
    while True:
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('invalid input, please try again.')
            day = input('Which day would you like to see data for? Please select a day of the week, or type all.').lower()
        else:
           print('you have selected', day)
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month] 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()] 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    busiest_month= df['month'].mode()[0]
    print('the most common month was', busiest_month)

    # TO DO: display the most common day of week
    busiest_day = df['day_of_week'].mode()[0]
    print('the most common day was', busiest_day)

    # TO DO: display the most common start hour
    busiest_start_hour = df['Start Time'].mode()[0]
    print('the most common start time was', busiest_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('the most popular start station was', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('the most popular ending station was', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start Plus End'] = df['Start Station'].map(str) + ' & ' + df['End Station']
    popular_start_end = df['Start Plus End'].value_counts().idxmax()
    print('the most common start station and end station combination is', popular_start_end)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time was', total_travel_time)
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('the average travel time was', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_of_user = df['User Type'].value_counts()
    print(type_of_user)

    # TO DO: Display counts of gender
   
    if 'Gender' in df.columns:
        gender_total = df['Gender'].value_counts()
        print(gender_total)
    else:
        print('Sorry, there is no gender data available for this region.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthday = df['Birth Year'].min()
        print('The earliest birthday was', earliest_birthday)
        most_recent_birthday = df['Birth Year'].max()
        print('The most recent birthday was', most_recent_birthday)
        most_common_birth_year = df['Birth Year'].mode().dropna()
        print('The most common birth year was', most_common_birth_year)       
    else:
        print('Sorry, there is no birthday information available for this region.')

    raw_user_data = input('would you like to see raw user data? Please select yes or no.').lower()
    while True:
            if raw_user_data == 'yes':
                print(df.sample(5))
                raw_user_data = input('would you like to see more raw user data? Type yes for more data.').lower()
            else:
                print('input received.')
                break

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
