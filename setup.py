from setuptools import setup

import transip_api

setup(
    name = transip_api.__name__,
    version = transip_api.__version__,
    author = transip_api.__author__,
    author_email = transip_api.__email__,
    license = transip_api.__license__,
    description = transip_api.__doc__.splitlines()[0],
    long_description = open('README.rst').read(),
    url = 'http://github.com/goabout/transip-backup',
    download_url = 'http://github.com/goabout/transip-backup/archives/master',
    packages = ['transip_api'],
    include_package_data = True,
    zip_safe = False,
    platforms = ['all'],
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'transip-backup = transip_api.client:main',
        ],
    },
    install_requires = [
        'requests',
    ],
)

