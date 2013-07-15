#!/usr/bin/env python

from setuptools import setup, Extension

import sys


setup(
    name="blitzy",
    description="A friendly layer atop Loopy for generating OpenCL kernels in Python.",
    long_description="",
    classifiers=['Development Status :: 3 - Alpha',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.7',
                 ],
    author="Alex Rubinsteyn",
    author_email="alexr@cs.nyu.edu",
    license="BSD",
    version="0.1",
    url="http://github.com/iskandr/blitzy",
    packages=[ 'blitzy'],
    requires=['loopy', 'numpy' ] 
    )
