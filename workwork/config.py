from os import environ

def load():
    config = {}
    params = ["AWS_PUBLIC_KEY", "AWS_SECRET_KEY", "AWS_REGION"]
    for param in params:
        config[param] = environ[param]
    return config
