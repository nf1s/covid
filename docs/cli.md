### Get all data

```bash
covid --help
```
#### John Hopkins source (default)

```bash
covid
```

or

```bash
covid -s john_hopkins
```

#### Worldometers source

```bash
covid -s worldometers
```

### List Countries

This comes in handy when you need to know the available names of countries
when using `covid -s 'source' -c 'country_name'`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

```bash
covid -s worldometers --list-countries
```

### Get Status By Country Name

```bash
covid -s worldometers -c sweden
```

### Get Total Active cases

```bash
covid -s worldometers -o active
```

### Get Total Confirmed cases

```bash
covid -s worldometers -o confirmed
```

### Get Total Recovered cases

```bash
covid -s worldometers -o recovered
```

### Get Total Deaths

```bash
covid -s worldometers -o deaths
```
