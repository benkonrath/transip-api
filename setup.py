from setuptools import setup

import transip

setup(
    name=transip.__name__,
    version=transip.__version__,
    author=transip.__author__,
    author_email=transip.__email__,
    license=transip.__license__,
    description=transip.__doc__.splitlines()[0],
    long_description=open('README.rst').read(),
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

