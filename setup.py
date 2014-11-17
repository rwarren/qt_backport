#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import codecs
import os
import re

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
main_pkg = "qt_backport"
setup(
    name=main_pkg,
    version=open(main_pkg + "/VERSION", "r").read().strip(),
    description="Makes PySide/PyQt4 code work with Qt5 (using PyQt5)",
    long_description=long_description,
    url='https://github.com/rwarren/qt_backport',
    author='Russell Warren',
    author_email='russ@perspexis.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Operating System :: OS Independent",
    ],
    keywords='Qt PyQt4 PyQt5 PySide',
    packages=[main_pkg, "PyQt4", "PySide"],
    install_requires = [], #PyQt5 needed, but not PyPI friendly
    package_data={main_pkg: ["VERSION", ]},
    data_files=[],
    entry_points={},
)
