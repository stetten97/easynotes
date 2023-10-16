from flask import Blueprint, render_template

base_bp = Blueprint('base', __name__)

@base_bp.route('/')
def home():
    return render_template('home.html')

from .notebooks import notebooks
from .notes import notes
base_bp.register_blueprint(notebooks)
base_bp.register_blueprint(notes)