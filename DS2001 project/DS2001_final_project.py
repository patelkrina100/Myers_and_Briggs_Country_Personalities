#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:48:47 2021

@author: jane & krina & diana
"""

import csv
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression
# Note: pers abbreviates for personality

"""
Background Info:
Myers and Briggs theorized that our preferences on each of the four dimensions 
would combine to create predictable patterns in thought and behavior, so that 
people with the same four preferences would share many commonalities in the 
way they approach their lives, from the hobbies they choose to the work that 
might suit them. 
Each of the four dimensions was described as a an either/or choice between two 
styles of being. The sum of a person's four preferred styles becomes their 
personality type.

I/E: Introverts are energized by spending quiet time alone or with a 
     small group. Extraverts are energized by spending time with people and in 
     busy, active surroundings. 
S/N: Sensors focus on their five senses and are interested in information they 
     can directly see, hear, feel, and so on. Intuitives focus on a more 
     abstract level of thinking; they are more interested in theories, 
     patterns, and explanations. 
T/F: Thinkers are interested in finding the most logical, reasonable choice.
     Feelers are interested in how a decision will affect people, and whether 
     it fits in with their values.
J/P: Judgers appreciate structure and order; they like things planned, and 
     dislike last-minute changes. Perceivers appreciate flexibility and 
     spontaneity; they like to leave things open so they can change their 
     minds.

Question: Which personality type is most common in the “best” countries? 
          What personality is the least common in the “best countries”? 
          Is there any correlation with their average Gross National 
          Income(GNI) per capita?”

This is an interesting question because looking at society and how different 
people come to work in different jobs and the money they earn because of their 
individuality is critical to how our society functions. There are 16 different 
personality traits according to Myers-Briggs and each of the types are said to 
be commonly associated with different personal strengths and weaknesses. 
Different countries have different percentages of personality types that may 
play a part in their average income. By analyzing different countries and what 
their overall strengths and weaknesses are, we can make better conclusions and 
predictions about other countries’ stability and overall strength. 
"""

"""
We used the dataset, country v MBTI (PERSONALITY_FILE) personality comparing 
the percentage of the population belonging to each MBTI type, with each 
country in the world.We found this data on Kaggle, and used it to find the 
most common and least common personality traits in each of the top 10 
countries in the world. We also used the data to analyze each personality type 
in a visual representation for each country.
"""
PERSONALITY_FILE = "country_personality_types.csv"

"""
We used the dataset, Country v GNI per Capita, comparing the a country’s final 
income per year, divided by the population for the years 1990-2018. By finding 
the average of this data, we were able to assign a definite average GNI per 
capita for each country to use for a comparison with our personality data. 
We also found this data on Kaggle, and calculated the average GNI per capita 
for each of the top 10 countries, as well as made a visual comparing their 
average incomes in a bar graph. 
"""
GNI_FILE = "GNI_per_capita.csv"

def read_in_file(filename):
    """
    Read in file and return a nested lst.
    
    Parameters 
    ---
    filename: str
        Name of the file.
    
    Returns
    ---
    file_lines: 2d_lst 
        Nested lst of the lst of the data for each country.
    """
    # Create an empty lst 
    file_lines = []
    
    # Open the file and read in the file 
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        
        # Iterate over each row in the csv_reader and append 
        # the row to the lst 
        for row in csv_reader:
            file_lines.append(row)
        
    return file_lines

def get_header_lst(nested_lst):
    """
    Pop off the lst with the headers from the nested_lst and return it as a 
    separate lst.
    
    Parameters
    ---
    nested_lst: 2d_lst 
        A nested_lst of the data. 
    
    Returns
    ---
    header_lst: lst
        A lst of the headers for each column of the data. 
    """
    # Iterate over each row of the nested_lst as an index and set header lst 
    # as the index 0 of the lst in the nested_lst 
    for row in range(len(nested_lst)):
        header_lst = nested_lst[0]
        
    return header_lst

def get_specific_country(nested_lst, country_name):
    """
    Get the lst for the GNI per capita for specific country.
    
    Parameters
    ---
    nested_lst: 2d_lst
        A nested lst of the data for each country. 
        
    country_name: str
        Name of the country. 
    """
    # Create an empty lst 
    lst_for_country = []
    
    # Iterate over each row in the nested lst 
    for row in nested_lst:
        
        # Iterate over the data in reach row to check to see the country_name 
        # wanted is in row, if it is, set the row as lst_for_country
        for data in row:
            if country_name in data:
                lst_for_country = row 
                
    # Iterate over each index in the lst_for_country and check to see if the
    # index is '', if it is then pop it from the lst.  
    for indx in range(len(lst_for_country)):
        if lst_for_country[indx] == '':
            lst_for_country.pop(indx)
    
    return lst_for_country

def make_dctn(lst_of_data):
    """
    Convert the lst for each country into a dictionary for the country. The
    key of the dictionary is the country's name and the value is the GNI per
    capita from years 1990-2018.
    
    Parameters
    ---
    lst_of_data: lst
        A lst of data. 
    
    Returns
    ---
    data_dctn: dictionary 
        A dicitonary of the data. 
    """
    # Create an empty dictionary 
    data_dctn = {}
    
    name = lst_of_data[0]
    data = lst_of_data[1:]
        
    data_dctn[name] = data
        
    return data_dctn

def calc_average_gni(data_dctn):
    """
    Calculate the average GNI per capita for GNI per capita from years 
    1990-2018 for each country's dictionary.
    
    Parameters
    ---
    data_dctn: 
        A dictionary of data.
        
    Returns
    ---
    round(average_gni, 4): float
        The rounded average_gni value. 
    """
    # Create an empty lst
    int_gni_lst = []
    
    # Iterate over the key and value in the data_dctn.items and set each value 
    # as gni_lst
    for key, value in data_dctn.items():
        gni_lst = value
    
    # Iterate over each item in gni_lst
    for items in gni_lst:
        # Convert each item into an integer
        gni = int(items)
        # Add the integer form of the gni into the lst
        int_gni_lst.append(gni)
    
    # Calculate average_gni by dividing the sum of all the integers in the 
    # lst by the length of the lst
    average_gni = sum(i for i in int_gni_lst) / len(int_gni_lst)
    
    return round(average_gni, 4) 

def combine_into_lst(avg_1, avg_2, avg_3, avg_4, avg_5, avg_6, avg_7, avg_8,
                   avg_9, avg_10):
    """
    Add the 10 average GNIs per capita into a lst. 

    Parameters
    ----------
    avg_1 : float
        An average GNI per capita value.
    avg_2 : float
        An average GNI per capita value.
    avg_3 : float
        An average GNI per capita value.
    avg_4 : float
        An average GNI per capita value.
    avg_5 : float
        An average GNI per capita value.
    avg_6 : float
        An average GNI per capita value.
    avg_7 : float
        An average GNI per capita value.
    avg_8 : float
        An average GNI per capita value.
    avg_9 : float
        An average GNI per capita value.
    avg_10 : float
        An average GNI per capita value.

    Returns
    -------
    lst of values: lst
        A lst of all the values in the parameter.
    """
    # Create an empty lst
    lst_of_values = []
    
    # Add each item to lst 
    lst_of_values.append(avg_1)
    lst_of_values.append(avg_2)
    lst_of_values.append(avg_3)
    lst_of_values.append(avg_4)
    lst_of_values.append(avg_5)
    lst_of_values.append(avg_6)
    lst_of_values.append(avg_7)
    lst_of_values.append(avg_8)
    lst_of_values.append(avg_9)
    lst_of_values.append(avg_10)
                                           
    return lst_of_values 
    
def combine_into_nested_lst(percentages_lst):
    """
    Convert a list into a nested list that looks like:
        [[0.1275], [0.1291], [0.1436]...]
        
    Parameters
    ---
    percentages_lst: List
        List of percentages.
    
    Returns
    ---
    nested_percentages_lst: 2d_list
        List of list of percentages.
    
    """
    # Create a empty list
    nested_percentages_lst = []
    
    # Iterate over each percentage in the list and make each percentage its 
    # own list and then append it to the bigger list
    for percentages in percentages_lst:
        nested_percentages_lst.append([percentages])
        
    return nested_percentages_lst

def make_country_gni_dctn(lst_of_countries, lst_of_avg_gni):
    """
    Load the 2 lsts defined in the parameters, and create a lst of dicts 
    where each dict has the following format: 
        {'country': 'Canada', 'average_gni': 37334.2759} 
    
    Paramters
    ---
    lst_of_countries: lst 
        A lst of the countries.
    lst_of_avg_gni: lst 
        A lst of the avergae GNI per capita for each country.
        
    Returns
    ---
    all_lst: lst
        A lst of all the dictionaries.
    """
    # Create an empty lst 
    all_lst = []
    
    # Iterate over each index in the lst 
    for i in range(len(lst_of_countries)):
        # Create an empty dicitonary 
        this_dict = {}
        
        # Make a new key "Country" and set its values as the countries in the 
        # lst of countries
        this_dict["Country"] = lst_of_countries[i]
        
        # Make the new key "Average_GNI" and set its value as the average GNIs 
        # per capita in the lst of average GNI per capita.
        this_dict["Average_GNI"] = lst_of_avg_gni[i]
        
        # Add this dictionary into the lst
        all_lst.append(this_dict)
        
    return all_lst 

def compare_gni_value(lst_of_dict):
    """
    Compare the avgerage GNI per capita values for each country to determine 
    which countries has the highest and lowest average GNIs per capita.

    Parameters
    ----------
    lst_of_dict : lst 
        A lst of dictionaries that has the country name and avergae GNI per 
        capita.

    Returns
    -------
    highest_avg_gni : float 
        The highest average GNI per capita.
    high_country : str
        The country with the highest avergae GNI per capita.
    lowest_avg_gni : float
        The lowest average GNI per capita.
    low_country : str
        The country with the lowest average GNI per capita.
    """
    # Set initial variables and their initial values 
    highest_avg_gni = 0
    lowest_avg_gni = 1000000000
    
    # Iteratve over each gni_valuesd_dctn in the list of dictionaries and 
    # check to see if the value of the key "Average_GNI" is greater than the 
    # value of the highest_avg_gni, if it is set that value as the 
    # highest_avg_gni. Then find the country that the highest_avg_gni
    # corresponds to.
    for gni_values_dctn in lst_of_dict:
        if gni_values_dctn["Average_GNI"] > highest_avg_gni:
            highest_avg_gni = gni_values_dctn["Average_GNI"]
    
    for gni_values_dctn in lst_of_dict:
        if highest_avg_gni == gni_values_dctn["Average_GNI"]:
            high_country = gni_values_dctn["Country"]
            
    # Iteratve over each gni_valuesd_dctn in the list of dictionaries and 
    # check to see if the value of the key "Average_GNI" is lower than the 
    # value of the highest_avg_gni, if it is set that value as the 
    # lowest_avg_gni. Then find the country that the lowest_avg_gni 
    # corresponds to.
    for gni_values_dctn in lst_of_dict: 
        if gni_values_dctn["Average_GNI"] < lowest_avg_gni:
            lowest_avg_gni = gni_values_dctn["Average_GNI"] 
            
    for gni_values_dctn in lst_of_dict:
        if lowest_avg_gni == gni_values_dctn["Average_GNI"]:
            low_country = gni_values_dctn["Country"]
            
    return highest_avg_gni, high_country, lowest_avg_gni, low_country

def compare_pers_value(personality_lst):
    """
    Compare the personality values 

    Parameters
    ----------
    personality_lst : lst 
        lst of the percentage of the personalities for each country.

    Returns
    -------
    highest_personality : float
        Highest percentage personality.
    lowest_personality : float
        Lowest percentage personality.
    """
    # Set initial variables and their initial values 
    highest_personality = 0.0000
    lowest_personality = 1000000.000
    
    # Remove name of country to compare percentages as integers
    personality_lst.pop(0)
    
    # Loop through lst and convert everything to floats 
    for i in range(len(personality_lst)):
        personality_lst[i]= float(personality_lst[i])
        
    # Find highest and lowest percentages from personality lst 
    for percentage in personality_lst:
        if percentage > highest_personality: 
            highest_personality = percentage
            
        if percentage < lowest_personality:
            lowest_personality = percentage
            
    return highest_personality, lowest_personality

def pers_headers(pers_lst, pers_header, highest_pers, lowest_pers):
    """
    Find the name of the most commmon and least common personalities for each
    country.

    Parameters
    ----------
    pers_lst : list
        List of personality percentages for each country.
    pers_header : list
        List of personality type names. 
    highest_pers : float
        Percentage of the most common personality type.
    lowest_pers : float
        Percentage of the least common personality type. 

    Returns
    -------
    highest_pers_type : str
        The personality type of the most common personality percentage.
    lowest_pers_type : str
        The personality type of the least common personality percentage.
    """
    # Initialize variable index 
    highest_pers_type_column= 0
    lowest_pers_type_column = 0
    
    # Initialize the variables of the personality types for the most and least 
    # common personalities.
    highest_pers_type = ''
    lowest_pers_type = ''
    
    # Iterate over each index in in the pers_lst 
    # Find column numbers for highest and lowest personality %
    # Add 1 to cancel the "country" object in the row
    for i in range(len(pers_lst)):
        if pers_lst[i] == highest_pers:
            highest_pers_type_column = i+1
            highest_pers_type = pers_header[highest_pers_type_column]
                   
        if pers_lst[i] == lowest_pers: 
            lowest_pers_type_column = i+1
            lowest_pers_type = pers_header[lowest_pers_type_column]
    
    return highest_pers_type, lowest_pers_type

def print_gni_data(country_name, average_gni):
    """
    Print the gni_data in the specific format.

    Parameters
    ----------
    country_name : str
        Name of country. 
    average_gni : float
        Average_gni per capita value for each country. 

    Returns
    -------
    None.
    """
    print("The average GNI per capita for {} is ${}."
          .format(country_name, average_gni))
    
    return 

def print_pers_data(highest_pers_type, highest_pers, 
                           lowest_pers_type, lowest_pers):  
    """
    Print the statements for most common and least common personalities. 

    Parameters
    ----------
    highest_pers_type : str
        The personality type of the most common personality.
    highest_pers : float
        The percentage of the most common personality. 
    lowest_pers_type : str
        The personality type of the most common personality. 
    lowest_pers : float
        The percentage of the least common personality.

    Returns
    -------
    None.
    """
    print("The most common personality type is {} with a percentage of {}."
          .format(highest_pers_type, round(highest_pers, 4)))
    print("The least common personality type is {} with a percentage of {}."
          .format(lowest_pers_type, round(lowest_pers, 4)))
       
    return  
    
def graph_bar_graph_pers(countries, personality_header, 
                         personality_percentages):
    """
    Plot the bar graphs for each personality percentages and types for each 
    country. 
    
    Parameters
    ---
    countries: list 
        List of countries.
    personality_header: list
        List of the headings for each column for the PERSONALITY_FILE.
    personality_percentages: list
        List of personality percentages for each personality type.   
        
    Returens
    ---
    None.
    """
    # Make list of personality types without header
    personality_type = personality_header[1:]
    
    # Loop through the percentages of personality types 32 times
    # convert to float
    for index in range(len(personality_percentages)):
        personality_percentages[index]= float(personality_percentages[index])
    
    # Build an array for the x-axis; 32 personality types on x-axis
    personality_type_axis = np.arange(len(personality_type))
    
    # Plot graph
    plt.bar(personality_type_axis, personality_percentages, -0.7, 
            color=("orange", "red", "pink"))
     
    plt.xticks(personality_type_axis, personality_type, rotation=90)
    plt.xticks(fontsize=7,color='black')
    plt.yticks(fontsize=8,color='black')
    plt.xlabel("Personality Types")
    plt.ylabel("Percentages")
    plt.title("Personality Distribution in {}".format(countries))
    plt.show()
  
    return

def graph_bar_gni_data(countries_lst, lst_of_avg_gni):
    """
    Plot a bar graph for the countries in the countries_lst with the height of 
    the bars being the average GNI per capita for each country.

    Parameters
    ----------
    countries_lst : list
        List of countries.
    lst_of_avg_gni : TYPE
        List of average GNI per capita values.

    Returns
    -------
    None.
    """
    # Create variable names for each parameter.
    countries = countries_lst
    average_gni = lst_of_avg_gni

    # Plot graph 
    plt.bar(countries, average_gni, color="green")
    plt.xticks(rotation=45)
    plt.title("Average GNI per capita for each Country")
    plt.xlabel("Countries")
    plt.ylabel("Average GNI per capita ($)") 
    
    # Save graph 
    plt.savefig("1.png", bbox_inches='tight')
    plt.show()
    
    return

def graph_regression(x_lst, y_lst):
    """
    Make a linearRegression graph to find if there is any correlation between 
    the percentage of INFP-T (most common personality) in each country and the 
    average Gross National Income per capita in each country.

    Parameters
    ----------
    x_lst : 2d_list
        List of list of x-values
    y_lst : list
        List of y-values

    Returns
    -------
    None.

    """
    # Create the y and X variables 
    y = y_lst
    X = x_lst
    # x needs to be a list of list 
    
    # Use the LinearRegression object 
    lr = LinearRegression()
    
    # Create the linearRegression model
    model = lr.fit(X, y)
    print("Linear Correlation Coefficient: ",  model.coef_)  
    
    # Create a insample prediction model 
    insample_pred = model.predict(X)
    
    # Plot outputs
    plt.scatter(X, y, color="orange")
    plt.plot(X, insample_pred, color="purple", linewidth=3)
    plt.title("INFP-T Personality % VS GNI per Capita Regression")
    plt.xlabel("Personality (%)")
    plt.ylabel("GNI per capita ($)")
    plt.show()

    return 

def print_country_name(country_name):
    """
    Print the country name in the specified format.
    
    Parameters
    ---
    country_name: str
        Name of the country.
    
    Returns
    ---
    None.
    """
    print("\n{}:".format(country_name))
    
def main():
    """
    According to the US news, these are the top 10 countries in the world:
        Canada, Japan, Germany, Switzerland, Australia, United States, 
        New Zealand, United Kingdom, Sweden, and Netherlands. 
    This is according to agility, entrepreneurship, quality of life, movers, 
    social purpose, cultural influence, open for business, power, adventure, 
    and heritage.
    """
    countries_lst = ["Canada", "Japan", "Germany", "Switzerland", 
                      "Australia", "United States", "New Zealand", 
                      "United Kingdom", "Sweden", "Netherlands"] 
    
    # These are the abbreviations used for each of the 10 countries:
        # Canada - ca, Japan - jp, Germany - ge, Switzerland - sw, 
        # Australia - au, United States - us, New Zealand - nz, 
        # United Kingdom - uk, Sweden - se, Netherlands - nl
  
    # Read in the file of the GNI per capita of each country from 
    # years 1990-2018 as a nested lst.
    gni_nested_lst = read_in_file(GNI_FILE)
    
    # Seperate the nested of the GNI per capita into a lst for each
    # of the 10 countries. 
    ca_gni = get_specific_country(gni_nested_lst, "Canada") 
    jp_gni = get_specific_country(gni_nested_lst, "Japan")
    ge_gni = get_specific_country(gni_nested_lst, "Germany")
    sw_gni = get_specific_country(gni_nested_lst, "Switzerland")
    au_gni = get_specific_country(gni_nested_lst, "Australia")
    us_gni = get_specific_country(gni_nested_lst, "United States")
    nz_gni = get_specific_country(gni_nested_lst, "New Zealand")
    uk_gni = get_specific_country(gni_nested_lst, "United Kingdom")
    se_gni = get_specific_country(gni_nested_lst, "Sweden")
    nl_gni = get_specific_country(gni_nested_lst, "Netherlands")
    
    # Convert the GNI per capita for each country into a dictionary.
    ca_dctn = make_dctn(ca_gni)
    jp_dctn = make_dctn(jp_gni)
    ge_dctn = make_dctn(ge_gni)
    sw_dctn = make_dctn(sw_gni)
    au_dctn = make_dctn(au_gni)
    us_dctn = make_dctn(us_gni)
    nz_dctn = make_dctn(nz_gni)
    uk_dctn = make_dctn(uk_gni)
    se_dctn = make_dctn(se_gni)
    nl_dctn = make_dctn(nl_gni) 
    
    # Calculate the avergae GNI per capita from years 1990-2018 for each 
    # country. 
    ca_average_gni = calc_average_gni(ca_dctn)
    jp_average_gni = calc_average_gni(jp_dctn)
    ge_average_gni = calc_average_gni(ge_dctn)
    sw_average_gni = calc_average_gni(sw_dctn)
    au_average_gni = calc_average_gni(au_dctn)
    us_average_gni = calc_average_gni(us_dctn)
    nz_average_gni = calc_average_gni(nz_dctn)
    uk_average_gni = calc_average_gni(uk_dctn)
    se_average_gni = calc_average_gni(se_dctn)
    nl_average_gni = calc_average_gni(nl_dctn)
    
    # Print the avergae GNI per capita for each country
    print("Here are the average GNI per capita for each country...")
    print("------------------------")
    print_gni_data("Canada", round(ca_average_gni, 2))
    print_gni_data("Japan", round(jp_average_gni, 2))
    print_gni_data("Germany", round(ge_average_gni, 2))
    print_gni_data("Switzerland", round(sw_average_gni, 2))
    print_gni_data("Australia", round(au_average_gni, 2))
    print_gni_data("United States", round(us_average_gni, 2))
    print_gni_data("New Zealand", round(nz_average_gni, 2))
    print_gni_data("United Kingdom", round(uk_average_gni, 2))
    print_gni_data("Sweden", round(se_average_gni, 2))
    print_gni_data("Netherlands", round(nl_average_gni, 2))
    
    # Make the avg gni per capita for each country into a list.
    lst_of_avg_gni = combine_into_lst(ca_average_gni, jp_average_gni, 
                                  ge_average_gni, sw_average_gni,
                                  au_average_gni, us_average_gni, 
                                  nz_average_gni, uk_average_gni, 
                                  se_average_gni, nl_average_gni)
     
    # Make a lst of dictionary of the country and the avg_gni
    country_and_agv_gni_lst = make_country_gni_dctn(countries_lst, 
                                                     lst_of_avg_gni)
    
    # Compare the values in the lst_of_avg_gni to find the value of the 
    # highest avg GNI per capita and its corresponding country and find the 
    # value of the lowest avg GNI per capita and its corresponding country. 
    top_avg_gni, top_country, lowest_avg_gni, low_country = compare_gni_value(
        country_and_agv_gni_lst)
    
    print("\nThese are the highest and lowest GNI per capita...")
    print("------------------------")
    print("The highest average GNI per capita is ${} from {}."
          .format(round(top_avg_gni, 2), top_country))
    print("The lowest average GNI per capita is ${} from {}."
          .format(round(lowest_avg_gni, 2), low_country))
    
    # Read in the file of the distribution of each personality type in 
    # each country from PERSONALITY_FILE. 
    pers_nested_lst = read_in_file(PERSONALITY_FILE) 
    
    # Get the header_lst from personality_nested_lst
    pers_header = get_header_lst(pers_nested_lst)

    # Get the personality_types lst for each of the 10 specific countries 
    # in the countries lst
    ca_pers_lst = get_specific_country(pers_nested_lst, "Canada") 
    jp_pers_lst = get_specific_country(pers_nested_lst, "Japan")
    ge_pers_lst = get_specific_country(pers_nested_lst, "Germany")
    sw_pers_lst = get_specific_country(pers_nested_lst, "Switzerland")
    au_pers_lst = get_specific_country(pers_nested_lst, "Australia")
    us_pers_lst = get_specific_country(pers_nested_lst, "United States")
    nz_pers_lst = get_specific_country(pers_nested_lst, "New Zealand")
    uk_pers_lst = get_specific_country(pers_nested_lst, "United Kingdom")
    se_pers_lst = get_specific_country(pers_nested_lst, "Sweden")
    nl_pers_lst = get_specific_country(pers_nested_lst, "Netherlands")
    
    # Get highest and lowest personality percentage values for each of 
    # the 10 countries and then find the matching personality types (headers) 
    # for each country to determine most common and least common personality 
    # types for each of the 10 countries.
    
    # Canada
    ca_highest_pers, ca_lowest_pers = compare_pers_value(ca_pers_lst)
    ca_highest_pers_type, ca_lowest_pers_type = pers_headers(ca_pers_lst, 
                                                             pers_header, 
                                                             ca_highest_pers, 
                                                             ca_lowest_pers)
    
    # Japan 
    jp_highest_pers, jp_lowest_pers = compare_pers_value(jp_pers_lst)
    jp_highest_pers_type, jp_lowest_pers_type = pers_headers(jp_pers_lst, 
                                                             pers_header, 
                                                             jp_highest_pers, 
                                                             jp_lowest_pers)
    
    # Germany 
    ge_highest_pers, ge_lowest_pers = compare_pers_value(ge_pers_lst)
    ge_highest_pers_type, ge_lowest_pers_type = pers_headers(ge_pers_lst, 
                                                             pers_header, 
                                                             ge_highest_pers, 
                                                             ge_lowest_pers)
    
    # Switzerland
    sw_highest_pers, sw_lowest_pers = compare_pers_value(sw_pers_lst)
    sw_highest_pers_type, sw_lowest_pers_type = pers_headers(sw_pers_lst, 
                                                             pers_header, 
                                                             sw_highest_pers, 
                                                             sw_lowest_pers)
    
    # Australia
    au_highest_pers, au_lowest_pers = compare_pers_value(au_pers_lst)
    au_highest_pers_type, au_lowest_pers_type = pers_headers(au_pers_lst, 
                                                             pers_header, 
                                                             au_highest_pers, 
                                                             au_lowest_pers)
    
    # United States 
    us_highest_pers, us_lowest_pers = compare_pers_value(us_pers_lst)
    us_highest_pers_type, us_lowest_pers_type = pers_headers(us_pers_lst, 
                                                             pers_header, 
                                                             us_highest_pers, 
                                                             us_lowest_pers)
    
    # New Zealand
    nz_highest_pers, nz_lowest_pers = compare_pers_value(nz_pers_lst)
    nz_highest_pers_type, nz_lowest_pers_type = pers_headers(nz_pers_lst, 
                                                             pers_header, 
                                                             nz_highest_pers, 
                                                             nz_lowest_pers)
    
    # United Kingdom
    uk_highest_pers, uk_lowest_pers = compare_pers_value(uk_pers_lst)
    uk_highest_pers_type, uk_lowest_pers_type = pers_headers(uk_pers_lst, 
                                                             pers_header, 
                                                             uk_highest_pers, 
                                                             uk_lowest_pers)
    
    # Sweden
    se_highest_pers, se_lowest_pers = compare_pers_value(se_pers_lst)
    se_highest_pers_type, se_lowest_pers_type = pers_headers(se_pers_lst, 
                                                             pers_header, 
                                                             se_highest_pers, 
                                                             se_lowest_pers)
    
    # Netherlands
    nl_highest_pers, nl_lowest_pers = compare_pers_value(nl_pers_lst)
    nl_highest_pers_type, nl_lowest_pers_type = pers_headers(nl_pers_lst, 
                                                             pers_header, 
                                                             nl_highest_pers, 
                                                             nl_lowest_pers)
       
    # Print personality data for each country
    print("\nHere are the personality data for each country...")
    print("------------------------") 
    print_country_name("Canada")
    print_pers_data(ca_highest_pers_type, ca_highest_pers, ca_lowest_pers_type, 
                    ca_lowest_pers)

    print_country_name("Japan")
    print_pers_data(jp_highest_pers_type, jp_highest_pers, jp_lowest_pers_type, 
                    jp_lowest_pers)
    
    print_country_name("Germany")
    print_pers_data(ge_highest_pers_type, ge_highest_pers, ge_lowest_pers_type, 
                    ge_lowest_pers)
    
    print_country_name("Switzerland")
    print_pers_data(sw_highest_pers_type, sw_highest_pers, sw_lowest_pers_type, 
                    sw_lowest_pers)
    
    print_country_name("Australia")
    print_pers_data(au_highest_pers_type, au_highest_pers, au_lowest_pers_type, 
                    au_lowest_pers)
    
    print_country_name("United States")
    print_pers_data(us_highest_pers_type, us_highest_pers, us_lowest_pers_type, 
                    us_lowest_pers)

    print_country_name("New Zealand")
    print_pers_data(nz_highest_pers_type, nz_highest_pers, nz_lowest_pers_type, 
                    nz_lowest_pers)

    print_country_name("United Kingdom")
    print_pers_data(uk_highest_pers_type, uk_highest_pers, uk_lowest_pers_type, 
                    uk_lowest_pers)
    
    print_country_name("Sweden")
    print_pers_data(se_highest_pers_type, se_highest_pers, se_lowest_pers_type, 
                    se_lowest_pers)
    
    print_country_name("Netherlands")
    print_pers_data(nl_highest_pers_type, nl_highest_pers, nl_lowest_pers_type, 
                    nl_lowest_pers) 
    
    
    """ 
    Since we have the same personality types of each of the country as the 
    most common personality types (INFP-T), we are going to determine if there
    is a correlation between the percentage of hat personaluity type and the 
    gross national income per capita for each country.
    """
    
    # Combine the most common personalities % of the 10 countries into a list
    top_pers_lst = combine_into_lst(ca_highest_pers, jp_highest_pers, 
                                             ge_highest_pers, sw_highest_pers, 
                                             au_highest_pers, us_highest_pers, 
                                             nz_highest_pers, uk_highest_pers,
                                             se_highest_pers, nl_highest_pers)  
    
    # Convert the top_pers_lst into a nested list
    nested_top_pers_lst = combine_into_nested_lst(top_pers_lst)

    # Combine all of the top 10 country personality % in a list of list 
    total_pers_lst = combine_into_lst(ca_pers_lst, jp_pers_lst, 
                                              ge_pers_lst, sw_pers_lst,
                                              au_pers_lst, us_pers_lst,
                                              nz_pers_lst, uk_pers_lst, 
                                              se_pers_lst, nl_pers_lst)
     
    # Create a bar graph for the avergae GNI per capita for each country
    graph_bar_gni_data(countries_lst, lst_of_avg_gni)
    
    # Loop through 10 times for each country
    # Assign each country's personality %'s into a variable for plotting
    # Create a variable for the list of country names for graph titles
    for i in range(len(countries_lst)):
        personality_percentages = total_pers_lst[i]
        country = countries_lst[i]
    
        # Create bar graphs for the % of each personality in each country
        graph_bar_graph_pers(country, pers_header, personality_percentages) 
    
    # Draw a linear regression of the curve 
    graph_regression(nested_top_pers_lst, lst_of_avg_gni)
    
    """
    Our team used for-loop iteration by value, matplotlib, csv library, 
    while loops, functions, splitting lists, data visualization, conditional 
    statements, importing file/libraries. We focused mainly on data 
    visualization and calculating parameters of normal data distribution 
    (mean, standard deviation, minimum, and maximum). We used these techniques 
    to find highest and lowest personality types in each country, average GNIs
    per capita from all the years together, and analyzing correlation between 
    each of these calculations to illustrate the impact of personality type. 
    
    We found that INFP-T is the most popular personality trait in all of the 
    10 best countries, and the least most popular personality is ESTP-T. The 
    least common personality trait was ESTP. An Entrepreneur (ESTP) is 
    someone with the Extraverted, Observant, Thinking, and Prospecting 
    personality traits. They tend to be energetic and action-oriented, deftly 
    navigating whatever is in front of them. They love uncovering life’s 
    opportunities, whether socializing with others or in more personal 
    pursuits.
    
    When looking at other countries in the dataset, we found that each of the 
    other countries varied greatly in their most popular personality type 
    percentage. For example, in Afghanistan, the most popular personality 
    trait is ESTJ-A. However, in each of the 10 best countries, the most 
    popular personality trait remained constant. 
    
    According to the regression line, there is a negative correlation 
    (-306857.77668173) between countries with higher incomes and countries 
    with a higher population percentage of INFP-T. So, of the 10 best 
    countries, those with higher incomes actually have a lower percentage 
    of INFP-T population percentages. This is very interesting, because INFP-T 
    is a rare personality trait according to 16personalities.com. INFP 
    personalities, or Mediators, share a sincere curiosity about the depths of 
    human nature. Introspective to the core, they’re exquisitely attuned to 
    their own thoughts and feelings, but they yearn to understand the people 
    around them as well. Mediators are compassionate and nonjudgmental, always 
    willing to hear another person’s story. When someone opens up to them or 
    turns to them for comfort, they feel honored to listen and be of help. 
    Knowing that this is the most common personality trait in the top 10 
    countries, we can better understand what type of trait is best needed for 
    a company to be strong and for people to work together in harmony. Seeing 
    correlation shows that there are clear patterns between GNI per Capita and 
    personality types. Understanding that Mediators are negatively correlated 
    with average GNI per Capita introduces many new questions about how we can 
    understand human nature in numbers and personality data. 
    """
    
main()