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
applications.

If you are on Mac OS X or Linux, chances are the one of the following two
commands will work for you::

   $ sudo easy_install virtualenv

or even better::

   $ sudo pip install virtualenv

One of these will probably install virtualenv on your system. Maybe it's even
in your package manager. If you use Ubuntu, try::

   $ sudo apt-get install python-virtualenv

If you are on Windows (or none of the above methods worked) you must install
``pip`` first. For more information about this, see `installing pip`_.
Once you have it installed, run the ``pip`` command from above, but without
the ``sudo`` prefix.

.. _installing pip: https://pip.readthedocs.io/en/latest/installing.html

Once you have virtualenv installed, just fire up a shell and create your own
environment. You could create a project folder and a `venv` folder within::

   $ mkdir myproject
   $ cd myproject
   $ virtualenv venv

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

   $ pip install virtualenv

A few seconds later and your are good to go.
