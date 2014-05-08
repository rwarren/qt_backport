from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="qt5_backport",
    version=open("VERSION", "r").read().strip(),
    description="Makes your old Qt4 code work with Qt5",
    long_description=long_description,
    url='https://github.com/russw/qt5_backport',
    author='Russell Warren',
    author_email='russ@perspexis.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='Qt PyQt4 PyQt5 PySide',
    packages=["PyQt4", "PySide"],
    install_requires = [], #PyQt5 needed, but not PyPI friendly
    package_data={},
    data_files=[],
    entry_points={},
)
