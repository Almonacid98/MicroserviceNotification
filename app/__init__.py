from flask import Flask
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from app.routes import Route


db = SQLAlchemy()
migrate = Migrate()

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    db.init_app(app)
    migrate.init_app(app, db)

    route = Route()
    route.init_app(app)
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app