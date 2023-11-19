from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Notebook(db.Model):
    """
    A class for a collection of notes.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    notes = db.relationship('Note', backref='notebook', lazy=True)

    __table_args__ = (
        db.CheckConstraint('name <> ""'),
        )

class Note(db.Model):
    """
    One note in a notebook.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'), nullable=False)

    __table_args__ = (
        db.CheckConstraint('content <> ""'),
        )