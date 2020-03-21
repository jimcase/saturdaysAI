# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# sudo apt install python3-pip
# pip3 install pytest
# python3-pytest
# pip3 install coveralls
# pip3 install setuptools


setup(
    name='common',
    url='https://github.com/jimcase/saturdaysAI/tree/develop',
    license='GNU General Public License v3.0',
    author='jimcase',
    keywords='test unittest common',
    description=u'Testing using unittest for common',
    packages=find_packages(include=['test_*.py']),
    python_requires='>=3',
)
