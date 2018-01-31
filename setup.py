# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pyselenium/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='pysele',
    version=version,
    author='bugmaster',
    description='WebUI automation testing framework based on Selenium and unittest ',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['selenium>=3.8.0', 'parameterized>=0.6.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Ubuntu',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries ::Testing'
    ],
    entry_points='''
        [console_scripts]
        pyselenium=pyselenum.Pyse:main
    '''
)
