from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"

db = SQLAlchemy(app)

class Note(db.Model):
    pass

if __name__ == "__main__":
    app.run(debug=True)