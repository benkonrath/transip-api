Welcome to transip-api's documentation!
=======================================

This library aims to implement the `TransIP SOAP V5 API`_ in Python. The SOAP V5 API is marked as **deprecated** by TransIP, users are strongly advised to switch to the new `TransIP REST API V6`_.

If you would like to use the new `TransIP REST API V6`_, please consider using `python-transip`_ instead.

.. _`TransIP SOAP V5 API`: https://api.transip.eu/docs/transip.nl/package-Transip.html
.. _`TransIP REST API V6`: https://api.transip.eu/rest/docs.html
.. _`python-transip`: https://github.com/roaldnefs/python-transip

Here is an example of a simple Python program:

.. code-block:: python

   from transip.service.vps import VpsService


   PRIVATE_KEY = '''
   -----BEGIN PRIVATE KEY-----
   ...
   -----END PRIVATE KEY-----
   '''

   # You can specify the private key directly or supply the path to the private
   # key file. The private_key_file will default to `decrypted_key`.
   client = VpsService('accountname', private_key_file='/path/to/decrypted_key')
   client = VpsService('accountname', private_key=PRIVATE_KEY)

   # Order a Vps without addons:
   client.order_vps('vps-bladevps-x1', None, 'ubuntu-18.04', 'vps-name')

You can get the library directly from PyPi::

   pip install transip

Documentation
-------------

This part of the documentation guides you through all of the library's
usage patterns.

.. toctree::
   :maxdepth: 2

   quickstart
   cli
   api

Miscellaneous Pages
-------------------

.. toctree::
   :maxdepth: 2

   contrib
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
