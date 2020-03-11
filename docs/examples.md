### Get All Data

    from covid import Covid

    covid = Covid()
    covid.get_data()

result

    [
        {
            'country': 'Mainland China',
            'confirmed': 80756,
            'deaths': 3136,
            'recovered': 60096,
            'latitude': 30.5928,
            'longitude': 114.3055,
            'last_update': 1582264984000
        },
        {
            'country': 'Italy',
            'confirmed': 9172,
            'deaths': 463,
            'recovered': 724,
            'latitude': 43.0,
            'longitude': 12.0,
            'last_update': 1583777591000
        },
        ...

### Get Status By Country

    sweden_cases = covid.get_status_by_country("sweden")
    print(sweden_cases)

result

    {
        'country': 'Sweden',
        'confirmed': 355,
        'deaths': 0,
        'recovered': 1,
        'latitude': 63.0,
        'longitude': 16.0,
        'last_update': 1583893094000
    }

### List Countries

This comes in handy when you need to know the available names of countries
when using `get_status_by_country`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

    countries = covid.list_countries()
    print(countries)

result

    [
        "china",
        "italy",
        "iran",
        "republic of korea",
        ...
    ]

### Get Total Confirmed cases

    confirmed = covid.get_total_confirmed_cases()

### Get Total Recovered cases

    recovered = covid.get_total_recovered()

### Get Total Deaths

    deaths = covid.get_total_deaths()
