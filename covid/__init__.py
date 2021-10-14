# -*- coding: utf-8 -*-
from covid import config
from covid.john_hopkins import Covid as JohnHopkinsCovid
from covid.worldometers import Covid as WorldometersCovid

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"
__version__ = "2.5.1"

services = {
    "john_hopkins": JohnHopkinsCovid,
    "worldometers": WorldometersCovid,
}


def Covid(source=config.JOHN_HOPKINS):
    try:
        service = services[source]
        return service()
    except KeyError:
        raise ValueError(f"Allowed sources are {', '.join(config.SOURCES)}")
