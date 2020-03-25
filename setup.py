# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open("README.md") as f:
    long_description = f.read()

VERSION = "2.0.2"

setup(
    name="covid",
    version=VERSION,
    description="Python SDK to get information regarding the novel corona virus provided by Johns Hopkins university and worldometers.info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ahmednafies.github.io/covid/",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=find_packages("covid"),
    package_dir={"": "covid"},
    # include_package_data=True,
    install_requires=["requests", "pydantic", "beautifulsoup4"],
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
