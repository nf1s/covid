# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

VERSION = "1.4.4"

setup(
    name="covid",
    version=VERSION,
    description="Python SDK to get information regarding the novel corona virus provided by Johns Hopkins university",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ahmednafies.github.io/covid/",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["covid"],
    install_requires=["requests", "pydantic"],
    project_urls={
        "Documentation": "https://ahmednafies.github.io/covid/",
        "Source": "https://github.com/ahmednafies/covid",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
    python_requires=">=3.6",
)
