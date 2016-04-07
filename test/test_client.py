import handwriting


def test_list_handwritings(client):
  hws = client.list_handwritings()
  assert hws

  hws = client.list_handwritings({'limit': 1})
  assert len(hws) == 1


def test_get_handwriting(client, test_handwriting):
  hw = client.get_handwriting(test_handwriting['id'])
  assert hw == test_handwriting
