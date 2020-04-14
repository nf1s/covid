# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statistics

"""
from pydantic import BaseModel, Field
from decimal import Decimal


class CovidModel(BaseModel):
    """Dataclass acts as a Model for Covid data

    """

    country: str = Field(..., alias="Country,Other")
    confirmed: int = Field(0, alias="TotalCases")
    new_cases: int = Field(0, alias="NewCases")
    deaths: int = Field(0, alias="TotalDeaths")
    recovered: int = Field(0, alias="TotalRecovered")
    active: int = Field(0, alias="ActiveCases")
    critical: int = Field(0, alias="Serious,Critical")
    new_deaths: int = Field(0, alias="NewDeaths")
    total_tests: int = Field(0, alias="TotalTests")
    total_tests_per_million: Decimal = Field(Decimal(0), alias="Tests/1M pop")
    total_cases_per_million: Decimal = Field(
        Decimal(0), alias="TotCases/1M pop"
    )
    total_deaths_per_million: Decimal = Field(
        Decimal(0), alias="Deaths/1M pop"
    )
