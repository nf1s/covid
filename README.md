# Covid

[![CircleCI](https://circleci.com/gh/ahmednafies/covid.svg?style=shield)](https://circleci.com/gh/ahmednafies/covid) [![codecov](https://codecov.io/gh/ahmednafies/covid/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/covid) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ahmednafies/covid) [![Downloads](https://pepy.tech/badge/covid)](https://pepy.tech/project/covid) ![GitHub](https://img.shields.io/github/license/ahmednafies/covid)

## Description

Python SDK to get information regarding the novel corona virus provided
by Johns Hopkins university and worldometers.info

Full Documentation can be found [here](https://ahmednafies.github.io/covid/)

![corona.jpeg](docs/img/corona.jpeg)

## Requirements

    python >= 3.6

## How to install

    pip install covid

## Dependencies

    pydantic
    requests

## How to use

## John Hopkins University API

![john_hopkins](docs/img/john_hopkins.png)

### Get All Data

```python
from covid import Covid

covid = Covid()
covid.get_data()
```

#### Result

```python
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
]
```

### List Countries

This comes in handy when you need to know the available names of countries
when using `get_status_by_country_name`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

```python
countries = covid.list_countries()
```

#### Result

```python
[
    {'id': '53', 'country': 'China'},
    {'id': '115', 'country': 'Italy'}
    ...
]
```

### Get Status By Country ID

```python
italy_cases = covid.get_status_by_country_id(115)
```

#### Result

```python
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
```

### Get Status By Country Name

```python
italy_cases = covid.get_status_by_country_name("italy")
```

#### Result

```python
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
```

### Get Total Active cases

```python
active = covid.get_total_active_cases()
```

### Get Total Confirmed cases

```python
confirmed = covid.get_total_confirmed_cases()
```

### Get Total Recovered cases

```python
recovered = covid.get_total_recovered()
```

### Get Total Deaths

```python
deaths = covid.get_total_deaths()
```

## Getting data from Worldometers.info (New)

![worldometers](docs/img/worldometers.png)

```python
covid = Covid(source="worldometers")
```

### Get Data

```python
covid.get_data()
```

#### Result

```python
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
```

### Get Status By Country Name

```python
covid.get_status_by_country_name("italy")
```

#### Result

```python
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
```

### List Countries

```python
countries = covid.list_countries()
```

#### Result

```python
[
    'china',
    'italy',
    'usa',
    'spain',
    'germany',
...
]
```

### Get Total Active cases

```python
active = covid.get_total_active_cases()
```

### Get Total Confirmed cases

```python
confirmed = covid.get_total_confirmed_cases()
```

### Get Total Recovered cases

```python
recovered = covid.get_total_recovered()
```

### Get Total Deaths

```python
deaths = covid.get_total_deaths()
```
