# -*- coding: utf-8 -*-
""" tests module
"""
from unittest.mock import patch

import pytest

from covid import Covid


class MockRequestData:
    @staticmethod
    def json():
        return {"key": "value"}


def test_all_data():
    covid = Covid(source="john_hopkins")
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
    covid = Covid(source="john_hopkins")
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
    covid = Covid(source="john_hopkins")
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


def test_get_by_country_name_initials():
    covid = Covid(source="john_hopkins")
    data = covid.get_status_by_country_name("US")
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data
    assert data["country"] == "US"


def test_get_by_country_invalid_name():
    covid = Covid(source="john_hopkins")
    with pytest.raises(ValueError):
        covid.get_status_by_country_name("USA")


def test_total_confirmed_cases():
    covid = Covid(source="john_hopkins")
    data = covid.get_total_confirmed_cases()
    assert type(data) is int


def test_total_deaths():
    covid = Covid(source="john_hopkins")
    data = covid.get_total_deaths()
    assert type(data) is int


def test_list_countries():
    covid = Covid(source="john_hopkins")
    countries = covid.list_countries()
    assert type(countries) == list


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
def test_exception_rasied_on_get_total_active_cases(mock):
    covid = Covid(source="john_hopkins")
    with pytest.raises(Exception):
        covid.get_total_active_cases()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
def test_exception_rasied_on_get_total_confirmed_cases(mock):
    covid = Covid(source="john_hopkins")
    with pytest.raises(Exception):
        covid.get_total_confirmed_cases()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
def test_exception_rasied_on_get_total_recovered(mock):
    covid = Covid(source="john_hopkins")
    with pytest.raises(Exception):
        covid.get_total_recovered()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
def test_exception_rasied_on_total_deaths(mock):
    covid = Covid(source="john_hopkins")
    with pytest.raises(Exception):
        covid.get_total_deaths()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
def test_exception_rasied_on_get_country_by_id(mock):
    covid = Covid(source="john_hopkins")
    with pytest.raises(Exception):
        covid.get_status_by_country_id(50)


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
def test_exception_rasied_on_get_country_by_name(mock):
    covid = Covid(source="john_hopkins")
    with pytest.raises(Exception):
        covid.get_status_by_country_name("italy")
