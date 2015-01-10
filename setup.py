from setuptools import setup

import transip

setup(
    name = transip.__name__,
    version = transip.__version__,
    author = transip.__author__,
    author_email = transip.__email__,
    license = transip.__license__,
    description = transip.__doc__.splitlines()[0],
    long_description = open('README.rst').read(),
    url = 'http://github.com/goabout/transip-backup',
    download_url = 'http://github.com/goabout/transip-backup/archives/master',
    packages = ['transip', 'transip.service'],
    include_package_data = True,
    zip_safe = False,
    platforms = ['all'],
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'transip-api = transip.transip_cli:main',
        ],
    },
    install_requires = [
        'requests',
    ],
)

