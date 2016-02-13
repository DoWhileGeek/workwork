
from flask import Flask

from workwork import config as _config


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = _config.load()
    app.config.update(config)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
