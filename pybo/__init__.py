from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
    
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # APP
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    from . import models
    db.init_app(app)
    migrate.init_app(app, db)    
    
    # Blueprint
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    
    return app


# if __name__ == "__main__":
#     app.run(debug=True)