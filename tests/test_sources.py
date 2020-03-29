import pytest
from covid import Covid
from unittest.mock import patch


def test_john_hopkins_source():
    covid = Covid()
    assert covid.source == "john_hopkins"

    covid = Covid(source="john_hopkins")
    assert covid.source == "john_hopkins"


@patch("covid.worldometers.covid.Covid._Covid__fetch")
@patch("covid.worldometers.covid.Covid._Covid__set_data")
def test_worldometers_source(mock_fetch, mock_set_data):
    covid = Covid(source="worldometers")
    assert covid.source == "worldometers"


def test_invalid_source():
    with pytest.raises(ValueError):
        Covid(source="invalid_source")
