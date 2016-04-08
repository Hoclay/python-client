Running tests
-------------

To run the tests with your installed python version:

.. code-block:: bash

    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ py.test

To run the full set of tests against multiple versions of python (requires Docker):

.. code-block:: bash

    $ make test
