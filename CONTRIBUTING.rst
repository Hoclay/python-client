Contributing
============

Please open an issue on `Github <https://github.com/handwritingio/python-client>`_
or `contact us <https://handwriting.io/contact>`_ directly for help with any
problems you find.

If you'd like to make changes to this code, please submit a Pull Request.


Running tests
-------------

To quickly run the tests against your installed Python version, use the test
command from ``setup.py``. This assumes that the API is running locally.

.. code-block:: bash

    $ python setup.py test


If you need to run the tests against a different API server, you will need to
provide a URL and credentials as environment variables:

.. code-block:: bash

    $ API_URL=https://api.handwriting.io API_KEY=123456 API_SECRET=ABCDEF python setup.py test


To run the full set of tests against multiple versions of Python, the project
uses Docker and tox. If you have the API running locally in Docker, you can run
tests with just:

.. code-block:: bash

    $ make test

Again, the API url and credentials can be overridden, except in this case these
must be passed as make variables:

.. code-block:: bash

    $ make test API_URL=https://api.handwriting.io API_KEY=123456 API_SECRET=ABCDEF


When using ``make test``, the Docker image will be (re)built as necessary and
the entire set of tests will run on each version of Python configured, so this
can be somewhat slow. For fast iteration, the ``py.test`` method will probably
work best, but make sure to run the full suite occasionally to check that your
changes are compatible.


Code Style
----------

Please follow the `PEP-8 <https://www.python.org/dev/peps/pep-0008/>`_ style
guide with one exception: indent with two spaces.
