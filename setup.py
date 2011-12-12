#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "django-user-registry",
    version = "0.3",
    url = 'https://github.com/sjzabel/django-user-registry',
    download_url = 'https://github.com/sjzabel/django-user-registry',
    license = 'BSD',
    description = "I think that this is a deprecated package that I need to kill",
    author = 'Stephen J. Zabel',
    author_email = 'sjzabel@gmail.com',
    packages = find_packages(),
    namespace_packages = ['user-registry'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
