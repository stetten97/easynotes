from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Notebook(db.Model):
    """
    A class for a collection of notes.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    notes = db.relationship('Notes', backref='notebook', lazy=True)

class Note(db.Model):
    """
    One note in a notebook.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'), nullable=False)