import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def clean_data(user_name: str, data_frame: object) -> object:
    '''
        user_name: user name whose data you want to visualize
        data_frame: data in the form panda dataframe

        Extra columns are removed and the time is converted to proper format
        and returns the cleaned data
    '''
    # Extracting data for the given profile name
    data = data_frame[data_frame['Profile Name'] == user_name]
    data.reset_index(inplace=True)

    # Droping extra columns that will not be used
    columns_to_drop = ['Country', 'Bookmark', 'Latest Bookmark', 'index', 'Attributes']
    data = data.drop(columns=columns_to_drop)

    # Convert Start Time to datetime. Currently it is object
    data = data.rename(columns={'Start Time': 'Date'})
    data['Date'] = pd.to_datetime(data['Date'])

    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    data['day_of_week'] = data['Date'].dt.dayofweek
    data['day_name'] = data['Date'].dt.day_name()

    # Type of video like TRAILER, PROMOTIONAL, etc.
    data = data[data['Supplemental Video Type'].isna()]
    data[['TV Show', 'Season', 'Episode']] = data['Title'].str.split(':', expand=True, n=2)
    data['Content Type'] = data['Season'].apply(lambda x : 'Movie' if x is None else 'TV Show')
    data = data.rename(columns={'Temp': 'Content Type'})

    # Droping Supplemental Videos
    data = data.drop(columns='Supplemental Video Type')
    data['date_of_month'] = data['Date'].dt.day
    temporary_data = ['Profile Name', 'Date', 'date_of_month', 'day_of_week', 'day_name', 'Month', 'Year']
    temporary_data += ['Duration', 'Title', 'TV Show', 'Season', 'Episode', 'Content Type', 'Device Type']
    data = data[temporary_data]

    # Extract timestamp as a seperate column
    data['Start Time'] = data['Date'].apply(lambda x : str(x).split('+')[0].split(' ')[1])
    data['Date'] = pd.to_datetime(data['Date'])
    data['Date'] = data['Date'].dt.date
    data.set_index('Date', inplace=True)

    # Convert duration HH:MM:SS to number of minutes
    data['Duration'] = data['Duration'].str.split(':').apply(lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]))

    return data


def average_time_spent_per_day(data: object) -> None:
    '''
        data: cleaned data

        Extracts the average time spent on each day
    '''

    avg_second_per_day = data.groupby('day_name')['Duration'].mean().sort_values()
    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sns.set_style("darkgrid")

    font = {'family': 'serif',
            'color': '#004466',
            'weight': 'normal',
            'size': 18}

    plt.figure(figsize=(20, 15))
    ax = sns.barplot(x=avg_second_per_day.index, y=avg_second_per_day.values, palette=("crest_r"), order=day_of_week)
    ax.set_ylabel('Viewing Duration (in Seconds)', fontdict={'size': 14, 'family': 'serif'})
    ax.set_xlabel('Day of Week', fontdict={'size': 14, 'family': 'serif'})
    ax.set_title('Average Viewing Time per Day (in seconds)', fontdict=font)
    ax.tick_params(axis='both', labelsize=13)
    plt.show()


def top_watched_TV_show(data: object) -> object:
    '''
        data: cleaned data

        Extracts the TV Shows and calculate the total time spent on each TV Show
        and returns the data of only tv_shows
    '''

    tv_shows = data[data['Content Type'] == 'TV Show']
    tv_shows[tv_shows['Episode'].isna()]
    tv_shows['Title'].nunique()
    order_tv_shows = tv_shows.groupby('TV Show')['Duration']
    most_watched = order_tv_shows.mean().reset_index().sort_values(by='Duration', ascending=False)

    font = {'family': 'serif',
            'color': '#004466',
            'weight': 'normal',
            'size': 18}

    plt.figure(figsize=(22, 12))
    ax = sns.barplot(y=most_watched['TV Show'][:10], x=most_watched['Duration'][:10], palette=("winter"))
    ax.set_ylabel('TV Series', fontdict={'size': 14, 'family': 'serif'})
    ax.set_xlabel('Watch Time (in seconds)', fontdict={'size': 14, 'family': 'serif'})
    ax.set_title('Top 10 TV Shows by Average Duration (seconds)', fontdict=font)
    ax.tick_params(axis='both', labelsize=13)

    return tv_shows


def binge_watch(tv_shows: object) -> None:
    '''
        tv_shows: data of tv_shows

        Extract top binge watched TV Shows
    '''

    binge = tv_shows.groupby([tv_shows.index, 'TV Show'])
    binge = binge['Episode'].count().reset_index().sort_values(by='Episode', ascending=False)
    binge = binge[binge['Episode'] > 5]
    top_10_binge = binge.groupby('TV Show')['Episode'].sum().reset_index().sort_values(by='Episode', ascending=False)

    font = {'family': 'serif',
            'color': '#004466',
            'weight': 'normal',
            'size': 18}

    plt.figure(figsize=(22, 12))
    ax = sns.barplot(y=top_10_binge['TV Show'][:10], x=top_10_binge['Episode'][:10], orient='h', ci='None')
    ax.set_ylabel('TV Series', fontdict={'size': 14, 'family': 'serif'})
    ax.set_xlabel('Number of Episodes', fontdict={'size': 14, 'family': 'serif'})
    ax.set_title('Top 10 Binge Watching TV Series', fontdict=font)
    ax.tick_params(axis='both', labelsize=13)


def average_time_spent_per_month(data: object) -> None:
    '''
        data: cleaned data

        Extact the average time spent per month
    '''

    font = {'family': 'serif',
            'color': '#004466',
            'weight': 'normal',
            'size': 18}

    # Each row is a data point in boxplot and plots the distribution (histogram) of Watch Time for each month
    plt.figure(figsize=(20, 10))
    ax = sns.boxplot(x=data['Month'], y=data['Duration'])
    ax.set_ylabel('Watch Time (Seconds)', fontdict={'size': 14, 'family': 'serif'})
    ax.set_xlabel('Month', fontdict={'size': 14, 'family': 'serif'})
    ax.set_title('Distribution of Duration (Seconds) over the months', fontdict=font)
    ax.tick_params(axis='both', labelsize=13)
    plt.show()


def main():
    user_name = '153'
    data_frame = pd.read_csv('ViewingActivity.csv')
    final_data = clean_data(user_name, data_frame)

    average_time_spent_per_day(final_data)
    tv_shows_data = top_watched_TV_show(final_data)
    binge_watch(tv_shows_data)
    average_time_spent_per_month(final_data)


if __name__ == '__main__':
    main()
