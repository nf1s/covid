# -*- coding: utf-8 -*-
from covid import config
from covid.john_hopkins import Covid as JohnHopkinsCovid
from covid.worldometers import Covid as WorldometersCovid

__author__ = "Ahmed Nafies <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies"
__license__ = "MIT"

services = {
    "john_hopkins": JohnHopkinsCovid,
    "worldometers": WorldometersCovid,
}


def Covid(source=config.WORLDOMETERS):
    try:
        service = services[source]
        return service()
    except KeyError:
        raise ValueError(f"Allowed sources are {', '.join(config.SOURCES)}")
