from os import environ

def load():
    config = {"AWS_PUBLIC_KEY": None, "AWS_SECRET_KEY": None, "AWS_REGION": None}
    for key in config.keys():
        config[key] = environ[key]
    return config
