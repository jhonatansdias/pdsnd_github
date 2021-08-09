import time
import pandas as pd
import numpy as np


#This line include the first letter of the city name. The user can type full name of the city or only the first letter.
CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv', 'c': 'chicago.csv', 'n' : 'new_york_city.csv', 'w' : 'new_york_city.csv'}

def get_filters():
    
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # Create the dictionary for the cities
    city_dict = {'c':'chicago','n':'new york city','w':'washington','chicago':'chicago','new york city':'new york city','washington':'washington'}
    # Create the dictionary for the months
    month_dict = {'all':'all','january':'january','february':'february','march':'march','april':'april','may':'may','june':'june'}
    # Create the dictionary for the days
    day_dict = {'all':'all','monday':'monday','tuesday':'tuesday','wednesday':'wednesday','thursday':'thursday','friday':'friday',
                'saturday':'saturday','sunday':'sunday'}

    while True:
        city =input('Please choose one of the cities to start: \nChicago(C), New York(N), or Washington(W) \n\nEnter Name or letter: ').lower() # Request the name of the city for the user
        if city in city_dict: # Check if the city exist.
            
            city = city_dict.get(city) # This is user to take the full name of the city if user type just a letter.
            print('You have selected: {}'.format((city).capitalize())) #print the name of the city with the first letter capitalized
            break #Used to stop the while loop
        else:
            print('\nInvalid value! Please choose a valid city below') #if the city doesn't exist display this message
                          
    while True:
        month = input('\nWhich months would you like to filter?\ (All,January,February ..June)\nMonth: ').lower()   # Request the month for the user
        if month in month_dict: # Check if the month exist.
            month = month_dict.get(month) # This is user to take the full name of the month
            print('You have selected: {}\n'.format((month).capitalize()))#print the name of the month with the first letter capitalized
            break #Used to stop the while loop
        else:
            print('\n[Invalid value] You have to enter a valid month!') #if the month doesn't exist display this message
   
    while True:
        day = input('Which day of week would you like to see? (All, Monday, Tuesday, ... Sunday)\nDay: ').lower() # Request the day for the user
        if day in day_dict: # Check if the day exist.
            day = day_dict.get(day) # This is user to take the full name of the day.
            print('You have selected: {}'.format((day).capitalize()))#print the name of the day with the first letter capitalized
            break #Used to stop the while loop
        else:
            print('[Invalid value] You have not enter a valid day. Please choose one of them.') #if the day doesn't exist display this message

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
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month']==month]
        
    # filter by day of week if applicable
    if day != 'all':        
        # filter by day of week to create the new dataframe
        df = df = df[df['day_of_week'] == day.title()]    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(common_month))

    # TO DO: display the most common day of week
    common_week_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: {}'.format(common_week_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    frequent_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(frequent_start_station  ))

    # TO DO: display most commonly used end station
    frequent_end_station = df['End Station'].mode()[0]
    print('The most common End station is: {}'.format(frequent_end_station ))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most common frequent station is: {}'.format(frequent_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration_time = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_duration_time))

    # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print('The average travel time is: {}'.format(avg_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users when user chose Washington"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('\nThe counts for user types is: {}'.format(count_user_types))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*110)
  
def user_stats_gender_birth(df):
    """Displays statistics on bikeshare users when user chose Chicago ou New York City"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('\nThe counts for user types is: {}'.format(count_user_types))
    
    # TO DO: Display counts of gender
    count_gender = df['Gender'].value_counts()
    print('\nThe counts for gender is: {}'.format(count_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_yeah = df['Birth Year'].min()
    recent_yeah = df['Birth Year'].max()
    common_yeah = df['Birth Year'].mode()[0]
    print('The earliest year is {}, the recent is {} and the common year is {}'.format(earliest_yeah, recent_yeah, common_yeah))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*110)

def view_raw_data(df):
    
    """    Function is used to display the lines of the data.    """
    print(df.iloc[0:5]) #Print the first five(5) rows of the data
    print('-'*110) #  Used to print the character
    view_row = 0
    while True:
        view = input('\nWould you like to see the next five(5) row of raw data? Enter (yes or y) or press any key to skip.\n').lower() #Request the answer for the user
        if (view != 'yes') and (view != 'y'): #if the user doesn't want the see the next 5 rows, skip the print.
            print('View canceled by user') # Used to show a message for the user.
            return #Stop the loop
        view_row = view_row + 5 #Add five more lines for this variable.
        print('-'*110)
        print(df.iloc[view_row:view_row+5]) #Print the the next 5 row of raw data
        print('-'*110)

def close_program():
    # This function is used to show a final message for the user.
    print('Program closed....!')
    print('-'*20)
    print('\nBy: Jhonatan Dias')   
       
def main():
    while True:
        city, month, day = get_filters() 
        df = load_data(city, month, day)
        time_stats(df) #User to call the function
        station_stats(df) #User to call the function
        trip_duration_stats(df) #User to call the function

        if (city == 'new york city') or (city == 'chicago') :
            user_stats_gender_birth(df) #If user choose Chicago ou New York City call the function that have a all information about user stat
        else:
            user_stats(df) #If user choose Washington call the function and show only the User Type
            
        view_raw_data(df) # Call the function to show the rows of raw data 

        restart = input('Would you like to restart? Enter yes or press any key to exit.\n').lower() #Request the answer for the user
        if (restart != 'yes') and (restart != 'y'): #if the user doesn't want restart, close the program.
            close_program() # Call the function to close the program.
            break # Stop the loop.

if __name__ == "__main__":
	main()