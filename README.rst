Handwriting.io Python Client
============================

.. image:: https://circleci.com/gh/handwritingio/python-client.svg?style=svg&circle-token=4526b4c3cf9d8fb76b63f7f706233d8af6b80a39
    :target: https://circleci.com/gh/handwritingio/python-client


Installation
------------

.. code-block:: bash

    $ pip install handwritingio


Basic Example
-------------

Set up the client, render an image, and write it to a file:

.. code-block:: python

    import handwritingio

    hwio = handwritingio.Client('KEY', 'SECRET')
    image = hwio.render_png({
      'handwriting_id': '2D5S46A80003', # found in our catalog or by listing handwritings
      'text': 'Handwriting with Python!',
      'height': 'auto',
    })
    with open('handwriting.png', 'wb') as f:
      f.write(image)

If all goes well, this should create an image similar to the following:

.. image:: https://d2igm8ue20pook.cloudfront.net/python-client-example.png


.. TODO: advanced examples: list handwritings (with params)


Reference
---------

See the `API Documentation <https://handwriting.io/docs/>`_ for details on
all endpoints and parameters. For the most part, the ``Client`` passes the
parameters through to the API directly.

The endpoints map to client methods as follows:

- `GET /handwritings <https://handwriting.io/docs/#get-handwritings>`_ -> ``Client.list_handwritings([params])``
- `GET /handwritings/{id} <https://handwriting.io/docs/#get-handwritings--id->`_ -> ``Client.get_handwriting(handwriting_id)``
- `GET /render/png <https://handwriting.io/docs/#get-render-png>`_ -> ``Client.render_png(params)``
- `GET /render/pdf <https://handwriting.io/docs/#get-render-pdf>`_ -> ``Client.render_pdf(params)``


Issues
------

Please open an issue on `Github <https://github.com/handwritingio/python-client>`_
or `contact us <https://handwriting.io/contact>`_ directly for help with any
problems you find.
