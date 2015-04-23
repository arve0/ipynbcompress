#!/usr/bin/env python

import os
import sys
from setuptools import setup

os.system('make rst')
try:
    readme = open('README.rst').read()
except FileNotFoundError:
    # fallback when installing from source package
    readme = ''

setup(
    name='ipynbcompress',
    version=open(os.path.join('ipynbcompress', 'VERSION')).read().strip(),
    description='Compress images in IPython/Jupyter notebooks',
    long_description=readme,
    author='Arve Seljebu',
    author_email='arve.seljebu@gmail.com',
    url='https://github.com/arve0/ipynbcompress',
    packages=[
        'ipynbcompress',
    ],
    package_dir={'ipynbcompress': 'ipynbcompress'},
    package_data={'ipynbcompress': ['VERSION']},
    scripts=[
        'scripts/ipynb-compress'
    ],
    include_package_data=True,
    install_requires=[
        'Pillow',
        'jsonschema',
        'ipython',
        'climate',
        'hurry.filesize'
    ],
    license='MIT',
    zip_safe=False,
    keywords='ipynbcompress',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
