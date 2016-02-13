
from flask import Flask

from workwork.config import load


def create_app(config=None):
    if config is None:
        config = load()

    app = Flask(__name__)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
