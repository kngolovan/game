"""Entry point of our application."""
from flask import Flask

from app.views import bp


def create_app(test_config=None):
    """Create and configure an instance of the application."""
    from app.models import db  # pylint: disable=import-outside-toplevel

    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_pyfile("config.py")

    app.register_blueprint(bp)
    app.add_url_rule("/", endpoint="index")

    db.init_app(app)

    return app
