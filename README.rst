ipynbcompress
=============

|build-status-image| |pypi-version| |wheel|

Overview
--------

So you have included an image with ``IPython.display.Image()`` and the
file size of your IPython Notebook got huge? No problem! This package
will resize images in your notebook and compress them as JPG or PNG.

Installation
------------

Install using ``pip``...

.. code:: bash

    pip install ipynbcompress

Example
-------

TODO: Write example.

API reference
-------------

API reference is at http://ipynbcompress.rtfd.org.

Development
-----------

Install dependencies and link development version of ipynbcompress to
pip:

.. code:: bash

    git clone https://github.com/arve0/ipynbcompress
    cd ipynbcompress
    pip install -r requirements.txt # install dependencies and ipynbcompress-package

Testing
~~~~~~~

.. code:: bash

    tox

Build documentation locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation:

.. code:: bash

    pip install -r docs/requirements.txt
    make docs

.. |build-status-image| image:: https://secure.travis-ci.org/arve0/ipynbcompress.png?branch=master
   :target: http://travis-ci.org/arve0/ipynbcompress?branch=master
.. |pypi-version| image:: https://pypip.in/version/ipynbcompress/badge.svg
   :target: https://pypi.python.org/pypi/ipynbcompress
.. |wheel| image:: https://pypip.in/wheel/ipynbcompress/badge.svg
   :target: https://pypi.python.org/pypi/ipynbcompress
