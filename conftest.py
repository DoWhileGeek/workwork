from os import environ

import pytest


@pytest.fixture
def config():
    _config = {
        "AWS_PUBLIC_KEY": "abc-123",
        "AWS_SECRET_KEY": "def-456",
        "AWS_REGION":     "us-west-2",
    }

    for key, value in _config.items():
        environ[key] = value

    return _config
