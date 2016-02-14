
from flask import Flask

from workwork import config as _config
from workwork.api import instance


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = _config.load()
    app.config.update(config)

    app.register_blueprint(instance.blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
