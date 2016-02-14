from os import environ

def load():
    config = {
        "AWS_ACCESS_KEY_ID": None,
        "AWS_SECRET_ACCESS_KEY": None,
        "AWS_REGION": None,
        "API_KEY": None,
    }
    for key in config.keys():
        config[key] = environ[key]
    return config
