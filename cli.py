#!/usr/bin/env python3
import click
from covid import Covid
from pprint import pprint

ACTIVE = "active"
CONFIRMED = "confirmed"
RECOVERED = "recovered"
DEATHS = "deaths"


@click.group()
def cli():
    pass


@click.option(
    "--source",
    "-s",
    type=str,
    default="john_hopkins",
    help="select source, 'john_hopkins' or 'worldometers'",
    show_default=True,
)
@click.option(
    "--country", "-c", type=str, help="get stats by country name, 'sweden' or 'italy'",
)
@click.option(
    "--option",
    "-o",
    type=str,
    help="get total stats. options 'active', 'confimed', 'recovered' or 'deaths'",
)
@cli.command(name="covid", help="Get coronavirus stats")
def get_data(source, country, option):
    click.echo(click.style(f"fetching data from  '{source}'", fg="green"))
    covid = Covid(source)

    if option and country:
        data = covid.get_status_by_country_name(country)
        click.echo(
            click.style(f"total {option} in {country}: {data[option]}", fg="yellow")
        )
        return

    if country:
        data = covid.get_status_by_country_name(country)
        pprint(data)
        return
    elif option:
        if option == ACTIVE:
            data = covid.get_total_active_cases()
            click.echo(click.style(f"total active cases: {data}", fg="yellow"))
            return
        if option == CONFIRMED:
            data = covid.get_total_confirmed_cases()
            click.echo(click.style(f"total confirmed cases: {data}", fg="yellow"))
            return
        if option == RECOVERED:
            data = covid.get_total_recovered()
            click.echo(click.style(f"total recovered cases: {data}", fg="yellow"))
            return
        if option == DEATHS:
            data = covid.get_total_deaths()
            click.echo(click.style(f"total deaths: {data}", fg="yellow"))
            return

        click.echo(
            click.style(f"Total option argument '{option}' is not allowed", fg="red")
        )
        return

    data = covid.get_data()
    pprint(data)
    return


if __name__ == "__main__":
    cli()
