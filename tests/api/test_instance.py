import json


def test_instance_start_happy_path(client):
    resp = client.post("/instance/some-id/start/")
    assert resp.status_code == 204
