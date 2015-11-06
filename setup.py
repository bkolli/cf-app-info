#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


INSTALL_REQUIRES = [
    'gevent',
    'grequests',
    'requests',
    'docopt',
]


setup(
    name='cf-app-info',
    version='1.0',
    description='Check the Information of CloudFoundry apps',
    url='https://github.com/bkolli/cf-app-info',
    install_requires=INSTALL_REQUIRES,
    platforms=['OS Independent'],
    scripts=['cf_app_info.py'],
    long_description='Check the Information of CloudFoundry apps',
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'cf-app-info = cf_app_info:cli',
        ],
    },
)
