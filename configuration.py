from routes.home import home_route
from routes.market import market_route
from routes.register import register_route
from database.database import db
from database.models.product import Product


def configure_all(app):
    configure_routes(app)
    #configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(market_route, url_prefix='/market')
    app.register_blueprint(register_route, url_prefix='/register')


def configure_db():
    db.connect()
    db.create_tables([Product])
