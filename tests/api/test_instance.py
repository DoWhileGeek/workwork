import json

from workwork.errors import InvalidInstanceId


def test_instance_post_happy_path(client, mocker):
    mocker.patch("workwork.platform.instance.set_instance_state")

    resp = client.post("/instance/some_id/start/")
    assert resp.status_code == 204


def test_instance_post_invalid_instance_id(client, mocker):
    mocker.patch("workwork.platform.instance.set_instance_state", side_effect=InvalidInstanceId())

    resp = client.post("/instance/some-invalid-id/start/")
    assert resp.status_code == 422

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'instance_id', 'title': 'Invalid instance id'}]}


def test_instance_post_invalid_action(client):
    resp = client.post("/instance/some_id/derp/")
    assert resp.status_code == 422

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'action', 'title': 'Invalid action'}]}


def test_instance_post_invalid_action_case(client):
    resp = client.post("/instance/some_id/Start/")
    assert resp.status_code == 422

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'action', 'title': 'Invalid action'}]}


def test_instance_post_invalid_region(client):
    resp = client.post("/instance/some_id/start/", data=json.dumps({"region": "us-derp-1"}), content_type="application/json")
    assert resp.status_code == 422

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'region', 'title': 'Invalid region'}]}
