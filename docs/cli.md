### Get all data

```bash
./cli --help
```
#### John Hopkins source (default)

```bash
./cli
```

or

```bash
./cli -s john_hopkins
```

#### Worldometers source

```bash
./cli -s worldometers
```

### List Countries

This comes in handy when you need to know the available names of countries
when using `./cli -s 'source' -c 'country_name'`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

```bash
./cli -s worldometers --list-countries
```

### Get Status By Country Name

```bash
./cli -s worldometers -c sweden
```

### Get Total Active cases

```bash
./cli -s worldometers -o active
```

### Get Total Confirmed cases

```bash
./cli -s worldometers -o confirmed
```

### Get Total Recovered cases

```bash
./cli -s worldometers -o recovered
```

### Get Total Deaths

```bash
./cli -s worldometers -o deaths
```
