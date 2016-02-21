import logging
import json

from flask import jsonify


LOGGER = logging.getLogger(__name__)

def register_error_handlers(app):
    @app.errorhandler(422)
    def handle_bad_request(err):
        # webargs attaches additional metadata to the `data` attribute
        data = getattr(err, 'data')

        messages = []
        if data:
            # Get validations from the ValidationError object
            for parameter, parameter_messages in data['exc'].messages.items():
                for message in parameter_messages:
                    payload = {
                        "id": parameter,
                        "title": message,
                    }
                    messages.append(payload)
        else:
            messages.append({"title": "Invalid Request"})

        print(json.dumps({"errors": messages}))

        return jsonify({
            'errors': messages,
        }), 422

    @app.errorhandler(APIException)
    def handle_APIException(err):
        return jsonify(err.to_dict()), err.status_code


class APIException(Exception):
    def __init__(self, exception_id, title, status_code, payload=None):
        self.exception_id = exception_id
        self.title = title
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        if self.payload:
            return self.payload
        else:
            return {
                "errors": [{
                    "id": self.exception_id,
                    "title": self.title,
                }, ],
            }


class InvalidApiKey(APIException):
    def __init__(self, exception_id="api_key", title="Invalid api key", status_code=401, payload=None):
        super().__init__(exception_id, title, status_code, payload)


class InstanceIdNotFound(APIException):
    def __init__(self, exception_id="instance_id", title="instance_id not found", status_code=404, payload=None):
        LOGGER.warn("instance_id not found")
        print("instance_id not found")
        super().__init__(exception_id, title, status_code, payload)


class InvalidRegion(APIException):
    def __init__(self, exception_id="region", title="Invalid region", status_code=422, payload=None):
        super().__init__(exception_id, title, status_code, payload)


class InvalidAction(APIException):
    def __init__(self, exception_id="action", title="Invalid action", status_code=422, payload=None):
        super().__init__(exception_id, title, status_code, payload)

