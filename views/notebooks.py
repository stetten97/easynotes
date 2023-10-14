from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Notebook, db
import sys

notebooks = Blueprint('notebooks', __name__)

@notebooks.route('/home')
def home():
    return render_template('home.html')

@notebooks.route('/go_to_notebooks')
def move_to_notebooks():
    return redirect('/notebooks')

@notebooks.route('/notebooks', methods=['GET', 'POST'])
def show_notebooks():
    notebooks = Notebook.query.all()
    return render_template('notebooks.html', notebooks=notebooks)

@notebooks.route('/create', methods=['GET', 'POST'])
def create_notebook():
    if request.method == 'POST':
        content = request.form.get('content')
        new_notebook = Notebook(name=content)
        db.session.add(new_notebook)
        db.session.commit()
        return redirect('/notebooks')
    
@notebooks.route('/delete/<int:id>', methods=['GET'])
def delete_notebook(id):
    notebook_to_delete = Notebook.query.get_or_404(id)
    db.session.delete(notebook_to_delete)
    db.session.commit()
    return redirect('/notebooks')

@notebooks.route('/rename/<int:id>', methods=['GET', 'POST'])
def rename_notebook(id):
    notebook_to_rename = Notebook.query.get_or_404(id)
    if request.method == 'POST':
        notebook_to_rename.name = request.form.get('content')
        db.session.commit()
        return redirect('/notebooks')
    else:
        return render_template("rename_notebook.html", notebook=notebook_to_rename)


    