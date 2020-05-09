### Get all data

#### John Hopkins source (default)

```bash
./cli.py covid
```

or

```bash
./cli.py covid -s john_hopkins
```

#### Worldometers source

```bash
./cli.py covid -s worldometers
```

### List Countries

This comes in handy when you need to know the available names of countries
when using `get_status_by_country_name`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

```bash
./cli.py covid -s worldometers --list-countries
```

### Get Status By Country Name

```bash
./cli.py covid -s worldometers -c sweden
```

### Get Total Active cases

```bash
./cli.py covid -s worldometers -o active
```

### Get Total Confirmed cases

```bash
./cli.py covid -s worldometers -o confirmed
```

### Get Total Recovered cases

```bash
./cli.py covid -s worldometers -o recovered
```

### Get Total Deaths

```bash
./cli.py covid -s worldometers -o deaths
```
