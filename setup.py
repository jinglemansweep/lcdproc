#import ez_setup, os
#ez_setup.use_setuptools()
import os, sys
from setuptools import setup, find_packages

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name = "lcdproc",
    version = "0.03",
    author = "JingleManSweep",
    author_email = "jinglemansweep@gmail.com",
    description = "Python OOP Wrapper Library for LCDproc Telnet API",
    url = "http://github.com/jingleman/lcdproc",
    packages = find_packages(),
    scripts = [],
    include_package_data = True,
    **extra
)
