# py2elastic

''' Python 3 only '''

Convert CSV file (and eventually others) in to an ElasticSearch document so it can be queried without having to worry about the format of the CSV file.

## Installation

    python setup.py install

## Usage
It's most basic usage is:

    py2elastic sample.csv

You can also specify the ElasticSearch server with a URL:

    py2elastic test.csv --esurl es://example.com:9200/index

Get help:

    py2elastic --help
