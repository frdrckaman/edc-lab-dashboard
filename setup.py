# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages
from os.path import join, abspath, normpath, dirname

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = ["edc_test_utils"]
with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='edc-lab-dashboard',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/clinicedc/edc-lab-dashboard',
    license='GPL license, see LICENSE',
    description='Lab dashboard views for clinic/edc projects',
    long_description=README,
    zip_safe=False,
    keywords='Edc lab dashboard views',
    install_requires=[
        'edc-constants',
        'edc-dashboard',
        'edc-lab',
        'edc-label',
        'edc-model',
        'edc-model-wrapper',
        'edc-navbar',
        'edc_utils',
        'reportlab',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)
