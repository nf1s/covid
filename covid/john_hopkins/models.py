# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statistics

"""
from pydantic import BaseModel, Field


class CovidModel(BaseModel):
    """Dataclass acts as a Model for Covid data"""

    id: int = Field(..., alias="OBJECTID")
    country: str = Field(..., alias="Country_Region")
    confirmed: int | None = Field(None, alias="Confirmed")
    active: int | None = Field(None, alias="Active")
    deaths: int | None = Field(None, alias="Deaths")
    recovered: int | None = Field(None, alias="Recovered")
    latitude: float | None = Field(None, alias="Lat")
    longitude: float | None = Field(None, alias="Long_")
    last_update: int | None = Field(None, alias="Last_Update")


class CountryModel(BaseModel):
    """Dataclass acts as a Model for Countries data"""

    id: int = Field(..., alias="OBJECTID")
    name: str = Field(..., alias="Country_Region")
