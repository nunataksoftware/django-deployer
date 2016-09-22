# -*- coding: utf-8 -*-

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-deployer',
    version='0.1',
    packages=['deployer'],
    include_package_data=True,
    license='MIT License',
    description='Helper utility to continuosly deploy django projects using an url',
    long_description=README,
    url='https://github.com/nunataksoftware/django-deployer',
    author=u'Guillermo Nuñez',
    author_email='gui.nunez@gmail.com',
    install_requires=[
        'GitPython',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
