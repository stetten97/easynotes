from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)