import flask
import flask_restless
from flask_cors import CORS

from config import config
import os

def create_app(app, config_name):
    """
    Generate app based on Flask instance.

    :type config_name: string
    :param config_name: Config Type (i.e. development, staging, production).

    :rtype: Object
    :return: Flask Object.
    """

    # Load generic configs.
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Save environment type
    app.config['ENVIRONMENT'] = config_name

    # Init database from environment variable.
    # databases_conf = app.config['GENERAL']['databases']
    # app.config['SQLALCHEMY_DATABASE_URI'] = databases_conf[database_engine]
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #
    # from api_0_1.models.model import db
    # db.init_app(app)
    # db.app = app
    #
    # # Import model classes.
    # from api_0_1.models.status import Status
    #
    # # Create db if not exist (defined at above models).
    # db.create_all()

    # Import views clasess.
    from api_0_1.views.statuses import Satuses

    Satuses = Satuses()

    # Register Blueprint for Non RESTfull routes.
    from api_0_1.views.endpoints import custom_api as custom_api_0_1_blueprint
    app.register_blueprint(custom_api_0_1_blueprint, url_prefix = Satuses.url_prefix)

    # Create the Flask-Restless API manager.
    # manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

    # Create API endpoints.
    # manager.create_api(
    #     Status,
    #     url_prefix=Satuses.url_prefix,
    #     methods=Satuses.methods,
    #     include_columns=Satuses.include_columns,
    #     exclude_columns=Satuses.exclude_columns,
    #     preprocessors=Satuses.preprocessors,
    #     postprocessors=Satuses.postprocessors
    # )

    return app


try:
    if os.environ['ENV']:
        environment = os.environ['ENV']
except KeyError, e:
    environment = 'development'

# try:
#     if os.environ['DATABASE']:
#         database = os.environ['DATABASE']
# except KeyError, e:
#     database = 'mysql'

app = flask.Flask(__name__)
create_app(app, environment)
CORS(
    app,
    origins='*',
    supports_credentials=True,
    expose_headers=['Content-Length'],
    allow_headers=['Content-Type', 'Authorization']
)
