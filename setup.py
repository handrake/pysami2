#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys

from setuptools import setup, find_packages

setup(
    name='pysami2',
    version='0.0.1',
    license='MIT',
    author='Byoung Gi Lee',
    author_email='handrake@gmail.com',
    url='https://github.com/handrake/pysami2',
    description='Python library and script for converting SAMI file',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['setuptools', 'chardet'],
    classifiers=[],
)
