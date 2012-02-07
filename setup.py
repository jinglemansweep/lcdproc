#import ez_setup, os
#ez_setup.use_setuptools()
import os
from setuptools import setup, find_packages
setup(
    name = "lcdproc",
    version = "0.03",
    author = "JingleManSweep",
    author_email = "jinglemansweep@gmail.com",
    description = "Python OOP Wrapper Library for LCDproc Telnet API",
    url = "http://github.com/jingleman/lcdproc",
    packages = find_packages(),
    scripts = [],
    include_package_data = True
)
