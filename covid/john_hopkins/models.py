# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statistics

"""
from pydantic import BaseModel, Field


class CovidModel(BaseModel):
    """Dataclass acts as a Model for Covid data

    """

    id: str = Field(..., alias="OBJECTID")
    country: str = Field(..., alias="Country_Region")
    confirmed: int = Field(0, alias="Confirmed")
    active: int = Field(0, alias="Active")
    deaths: int = Field(0, alias="Deaths")
    recovered: int = Field(0, alias="Recovered")
    latitude: float = Field(None, alias="Lat")
    longitude: float = Field(None, alias="Long_")
    last_update: int = Field(0, alias="Last_Update")


class CountryModel(BaseModel):
    """Dataclass acts as a Model for Countries data

    """

    id: str = Field(..., alias="OBJECTID")
    name: str = Field(..., alias="Country_Region")
