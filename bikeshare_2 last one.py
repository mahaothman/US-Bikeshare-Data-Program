import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.,
    
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        
        city = input("please type your city chicago , new york city or washington to start analyzing ")
        city = city.lower()
        if city in ['chicago','new york city','washington']:
            
            break
      
        else:
          print("Your input is invalid,please retype your city to analyze correctly.")
      

        
    # get user input for month (all, january, february, ... , june)
   
    
    
    while True:
         month = input('please type your month or all to analyze ')
         month = month.lower()
         if month in ['all','january','february','march','april','may','june']:
             break
         else:
            
           print ('your input is invalid .please retype your month to analyze correctly.')
   
           
    # get user input for day of week (all, monday, tuesday, ... sunday)
   
    
    while True :
        day = input('pleasy enter your day or type all to show your data. ')
        day = day.lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            
         print('your input is invalid , please retype your day to analyze correctly.')
        
       
    print('-'*40)
    return city, month,day


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

    df =pd.read_csv(CITY_DATA[city])
   
    df ['Start Time'] = pd.to_datetime(df['Start Time'])
    df ['month']= df['Start Time'].dt.month
    df ['day_of_week']= df['Start Time'].dt.day_name()
    
    if month!= 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month']== month]
        
    if day!= 'all':
       day= df[df['day_of_week']== day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month= df['month'].mode()[0]
    print('common_month :', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('common_day:' , common_day)

    # display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    common_start_time = df['hour'].mode()[0]
    print('common_start_time:', common_start_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most common start station is ", df['Start Station'].mode()[0])
    
    
    # display most commonly used end station
    print('most common end station is', df['End Station'].mode()[0])
    
    # display most frequent combination of start station and end station trip
    df['frequent']= df['End Station']+" " + df['Start Station']
    print('frequent combination of start and end station is' , df['frequent'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if 'Trip Duration' in df :
        
        print(" total_travel_time ", df['Trip Duration'].sum())
    else:
        print('can not be calculated')
        
    

    # display mean travel 
    
    if 'Trip Duration' in df :
    
       print("average_travel_time" , df['Trip Duration'].mean())
    else:
        print('can not be calculated')
            
       
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type'in df :
        user_types = df['User Type'].value_counts()
        print(user_types)
    else:
       print('user types can not be calculated')
       
    # Display counts of gender
    if 'Gender' in df :
       user_gender = df['Gender'].value_counts()
       print(user_gender)
    else:
       print('gender can not be calculated')
       
    # Display earliest, most recent, and most common year of
    
  
  
    if 'Birth Year' in df :
          earliest_year= df['Birth Year'].min()
          recent_year=  df['Birth Year'].max()
          most_common_year  = df['Birth Year'].mode()[0]

          print(earliest_year)
          print(recent_year)
          print(most_common_year)
        
    else:
        print('Birth Year can not be calculated')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    view_data=input('would you like to view 5 rows of individual trip data? Enter yes or no ')
    view_data= view_data.lower()
    start_loc = 0
    while True:
        
       # if view_data == 'yes':
           
          print(df.iloc[start_loc: start_loc +5])
          start_loc +=5
          view_data = input('more 5 raws ?').lower()
          if view_data =='no':
             break
            
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
