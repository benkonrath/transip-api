===========
TransIP API
===========

.. image:: https://travis-ci.org/mhogerheijde/transip-api.png?branch=develop
   :align: right
   :target: https://travis-ci.org/mhogerheijde/transip-api

This library aims to implement the `TransIP API`_ in Python.

Usage
=====

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

.. code-block::

	$ transip-api
	[example.com, example.org, example.net]


Contribute
==========

This project uses git & python.

You can fork this repository:

.. code-block::

	https://github.com/goabout/goabout-backend/fork
	
Isolating the Python environment with virtualenv_ is recommended. Use the following commands to set up a development environment within the Git workspace:

.. code-block::

	virtualenv .
	. bin/activate
	pip install -r dev_requirements.txt

Documentation
=============

The documentation can be found in the ``docs`` directory.

.. _virtualenv: http://virtualenv.org/
.. _TransIP: https://www.transip.nl/cp/
.. _`TransIP API`: https://www.transip.eu/transip/api/

