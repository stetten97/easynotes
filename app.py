from flask import Flask
from flask_migrate import Migrate
from models import db
from views.notes import bp

app = Flask(__name__)
app.register_blueprint(bp)

# app.register_blueprint(bp)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"

migrate = Migrate(app, db)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)