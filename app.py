"""
Module: projet.py

Description: This module contains code for an application that analyzes population data.
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def display_welcome_message():
    """Displays a welcome message."""
    st.write(
        """
        This app presents Louis Wiart's project in advanced python. Here, you will find an extract 
        of the database and a plot about the evolution of China's population.
        """
    )


def get_countries(df_population):
    """Returns a list of countries from the given dataframe."""
    return sorted(df_population['Country/Territory'].unique().tolist())[:234]


def display_data():
    """Displays data for the selected country or all data."""
    df_population = pd.read_csv('world_population.csv', encoding="ISO-8859-1")
    users_list = ['All'] + get_countries(df_population)
    selected_country = st.selectbox('Choose a Country', users_list)

    if selected_country == 'All':
        st.write('You want to see all data')
        st.write(df_population.head(234))
    else:
        st.write(f'You selected {selected_country}')
        pop_country = df_population[df_population['Country/Territory'] == selected_country]
        st.write(pop_country)


def display_population_plot():
    """Displays a graph on the evolution of population in China."""
    world_pop = pd.read_csv('world_population.csv', encoding="ISO-8859-1")
    china_data = world_pop[world_pop['Country/Territory'] == 'China']

    years = ['1970 Population', '1980 Population', '1990 Population',
             '2000 Population', '2010 Population', '2022 Population']
    populations_china = china_data[years].values[0]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(years, populations_china, marker='o', linestyle='-', color='red')
    ax.set_title('Evolution of population in China over time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')

    st.pyplot(fig)


def run_application():
    """Main function of the application."""
    st.title("My project")
    st.header("Evolution of Population in the world")
    st.subheader("This application is made by Louis Wiart")
    st.sidebar.title("Navigation")

    menu_action = st.sidebar.selectbox(
        "Choose a menu", ['Home', 'Database', 'Plot'])

    if menu_action == 'Home':
        display_welcome_message()
    elif menu_action == 'Database':
        display_data()
    elif menu_action == 'Plot':
        display_population_plot()
    else:
        st.write('Error: selection invalid')


if __name__ == '__main__':
    run_application()
