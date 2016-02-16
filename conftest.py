import json
from os import environ

import pytest

from workwork.server import create_app


@pytest.fixture
def config():
    _config = {
        "AWS_ACCESS_KEY_ID":     "abc-123",
        "AWS_SECRET_ACCESS_KEY": "def-456",
        "API_KEY":               "2eb05a35-1bb4-4900-a247-1aa5166ddf99",
    }

    for key, value in _config.items():
        environ[key] = value

    return _config


@pytest.fixture
def app(config):
    _app = create_app(config=config)
    _app.config["DEBUG"] = True
    return _app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def instance_payload(config):
    payload = {
        "api_key": config["API_KEY"],
    }

    return Payload(payload)


class Payload:
    def __init__(self, payload):
        self.payload = payload

    def __getitem__(self, key):
        return self.payload[key]

    def __setitem__(self, key, value):
        self.payload[key] = value

    def __delitem__(self, key):
        del self.payload[key]

    def to_json(self):
        return {
            "data": json.dumps(self.payload),
            "content_type": "application/json",
        }

    def to_dict(self):
        return self.payload
