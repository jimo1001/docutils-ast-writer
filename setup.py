#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import rst2ast as this

setup(
    name='docutils-ast-writer',
    description='AST Writer for docutils',
    version=this.__version__,
    author=this.__author__,
    author_email=this.__author_email__,
    license=this.__license__,
    url='https://github.com/iij/docutils-ast-writer',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'docutils'
    ],
    entry_points="""
        [console_scripts]
        rst2ast = rst2ast:main
    """
)
