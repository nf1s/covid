# -*- coding: utf-8 -*-
"""Sample example used for testing purposes

"""

from covid import Covid

if __name__ == "__main__":
    covid = Covid()

    deaths = covid.get_total_deaths()
    confirmed = covid.get_total_confirmed_cases()
    recovered = covid.get_total_recovered()

    countries = covid.list_countries()
    sweden_cases = covid.get_status_by_country("sweden")

    print(covid.get_data())

    print(f"deaths: {deaths}, confirmed: {confirmed}, recovered: {recovered}")

    print(f"sweden_cases: {sweden_cases}")

    print(f"countries: {countries}")
