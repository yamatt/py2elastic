#!/usr/bin/env python

from distutils.core import setup

setup(
    name='py2elastic',
    version='0.1',
    description='Take import file (csv) and put it in ElasticSearch',
    log_description=open("README.md","r").read()
    author='Matt Copperwaite',
    author_email='matt@copperwaite.net',
    url='https://github.com/yamatt/py2elastic',
    packages=[
        'py2elastic',
    ],
    scripts=[
        'scripts/py2elastic'
    ],
    classifiers=[
    ],
    dependencies=open("requirements.txt","r").readlines()
    license="AGPLv3"
)
