from flask import Blueprint, render_template, request, redirect, url_for
from models import Notebook, db
import sys

notebooks = Blueprint('notebooks', __name__)

@notebooks.route('/')
def home():
    return render_template('home.html')

@notebooks.route('/go_to_notebooks', methods=('GET', 'POST'))
def move_to_notebooks():
    print("Button request is received", file=sys.stdout)
    return redirect('/notebooks')

@notebooks.route('/notebooks', methods=('GET', 'POST'))
def show_notebooks():
    notebooks = Notebook.query.all()
    return render_template('notebooks.html', notebooks=notebooks)

@notebooks.route('/create_notebook', methods=('GET', 'POST'))
def create_notebook():
    if request.method == 'POST':
        content = request.form.get('content')
        new_notebook = Notebook(name=content)
        db.session.add(new_notebook)
        db.session.commit()
        return redirect('/notebooks')