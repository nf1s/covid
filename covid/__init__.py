# -*- coding: utf-8 -*-
from .john_hopkins import Covid as JohnHopkinsCovid
from .worldometers import Covid as WorldometersCovid

__author__ = "Ahmed Nafies Okasha Mohamed"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"

__license__ = "MIT"
__version__ = "2.0.0"
__maintainer__ = "Ahmed Nafies"
__email__ = "ahmed.nafies@gmail.com"
__status__ = "Production"


def Covid(source="john_hopkins"):
    if source == "worldometers":
        return WorldometersCovid()
    return JohnHopkinsCovid()
