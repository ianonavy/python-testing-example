#!/usr/bin/env python

from setuptools import find_packages, setup


NAME = 'favorite-printer'
VERSION = '0.7.1'
DESCRIPTION = 'Media API asserter server implementation and client library'
LONG_DESCRIPTION = DESCRIPTION
REQUIREMENTS = [
]


if __name__ == '__main__':
    setup(name=NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          install_requires=REQUIREMENTS,
          namespace_packages=[],
          packages=find_packages(exclude=['test', 'test.*']))
