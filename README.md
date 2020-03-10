# Covid

## Description

Python SDK to get information regarding the novel corona virus provided by Johns Hopkins university

## How to install

    pip install covid

## Dependencies

    pydantic
    requests

## How to use

    import covid

    covid.data()

### result

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
