# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) wayhk. All Rights Reserved
#
################################################################################
"""
Setup
"""
from setuptools import setup
from setuptools import find_packages
with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()
setup(
    name='Pflow',
    version='0.1.0',
    description='a light work flow engine implemented by python',
    long_description=readme,
    author='wayhk',
    author_email='@15210836313@163.com',
    url='https://github.com/wayhk/Pflow',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
    ]
)