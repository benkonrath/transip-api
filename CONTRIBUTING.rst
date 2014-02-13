==========
Contribute
==========

This project uses git & python.

Setup
=====

In order to contribute, please start by making your own fork_ of this
repository, and proceed to clone your own nifty fork to your local machine.
	
Isolating the Python environment with virtualenv_ is recommended. Use the
following commands to set up a development environment within the Git workspace:

.. code-block::

	$ virtualenv .
	$ . bin/activate
	(transip-api) $ pip install -r dev_requirements.txt

Or by using virtualenvwrapper_:

.. code-block::

	$ mkvirtualenv transip-api
	$ cd /path/to/clone
	$ setvirtualenvproject

Proceed to using pip to install all the dependencies

.. code-block::

	$ pip install -r dev_requirements.txt


Pull-Request
============

Please make sure that you make a separate branch for the changes you propose.
Subsequent commits to the same branch as the Pull-Request originated from will
be picked up by GitHub and added to the Pull-Request.

This is quite handy to change things when there are comments about the
changeset, but can be annoying if not taken into account. If you make a Pull-
Request from your develop branch and you continue developing, all new commits
get added to the Pull-Request, which is clearly not wanted.


Testing
=======

This project uses `unittest` to automatically test the software. Every Pull
Request should contain tests, unless it is clear why they are not needed. (e.g.
document change only, bugfixes that don't change behaviour)

TravisCI
--------

When a Pull-Request is made, TravisCI_ will automatically pick it up and test it
using the settings from .travis.yml. The results will be made available both on
GitHub with the Pull-Request, as on the specific page for this repository at
TravisCI_: https://travis-ci.org/mhogerheijde/transip-api. If anything fails,
you can see the specifics about the failure there.

Obviously, Pull-Request that fail the test will not be merged.


.. _virtualenv: https://github.com/pypa/virtualenv
.. _virtualenvwrapper: https://github.com/bernardofire/virtualenvwrapper
.. _fork: https://github.com/goabout/goabout-backend/fork
.. _TravisCI: https://travis-ci.org/
