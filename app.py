from flask import Flask
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def hello_word():
    return '<h1>hello world</h1>'

if __name__ == "__main__":
    app.run(debug=True)