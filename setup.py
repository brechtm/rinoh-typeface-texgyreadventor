#!/bin/env python

from setuptools import setup, find_packages


NAME = 'TeX Gyre Adventor'
LICENSE = 'GUST Font License (GFL)'

TYPEFACE_ID = ''.join(char for char in NAME if char.isalnum()).lower()
PACKAGE_NAME = 'rinoh-typeface-{}'.format(TYPEFACE_ID)
PACKAGE_DIR = PACKAGE_NAME.replace('-', '_')


setup(
    name=PACKAGE_NAME,
    version='0.1.0',
    packages=find_packages(),
    package_data={PACKAGE_DIR: ['*.otf', '*.txt']},
    install_requires=['rinohtype'],
    provides=[PACKAGE_DIR],
    entry_points={
        'rinoh_typefaces':
            ['{} = {}:typeface'.format(TYPEFACE_ID, PACKAGE_DIR)]
    },

    author='Brecht Machiels',
    author_email='brecht@mos6581.org',
    description='TeX Gyre Adventor typeface',
    url='https://github.com/brechtm/rinoh-typeface-texgyreadventor',
    keywords='opentype font',
    license=LICENSE,
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Fonts',
    ]
)
