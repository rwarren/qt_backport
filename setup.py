from setuptools import setup, find_packages
import codecs
import os
import re

from version import __version__

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="qt_backport",
    version='.'.join(str(x) for x in __version__),
    description="Makes PySide/PyQt4 code work with Qt5 (using PyQt5)",
    long_description=long_description,
    url='https://github.com/russw/qt_backport',
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
    packages=["PyQt4", "PySide"],
    install_requires = [], #PyQt5 needed, but not PyPI friendly
    package_data={},
    data_files=[],
    entry_points={},
)
