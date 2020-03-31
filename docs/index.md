# Getting Started

[![CircleCI](https://circleci.com/gh/ahmednafies/covid.svg?style=shield)](https://circleci.com/gh/ahmednafies/covid) ![CircleCI](https://img.shields.io/circleci/build/github/ahmednafies/covid/master) [![codecov](https://codecov.io/gh/ahmednafies/covid/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/covid) ![GitHub top language](https://img.shields.io/github/languages/top/ahmednafies/covid) ![PyPI](https://img.shields.io/pypi/v/covid) [![Downloads](https://pepy.tech/badge/covid)](https://pepy.tech/project/covid) ![license](https://img.shields.io/badge/license-MIT-green)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ahmednafies/covid) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/ahmednafies/covid) ![GitHub issues](https://img.shields.io/github/issues/ahmednafies/covid) ![GitHub closed issues](https://img.shields.io/github/issues-closed/ahmednafies/covid)

Python SDK to get information regarding the novel corona virus provided
by Johns Hopkins university and worldometers.info

![corona.jpeg](img/corona.jpeg)

Full code on [github](https://github.com/ahmednafies/covid)

## Requirements

    python >= 3.6

## How to install

    pip install covid

## Dependencies

    pydantic
    requests

## How to use

    from covid import Covid

    # by default data source is "john_hopkins"
    covid = Covid()

    # or
    covid = Covid(source="john_hopkins")

    # to get data from worldometers.info
    covid = Covid(source="worldometers")

    # get all data
    covid.get_data()
