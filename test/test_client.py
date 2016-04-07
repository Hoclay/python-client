def test_list_handwritings(client):
  hws = client.list_handwritings()
  assert hws

  hws = client.list_handwritings({'limit': 1})
  assert len(hws) == 1


def test_get_handwriting(client, test_handwriting):
  hw = client.get_handwriting(test_handwriting['id'])
  assert hw == test_handwriting


def test_render_png(client, test_handwriting):
  image = client.render_png({
      'handwriting_id': test_handwriting['id'],
      'text': 'Hello world!',
  })
  assert image
  assert isinstance(image, bytes)


def test_render_pdf(client, test_handwriting):
  image = client.render_pdf({
      'handwriting_id': test_handwriting['id'],
      'text': 'Hello world!',
  })
  assert image
  assert isinstance(image, bytes)
