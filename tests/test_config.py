from workwork import config as _config


def test_config_load(config):
    assert _config.load() == config
