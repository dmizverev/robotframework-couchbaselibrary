"""Setup module for Robot Framework Couchbase Library"""

from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get install requires from requirements.txt
with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='robotframework-couchbaselibrary',
    version='1.0.0',
    description='A Robot Framework library to work with Couchbase',
    long_description=long_description,
    url='https://github.com/peterservice-rnd/robotframework-couchbaselibrary',
    license='Apache License, Version 2.0',
    author='JSC PETER-SERVICE',
    author_email='drse_aist_all@billing.ru',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Robot Framework :: Library',
    ],
    keywords='testing robotframework couchbase',
    package_dir={'': 'src'},
    py_modules=['CouchbaseLibrary'],
    install_requires=requirements,
)