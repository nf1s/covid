# -*- coding: utf-8 -*-
from .john_hopkins import Covid as JohnHopkinsCovid
from .worldometers import Covid as WorldometersCovid


def Covid(source="john_hopkins"):
    if source == "worldometers":
        return WorldometersCovid()
    return JohnHopkinsCovid()
