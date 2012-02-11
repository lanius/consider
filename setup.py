# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = f.read()

description = """Consider is a parser for the ThinkGear protocol \
used by NeuroSky devices."""

setup(
    name='consider',
    version='0.1',
    url='https://github.com/lanius/consider/',
    license='MIT',
    author='lanius',
    author_email='lanius@nirvake.org',
    description=description,
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
