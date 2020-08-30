import typer
from covid import Covid
from pprint import pprint
from enum import Enum


class Options(str, Enum):
    ACTIVE = "active"
    CONFIRMED = "confirmed"
    RECOVERED = "recovered"
    DEATHS = "deaths"


app = typer.Typer()


@app.command()
def get_data(
    source: str = typer.Option(
        "john_hopkins",
        "-s",
        "--source",
        help="select source, 'john_hopkins' or  'worldometers'",
        show_default=True,
    ),
    country: str = typer.Option(
        None,
        "--country",
        "-c",
        help="get stats by country name, 'sweden' or 'italy'",
    ),
    option: Options = typer.Option(
        None,
        "--option",
        "-o",
        help="get total stats. options 'active', 'confimed', 'recovered' or 'deaths'",
    ),
    list_countries: bool = typer.Option(
        None,
        "--list-countries",
        "-l",
        help="get a list of country name depending on a source",
        is_flag=True,
    ),
):
    """Get coronavirus information"""

    typer.echo(typer.style(f"fetching data from  '{source}'", fg="green"))
    covid = Covid(source)

    if list_countries:
        data = covid.list_countries()
        pprint(data)
        return

    if option and country:
        data = covid.get_status_by_country_name(country)
        typer.echo(
            typer.style(
                f"total {option} in {country}: {data[option]}", fg="yellow"
            )
        )
        return

    if country:
        data = covid.get_status_by_country_name(country)
        pprint(data)
        return
    elif option:
        if option == Options.ACTIVE:
            data = covid.get_total_active_cases()
            typer.echo(typer.style(f"total active cases: {data}", fg="yellow"))
            return
        if option == Options.CONFIRMED:
            data = covid.get_total_confirmed_cases()
            typer.echo(
                typer.style(f"total confirmed cases: {data}", fg="yellow")
            )
            return
        if option == Options.RECOVERED:
            data = covid.get_total_recovered()
            typer.echo(
                typer.style(f"total recovered cases: {data}", fg="yellow")
            )
            return
        if option == Options.DEATHS:
            data = covid.get_total_deaths()
            typer.echo(typer.style(f"total deaths: {data}", fg="yellow"))
            return

        typer.echo(
            typer.style(
                f"Total option argument '{option}' is not allowed", fg="red"
            )
        )
        return

    data = covid.get_data()
    pprint(data)
    return


if __name__ == "__main__":
    app()
