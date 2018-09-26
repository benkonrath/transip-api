Welcome to transip-api's documentation!
=======================================

This library aims to implement the TransIP API in Python.

Here is an example of a simple Python program:

.. code-block:: python

   from transip.service.vps import VpsService


   client = VpsService('accountname')

   # Order a Vps without addons:
   client.order_vps('vps-bladevps-x1', None, 'ubuntu-18.04', 'vps-name')

You can get the library directly from PyPI::

   pip install transip-api

Documentation
-------------

This part of the documentation quides you through all of the library's
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
