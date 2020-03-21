# Covid

[![CircleCI](https://circleci.com/gh/ahmednafies/covid.svg?style=shield)](https://circleci.com/gh/ahmednafies/covid) [![codecov](https://codecov.io/gh/ahmednafies/covid/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/covid)

## Description

Python SDK to get information regarding the novel corona virus provided by Johns Hopkins university

Full Documentation can be found [here](https://ahmednafies.github.io/covid/)

## Requirements

    python >= 3.6

## How to install

    pip install covid

## Dependencies

    pydantic
    requests

## How to use

### Get All Data

    from covid import Covid

    covid = Covid()
    covid.get_data()

#### Result

    [
        {
            'id': '53',
            'country': 'China',
            'confirmed': 81020,
            'active': 9960,
            'deaths': 3217,
            'recovered': 67843,
            'latitude': 30.5928,
            'longitude': 114.3055,
            'last_update': 1584097775000
        },
        {
            'id': '115',
            'country': 'Italy',
            'confirmed': 24747,
            'active': 20603,
            'deaths': 1809,
            'recovered': 2335,
            'latitude': 41.8719,
            'longitude': 12.5674,
            'last_update': 1584318130000
        },
        ...

### List Countries

This comes in handy when you need to know the available names of countries
when using `get_status_by_country`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

    countries = covid.list_countries()

#### Result

    [
        {'id': '53', 'country': 'China'},
        {'id': '115', 'country': 'Italy'}
        ...
    ]

### Get Status By Country ID

    italy_cases = covid.get_status_by_country_id(115)

#### Result

    {
        'id': '115',
        'country': 'Italy',
        'confirmed': 24747,
        'active': 20603,
        'deaths': 1809,
        'recovered': 2335,
        'latitude': 41.8719,
        'longitude': 12.5674,
        'last_update': 1584318130000
    }

### Get Status By Country Name

    italy_cases = covid.get_status_by_country_name("italy")

#### Result

    {
        'id': '115',
        'country': 'Italy',
        'confirmed': 24747,
        'active': 20603,
        'deaths': 1809,
        'recovered': 2335,
        'latitude': 41.8719,
        'longitude': 12.5674,
        'last_update': 1584318130000
    }

### Get Total Active cases

    active = covid.get_total_active_cases()

### Get Total Confirmed cases

    confirmed = covid.get_total_confirmed_cases()

### Get Total Recovered cases

    recovered = covid.get_total_recovered()

### Get Total Deaths

    deaths = covid.get_total_deaths()
