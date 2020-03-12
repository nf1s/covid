# -*- coding: utf-8 -*-
"""Sample example used for testing purposes

"""

from covid import Covid

if __name__ == "__main__":
    covid = Covid()
    print(covid.get_data())

    deaths = covid.get_total_deaths()
    confirmed = covid.get_total_confirmed_cases()
    recovered = covid.get_total_recovered()

    print(f"deaths: {deaths}, confirmed: {confirmed}, recovered: {recovered}")

    countries = covid.list_countries()
    print(f"countries: {countries}")

    cases = covid.get_status_by_country_id(40)
    print(f"cases: {cases}")

    cases = covid.get_status_by_country_name("sweden")
    print(f"cases: {cases}")
