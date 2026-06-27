"""
Package: service

Creates and configures the Flask app. Sets the CORS policy, attaches
Flask-Talisman security headers, wires up logging, and initializes the
database before loading the routes and error handlers.
"""
import os
import sys
import logging
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

# Create the Flask app
app = Flask(__name__)

# ---------------------------------------------------------------
# DATABASE CONFIG
# ---------------------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URI", "sqlite:///test.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ---------------------------------------------------------------
# CORS POLICY
# Allows the API to be called from any front-end client.
# Tighten "origins" to your real domain(s) before going to production.
# ---------------------------------------------------------------
CORS(app, resources={r"/*": {"origins": "*"}})

# ---------------------------------------------------------------
# TALISMAN SECURITY HEADERS
# Adds X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security,
# Content-Security-Policy, etc. force_https is False so local/dev/test
# runs over plain HTTP still work; set it True behind a real TLS terminator.
# ---------------------------------------------------------------
talisman = Talisman(app, force_https=False)

# ---------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

# Import routes and error handlers AFTER the app is created to avoid
# circular imports.
from service import routes              # noqa: F401, E402
from service.common import error_handlers  # noqa: F401, E402
from service.models import init_db          # noqa: E402

try:
    init_db(app)
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)

app.logger.info("Service initialized!")
