#!/usr/bin/env python

from distutils.core import setup

setup(name='cvdarts',
      version='0.1',
      description='Darts score perception using opencv',
      author='nluede',
      author_email='niels@nlue.de',
      url='https://github.com/nluede/cvDarts',
      packages=['cvdarts'], requires=['opencv-python', 'numpy']
      )
