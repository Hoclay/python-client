Running tests
-------------

To quickly run the tests against your installed Python version, use ``py.test``.
First, install the requirements (inside a virtualenv is recommended), then run
the test. This assumes that the API is running locally:

.. code-block:: bash

    $ pip install -e .
    $ pip install -r requirements-dev.txt
    $ py.test -v


If you need to run the tests against a different API server, you will need to
provide a URL and credentials as environment variables:

.. code-block:: bash

    $ API_URL=https://api.handwriting.io API_KEY=123456 API_SECRET=ABCDEF py.test -v


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
