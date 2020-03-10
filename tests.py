# -*- coding: utf-8 -*-
""" tests module
"""

import covid


def test_data():
    data = covid.data()
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
