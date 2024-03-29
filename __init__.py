from flask import Flask
from flask_migrate import Migrate
from easynotes.models.models import db
from easynotes.views.base import base_bp

app = Flask(__name__)
app.secret_key = "test_key"
app.register_blueprint(base_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"

migrate = Migrate(app, db)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)