Handwriting.io Python Client
============================

.. image:: https://circleci.com/gh/handwritingio/handwriting-python.svg?style=svg&circle-token=4526b4c3cf9d8fb76b63f7f706233d8af6b80a39
    :target: https://circleci.com/gh/handwritingio/handwriting-python

.. image:: http://handwriting.io/images/hwio_logo_black.png
        :target: https://handwriting.io

Running tests
-------------

.. code-block:: bash

    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ py.test

To run the tests against multiple versions of python:

.. code-block:: bash

    $ python setup.py test

You will need to have each of the tested versions of python installed on your
system.
