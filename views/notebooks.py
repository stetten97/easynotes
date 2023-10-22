from flask import Blueprint, render_template, request, redirect, url_for, flash
from easynotes.models.models import Notebook, Note, db
import sys

notebooks = Blueprint('notebooks', __name__)

@notebooks.route('/go_to_notebooks')
def move_to_notebooks():
    return redirect('/notebooks')

@notebooks.route('/notebooks', methods=['GET', 'POST'])
def show_notebooks():
    notebooks = Notebook.query.all()
    return render_template('notebooks.html', notebooks=notebooks)

@notebooks.route('/create_notebook', methods=['GET', 'POST'])
def create_notebook():
    if request.method == 'POST':
        name = request.form.get('notebook_name')
        new_notebook = Notebook(name=name)
        db.session.add(new_notebook)
        db.session.commit()
        return redirect('/notebooks')
    
@notebooks.route('/delete/<int:id>', methods=['GET'])
def delete_notebook(id):
    notebook_to_delete = Notebook.query.get_or_404(id)
    db.session.query(Note).filter_by(notebook_id=notebook_to_delete.id).delete()
    db.session.delete(notebook_to_delete)
    db.session.commit()
    return redirect('/notebooks')

@notebooks.route('/rename/<int:id>', methods=['GET', 'POST'])
def rename_notebook(id):
    notebook_to_rename = Notebook.query.get_or_404(id)
    print(notebook_to_rename.name, file=sys.stdout)
    if request.method == 'POST':
        new_name = request.form.get('notebook_name')
        notebook_to_rename.name = new_name
        db.session.commit()
        return redirect('/notebooks')
    else:
        return render_template("rename_notebook.html", notebook=notebook_to_rename)   