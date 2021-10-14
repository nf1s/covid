![john_hopkins.png](img/john_hopkins.png)

by default `Covid` uses John Hopkins univeristy API as default
so you can use:

```python
covid = Covid()
```

or

```python
covid = Covid(source="john_hopkins")
```

### Check the Source

```python
covid.source
```

result

```python
"john_hopkins"
```

### Get All Data

```python
from covid import Covid

covid = Covid()
covid.get_data()
```

result

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
    {'id': '53', 'country': 'China'},
    {'id': '115', 'country': 'Italy'}
    ...
]
```

### Get Status By Country ID

```python
italy_cases = covid.get_status_by_country_id(115)
```

result

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

result

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

### Get Total Confirmed cases

```python
confirmed = covid.get_total_confirmed_cases()
```

### Get Total Deaths

```python
deaths = covid.get_total_deaths()
```
