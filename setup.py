#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import rst2ast as this

setup(
    name='docutils-ast-writer',
    description='AST Writer for docutils',
    version='0.1.0',
    author='jimo1001',
    author_email='jimo1001@gmail.com',
    license='MIT',
    url='https://github.com/jimo1001/docutils-ast-writer',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'docutils>=0.12'
    ],
    entry_points="""
        [console_scripts]
        rst2ast = rst2ast.cmd:run
    """
)
