# Imports
import fire
import pandas as pd
import matplotlib.pyplot as plt

# Global variables
Path = 'data/covid_data.csv'

def return_dataframe():
    # CSV into dataframe
    dataframe = pd.read_csv(Path, sep=',')
    
    # Return dataframe
    return dataframe

def country_data(country,df_country,plot,cases,deaths,raw):
    # Set xticks in plot
    plot.set_xticks(range(0,len(df_country),30))

    # Check if dataframe is empty
    if not df_country.empty:

        if raw:
            cases_list = df_country['New_cases']
            deaths_list = df_country['New_deaths']

        else:
            df_cases = df_country[['Date_reported','New_cases','New_deaths']]
            rolling = df_cases.rolling(window=7)
            rolling_mean = rolling.mean()

            cases_list = rolling_mean['New_cases']
            deaths_list = rolling_mean['New_deaths']

        # Plot cases
        if cases:
            plot.plot(
                df_country['Date_reported'],
                cases_list,
                label='{country_name}: Cases'.format(country_name=country)
                )

        # Plot deaths
        if deaths:
            plot.plot(
                df_country['Date_reported'],
                deaths_list,
                label='{country_name}: Deaths'.format(country_name=country)
                )

    # Error Message
    else:
        print('{} was not found.'.format(country))

def compare_countrys(*args, cases=True, deaths=True, raw=False):
    # Data from CSV
    df = return_dataframe()

    # Convert arguments to list
    list_of_countrys = list(args)

    # Generate figure and plot
    fig, ax1 = plt.subplots(1)

    # Set title, x-axe, y-axe
    fig.suptitle('Covid-19 Model')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Humans')

    # Iterate country list
    for country in list_of_countrys:

        # Get country data from dataframe
        df_country = df[df['Country'].str.fullmatch(country)]

        country_data(country,df_country,ax1,cases,deaths,raw)

    # Show legend, plot
    plt.legend()
    plt.show()

def list_countrys():
    df = return_dataframe()

    countrys = []

    for country_name in df['Country']:
        if not country_name in countrys:
            print(country_name)
            countrys.append(country_name)