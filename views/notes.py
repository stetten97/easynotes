from flask import Flask, Blueprint, render_template, request, redirect, url_for
from models import Notebook, db

bp = Blueprint('notes', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/notebooks', methods=('GET', 'POST'))
def show_notebooks():
    notebooks = Notebook.query.all()
    return render_template('notebooks.html', notebooks=notebooks)

@bp.route('/create_notebook', methods=('GET', 'POST'))
def create_notebook():
    if request.method == 'POST':
        content = request.form.get('content')
        new_notebook = Notebook(name=content)
        db.session.add(new_notebook)
        db.session.commit()
        return redirect('/notebooks')