# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statistics

"""
from pydantic import BaseModel, Field
from decimal import Decimal


class CovidModel(BaseModel):
    """Dataclass acts as a Model for Covid data

    """

    country: str = Field(..., alias="Country,Other")
    confirmed: int = Field(..., alias="TotalCases")
    new_cases: int = Field(..., alias="NewCases")
    deaths: int = Field(..., alias="TotalDeaths")
    recovered: int = Field(..., alias="TotalRecovered")
    active: int = Field(..., alias="ActiveCases")
    critical: int = Field(None, alias="Serious,Critical")
    total_cases_per_million: Decimal = Field(..., alias="TotCases/1M pop")
    total_deaths_per_million: Decimal = Field(..., alias="TotDeaths/1M pop")
