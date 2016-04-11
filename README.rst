Handwriting.io Python Client
============================

.. image:: http://handwriting.io/images/hwio_logo_black.png
        :target: https://handwriting.io


Code Status
-----------

.. image:: https://circleci.com/gh/handwritingio/handwriting-python.svg?style=svg&circle-token=4526b4c3cf9d8fb76b63f7f706233d8af6b80a39
    :target: https://circleci.com/gh/handwritingio/handwriting-python


Installation
------------

.. code-block:: bash

    $ pip install handwritingio


Basic Usage
-----------

.. code-block:: python

    import handwritingio

    hwio = handwritingio.Client('KEY', 'SECRET')
    handwritings = hwio.list_handwritings()
    image = hwio.render_png({
      'handwriting_id': handwritings[0]['id'],
      'text': 'Handwriting with python!'
    })
    with open('handwriting.png', 'wb') as f:
      f.write(image)


.. TODO: embed the resulting image here
