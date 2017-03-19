#!/usr/bin/env python
import os
import re
import codecs
from setuptools import setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='transip',
    version=find_version('transip', '__init__.py'),
    author='Go About B.V.',
    author_email='tech@goabout.com',
    maintainer='Ben Konrath',
    maintainer_email='ben@bagu.org',
    license='MIT',
    description='TransIP API Connector',
    long_description=read('README.rst'),
    url='https://github.com/benkonrath/transip-api',
    packages=['transip', 'transip.service'],
    include_package_data=True,
    zip_safe=False,
    platforms=['all'],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'transip-api=transip.transip_cli:main',
        ],
    },
    install_requires=[
        'requests',
        'rsa',
        'suds-jurko',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)

