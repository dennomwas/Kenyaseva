# app/__init__.py

# third-party imports
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# initialize db
db = SQLAlchemy()

# initialize login manager
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    # register blueprints
    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.donors import donor as donor_blueprint
    app.register_blueprint(donor_blueprint)

    # error page handlers
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html',
                               title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html',
                               title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html',
                               title='Server Error'), 500

    return app

