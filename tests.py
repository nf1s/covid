# -*- coding: utf-8 -*-
""" tests module
"""

from covid import Covid


def test_all_data():
    covid = Covid()
    data = covid.get_data()
    assert data is not None
    assert type(data) == list
    element = data[0]
    assert "country" in element
    assert "confirmed" in element
    assert "deaths" in element
    assert "recovered" in element
    assert "latitude" in element
    assert "longitude" in element
    assert "last_update" in element


def test_get_by_country_id():
    covid = Covid()
    countries = covid.list_countries()
    country = filter(lambda country: country["name"] == "Sweden", countries)
    country = next(country)
    data = covid.get_status_by_country_id(country["id"])
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data
    assert data["country"] == "Sweden"


def test_get_by_country_name():
    covid = Covid()
    data = covid.get_status_by_country_name("sweden")
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data
    assert data["country"] == "Sweden"


def test_total_active_cases():
    covid = Covid()
    data = covid.get_total_active_cases()
    assert type(data) is int


def test_total_confirmed_cases():
    covid = Covid()
    data = covid.get_total_confirmed_cases()
    assert type(data) is int


def test_total_deaths():
    covid = Covid()
    data = covid.get_total_deaths()
    assert type(data) is int


def test_total_recovered():
    covid = Covid()
    data = covid.get_total_recovered()
    assert type(data) is int


def test_list_countries():
    covid = Covid()
    countries = covid.list_countries()
    assert type(countries) == list
