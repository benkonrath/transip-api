=========
Changelog
=========

This document records all notable changes to `transip-api <https://github.com/benkonrath/transip-api>`_.
This project adheres to `Semantic Versioning <http://semver.org/>`_.

`1.0.1`_ (2019-03-17)
---------------------

* Fixed bytes input for cryptography library

`1.0.0`_ (2019-03-15)
---------------------

* Added cryptography as an optional replacement for rsa library (cryptography doesn't require the private key to be converted)
* Fixed ordering Vps
* Added option to clone Vps
* Added availability zones for Vps
* Added option to specify private key directly

`0.4.1`_ (2018-08-03)
---------------------

* Many improvements and bug fixes

`0.4.0`_ (2018-05-31)
---------------------

* Many improvements and bug fixes

`0.3.0`_ (2017-03-19)
---------------------

* Initial public release, versions 0.1.0 and 0.2.0 have been skipped to miminize interference when publishing to PyPi


.. _0.3.0: https://github.com/benkonrath/transip-api/commit/73925ff
.. _0.4.0: https://github.com/benkonrath/transip-api/compare/0.3.0...0.4.0
.. _0.4.1: https://github.com/benkonrath/transip-api/compare/0.4.0...0.4.1
.. _1.0.0: https://github.com/benkonrath/transip-api/compare/0.4.1...v1.0.0
.. _1.0.1: https://github.com/benkonrath/transip-api/compare/v1.0.0...v1.0.1
