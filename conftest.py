from os import environ

import pytest

from workwork.server import create_app


@pytest.fixture
def config():
    _config = {
        "AWS_ACCESS_KEY_ID":     "abc-123",
        "AWS_SECRET_ACCESS_KEY": "def-456",
        "AWS_REGION":            "us-west-2",
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

