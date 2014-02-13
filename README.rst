===========
TransIP API
===========

.. image:: https://travis-ci.org/mhogerheijde/transip-api.png?branch=develop
   :align: right
   :target: https://travis-ci.org/mhogerheijde/transip-api

This library aims to implement the `TransIP API`_ in Python.

Quick Start
===========

Prerequisite
------------

* Make sure you have an account at TransIP_
* *Enable* the API (https://www.transip.nl/cp/mijn-account/#api)
* Add your IP.
* Generate key-pairs
	+ Copy-paste the key into a file.
	+ Encrypt the key ``$ openssl enc -aes-256-cbc -in new_key -out encrypted_key``
	+ Decrypt it again (for now, only unencrypted RSA is supported) ``$ openssl rsa -in encrypted_key -out decrypted_key``
	+ put decrypted key next to this readme

Setup
-----

.. code-block::

	$ python setup.py install


Example
-------

The command-line interpreter is a bit silly right now, it only does a
getDomainNames() call.

.. code-block::

	$ transip-api
	[example.com, example.org, example.net]


Documentation
=============

Further documentation can be found in the ``docs`` directory, although this is
not filled in yet.

.. _virtualenv: http://virtualenv.org/
.. _TransIP: https://www.transip.nl/cp/
.. _`TransIP API`: https://www.transip.eu/transip/api/

