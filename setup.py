#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='superblock',
      version='0.2.1',
      description='A script written in Python 2 to analyze the superblock of an ' + \
                  'ext2/ext3 formatted file.',
      author='Danilo Bargen',
      author_email='gezuru@gmail.com',
      url='https://github.com/dbrgn/superblock',
      py_modules=['superblock'],
      license='MIT',
      keywords='filesystem superblock ext2 ext3 extfs analyze',
      long_description=open('README.rst').read(),
      entry_points={
          'console_scripts': [
              'superblock = superblock:run',
          ]
      },
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2',
          'Topic :: Education',
          'Topic :: System :: Filesystems',
          'Topic :: Utilities',
      ],
)
