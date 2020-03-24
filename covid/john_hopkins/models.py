# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statistics

"""
from pydantic import BaseModel, Field


class CovidModel(BaseModel):
    """Dataclass acts as a Model for Covid data

    """

    id: str = Field(..., alias="OBJECTID")
    country: str = Field(..., alias="Country_Region")
    confirmed: int = Field(..., alias="Confirmed")
    active: int = Field(..., alias="Active")
    deaths: int = Field(..., alias="Deaths")
    recovered: int = Field(..., alias="Recovered")
    latitude: float = Field(..., alias="Lat")
    longitude: float = Field(..., alias="Long_")
    last_update: int = Field(..., alias="Last_Update")


class CountryModel(BaseModel):
    """Dataclass acts as a Model for Countries data

    """

    id: str = Field(..., alias="OBJECTID")
    name: str = Field(..., alias="Country_Region")
