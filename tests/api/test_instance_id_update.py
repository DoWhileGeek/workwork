import json

from workwork.errors import InstanceIdNotFound


def test_instance_post_happy_path(client, mocker, instance_payload):
    mocker.patch("workwork.platform.instance.set_instance_state")

    resp = client.post("/instance/us-west-2/some_id/start/", **instance_payload.to_json())
    assert resp.status_code == 204


def test_instance_post_invalid_api_key(client, mocker, instance_payload):
    instance_payload["api_key"] = "wrong_api_key"

    resp = client.post("/instance/us-west-2/some_id/start/", **instance_payload.to_json())
    assert resp.status_code == 401

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'api_key', 'title': 'Invalid api key'}]}


def test_instance_post_instance_id_not_found(client, mocker, instance_payload):
    mocker.patch("workwork.platform.instance.set_instance_state", side_effect=InstanceIdNotFound)

    resp = client.post("/instance/us-west-2/some_invalid_id/start/", **instance_payload.to_json())
    assert resp.status_code == 404

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'instance_id', 'title': 'instance_id not found'}]}


def test_instance_post_invalid_action(client, instance_payload):
    resp = client.post("/instance/us-west-2/some_id/derp/", **instance_payload.to_json())
    assert resp.status_code == 422

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'action', 'title': 'Invalid action'}]}


def test_instance_post_invalid_action_case(client, instance_payload):
    resp = client.post("/instance/us-west-2/some_id/Start/", **instance_payload.to_json())
    assert resp.status_code == 422

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'action', 'title': 'Invalid action'}]}


def test_instance_post_invalid_region(client, instance_payload):
    resp = client.post("/instance/derp/some_id/start/", **instance_payload.to_json())
    assert resp.status_code == 422

    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {'errors': [{'id': 'region', 'title': 'Invalid region'}]}
