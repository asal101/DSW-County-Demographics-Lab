import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(percent_most_under_18(counties))
    print(county_most_under_18(counties))
    print(lowest_median_income(counties))
    print(high_income_counties(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    #Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True
    first_county = counties[0]["County"]
    for county in counties:
        county["County"]
        if county["County"] < first_county:
            first_county = county["County"]
    return first_county
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""    
    first_county = counties[0]["Age"]["Percent Under 18 Years"]
    for age in counties:
        age["Age"]["Percent Under 18 Years"]
        if age["Age"]["Percent Under 18 Years"] > first_county:
            first_county = age["Age"]["Percent Under 18 Years"]
    return first_county
    
    """Return the NAME of a county with the highest percent of under 18 year olds."""
def county_most_under_18(counties):
    first_county = counties[0]["Age"]["Percent Under 18 Years"]
    county_name = ""
    for age in counties:
        age["Age"]["Percent Under 18 Years"]
        if age["Age"]["Percent Under 18 Years"] > first_county:
            first_county = age["Age"]["Percent Under 18 Years"]
            county_name = age["County"]
    return county_name
    
def lowest_median_income(counties):
    """Return a name of a county with the lowest median household income"""
    first_county = counties[0]["Income"]["Median Houseold Income"]
    county_name = ""
    for income in counties:
        income["Income"]["Median Houseold Income"]
        if income["Income"]["Median Houseold Income"] < first_county:
            first_county = income["Income"]["Median Houseold Income"]
            county_name = income["County"]
    return county_name

    
def high_income_counties(counties):
    """Return a LIST of the counties with a median household income over $90,000."""
    incomeList = []
    for income in counties:
        income["Income"]["Median Houseold Income"]
        if income["Income"]["Median Houseold Income"] > 90000:
            incomeList.append(income["County"])
    return incomeList
