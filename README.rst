===========
TransIP API
===========

.. image:: https://travis-ci.org/benkonrath/transip-api.png?branch=develop
   :align: right
   :target: https://travis-ci.org/benkonrath/transip-api

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
	+ Reformat the key ``$ openssl rsa -in input.key -out decrypted_key``
	+ put decrypted key next to this readme

Setup
-----

.. code-block::

	$ python setup.py install


Example
-------

The command-line interpreter doesn't do much yet. By default it does a
getDomainNames() call, but with the '-u' option it's also possible to add or
update DNS records. When calling it with '-h', it will show all available options.

.. code-block::

	$ transip-api
	[example.com, example.org, example.net]
	
	$ transip-api -h
	usage: transip-api [-h] [-l LOGINNAME] [-s] [-a] [-u] [-d]
	                   [--domain-name DOMAIN_NAME] [--entry-name ENTRY_NAME]
	                   [--entry-expire ENTRY_EXPIRE] [--entry-type ENTRY_TYPE]
	                   [--entry-content ENTRY_CONTENT] [--api-key PRIVATE_KEY_FILE]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -l LOGINNAME, --login-name LOGINNAME
	                        TransIP username
	  -s, --show-dns-entries
	                        show all DNS entries for a domain
	  -a, --add-dns-entry   add an entry in the DNS
	  -u, --update-dns-entry
	                        update an entry in the DNS
	  -d, --delete-dns-entry
	                        delete an entry in the DNS
	  --domain-name DOMAIN_NAME
	                        domain name to use
	  --entry-name ENTRY_NAME
	                        name of the DNS entry
	  --entry-expire ENTRY_EXPIRE
	                        expire time of the DNS entry
	  --entry-type ENTRY_TYPE
	                        type of the DNS entry
	  --entry-content ENTRY_CONTENT
	                        content of the DNS entry
          --api-key PRIVATE_KEY_FILE
                                TransIP private key


Example of adding/updating a record:

.. code-block::

	$ transip-api -l githubuser -u --api-key privatekey --domain-name example.com --entry-name testentry --entry-expire 86400 --entry-type A --entry-content 127.0.0.1
	Request finished successfully.


Documentation
=============

Further documentation can be found in the ``docs`` directory, although this is
not filled in yet.

.. _virtualenv: http://virtualenv.org/
.. _TransIP: https://www.transip.nl/cp/
.. _`TransIP API`: https://www.transip.eu/transip/api/

FAQ
===

Question:

    When using the library I get SSL errors such as:

    .. code-block::
    
        urllib2.URLError: <urlopen error [Errno 1] _ssl.c:510: error:14077458:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 unrecognized name>
   
Answer:

    The `suds` library has fairly limited SSL support which is dependent on the Python version, to work around this the `suds_requests` library can be used which replaces `urllib2` with the `requests` library. Additionally the `requests` library automatically pools connections which makes the library slightly faster to use.
   To install:
   
    .. code-block::
    
       pip install suds_requests
