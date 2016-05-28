#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    'pytest'
]

setup(
    name='blinker_herald',
    version='0.1.0',
    description=(
        "The Blinker Herald includes helpers to easily emit signals using "
        "Blinker. Decorate a function or method with @blinker_herald.emit() "
        "and pre and post signals will automatically "
        "be emitted to connected handlers."
    ),
    long_description=readme + '\n\n' + history,
    author="Bruno Rocha",
    author_email='rochacbruno@gmail.com',
    url='https://github.com/SatelliteQE/blinker_herald',
    packages=[
        'blinker_herald',
    ],
    package_dir={'blinker_herald':
                 'blinker_herald'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='blinker_herald',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
