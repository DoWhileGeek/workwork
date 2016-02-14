from flask import current_app

from workwork.errors import InvalidApiKey

def validate_api_key(api_key):
    if current_app.config["API_KEY"] != api_key:
        raise InvalidApiKey
