# -*- coding: utf-8 -*-
from .john_hopkins import Covid as JohnHopkinsCovid
from .worldometers import Covid as WorldometersCovid

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"


def Covid(source="john_hopkins"):
    if source == "worldometers":
        return WorldometersCovid()
    return JohnHopkinsCovid()
