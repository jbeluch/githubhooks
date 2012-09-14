#!/usr/bin/env python
from setuptools import setup


setup(name='githubhooks',
    version='0.2-dev',
    description='List and Test Github hooks from the command line',
    author='Jonathan Beluch',
    author_email='web@jonathanbeluch.com',
    url='https://github.com/jbeluch/githubhooks',
    scripts=['scripts/githubhooks.py'],
    install_requires=['PyGithub'],
)
