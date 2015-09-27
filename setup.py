#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_fbcomments

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_fbcomments.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

long_description = open('README.rst').read()

setup(
    name='djangocms-fbcomments',
    version=version,
    description="""The easiest way to integrate Facebook Comments for your django-cms powered site with lazy-loading, analytics and more.""",
    long_description=long_description,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/djangocms-fbcomments',
    packages=[
        'djangocms_fbcomments',
    ],
    include_package_data=True,
    install_requires=[
        'django-appconf',
        'django-cms>=3.0',
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangocms-fbcomments, facebook, django-cms, cmsplugin-fbcomments',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
