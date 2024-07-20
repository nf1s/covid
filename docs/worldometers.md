![worldometers.png](img/worldometers.png)

by default `Covid` uses worldometers.info as default
so you can use:


```python
from covid import covid

# by default data source is "worldometers"
covid = Covid()

# or

covid = Covid(source="worldometers")
```

### Check the Source

```python
covid.source
```

result

```python
"worldometers"
```

### Get Data

```python
covid.get_data()
```

result

```python
[
    {
        'country': 'USA',
        'confirmed': 311637,
        'new_cases': 280,
        'deaths': 8454,
        'recovered': 14828,
        'active': 288355,
        'critical': 8206,
        'new_deaths': 2,
        'total_tests': 1656897,
        'total_tests_per_million': Decimal('0'),
        'total_cases_per_million': Decimal('941'),
        'total_deaths_per_million': Decimal('26')
    },
    {
        'active': 1376,
        'confirmed': 81669,
        'country': 'China',
        'critical': 295,
        'deaths': 3329,
        'new_cases': 30,
        'new_deaths': 3,
        'recovered': 76964,
        'total_cases_per_million': Decimal('57'),
        'total_deaths_per_million': Decimal('2'),
        'total_tests': 0,
        'total_tests_per_million': Decimal('0')
    }
    ...
]
```

### Get Status By Country Name

```python
covid.get_status_by_country_name("italy")
```

result

```python
{
    'active': 88274,
    'confirmed': 124632,
    'country': 'Italy',
    'critical': 3994,
    'deaths': 15362,
    'new_cases': 0,
    'new_deaths': 0,
    'recovered': 20996,
    'total_cases_per_million': Decimal('2061'),
    'total_deaths_per_million': Decimal('254'),
    'total_tests': 657224,
    'total_tests_per_million': Decimal('0')
 }
```

### List Countries

This comes in handy when you need to know the available names of countries
when using `get_status_by_country_name`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

```python
countries = covid.list_countries()
```

result

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
