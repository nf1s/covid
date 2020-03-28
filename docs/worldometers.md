    covid = Covid(source="worldometers")

### Check the Source

    covid.source

result

    "worldometers"

### Get Data

    covid.get_data()

result

    [
        {
            'country': 'Malta',
            'confirmed': 110,
            'new_cases': 3,
            'deaths': 0,
            'recovered': 2,
            'active': 108,
            'critical': 1,
            'total_cases_per_million': Decimal('249'),
            'total_deaths_per_million': Decimal('0')
        },
        {
            'country': 'Cameroon',
            'confirmed': 66,
            'new_cases': 10,
            'deaths': 0,
            'recovered': 2,
            'active': 64,
            'critical': 0,
            'total_cases_per_million': Decimal('2'),
            'total_deaths_per_million': Decimal('0')
        },
        ...
    ]

### Get Status By Country Name

    covid.get_status_by_country_name("italy")

result

    {
        'country': 'Italy',
        'confirmed': 69176,
        'new_cases': 5249,
        'deaths': 6820,
        'recovered': 8326,
        'active': 54030,
        'critical': 3393,
        'total_cases_per_million': Decimal('1144'),
        'total_deaths_per_million': Decimal('113')
    }

### List Countries

This comes in handy when you need to know the available names of countries
when using `get_status_by_country_name`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

    countries = covid.list_countries()

result

    [
        'china',
        'italy',
        'usa',
        'spain',
        'germany',
    ...
    ]

### Get Total Active cases

    active = covid.get_total_active_cases()

### Get Total Confirmed cases

    confirmed = covid.get_total_confirmed_cases()

### Get Total Recovered cases

    recovered = covid.get_total_recovered()

### Get Total Deaths

    deaths = covid.get_total_deaths()
