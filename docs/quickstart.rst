Quickstart
==========

.. currentmodule:: transip-api

You can get the library directly from PyPI::

    pip install transip-api

The installation into a :ref:`virtualenv` is heavily recommended.

.. _virtualenv:

virtualenv
----------

Virtualenv is probably what you want to use for developing Python
applications. Simply fire up a shell and create your own isolated
Python environment in the `venv` folder::

   $ mkdir myproject
   $ cd myproject
   $ python -m venv venv

Now, whenever you want to work on a project, you only have to activate the
corresponding environment. On Mac OS X and Linux, do the following::

   $ . venv/bin/activate

If you are on Windows, use the following command::

   $ venv\scripts\activate

Either way, you should now be using your virtualenv (notice how the promt of
you shell has changed to show the active environment).

And if you want to exit your virtualenv, use the following command::

   $ deactivate

Enter the following command to get transip-api installed in your virtualenv::

   $ pip install transip

A few seconds later and your are good to go.
