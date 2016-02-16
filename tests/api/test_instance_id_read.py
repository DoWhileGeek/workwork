from workwork.errors import InstanceIdNotFound


def test_instance_id_read_happy_path(client, mocker, instance_payload):
    mocker.patch("workwork.platform.instance.get_instance")

    resp = client.get("/instance/us-west-2/some_id/", headers=instance_payload.to_dict())
    assert resp.status_code == 200


def test_instance_id_read_resource_not_found(client, mocker, instance_payload):
    mocker.patch("workwork.platform.instance.get_instance", side_effect=InstanceIdNotFound)

    resp = client.get("/instance/us-west-2/some_id/", headers=instance_payload.to_dict())
    assert resp.status_code == 404
