from flask import Blueprint, render_template, request, redirect
from easynotes.models.models import Notebook, Note, db

notes = Blueprint('notes', __name__)

@notes.route('/notes/<int:id>')
def show_notes(id):
    notebook = Notebook.query.get_or_404(id)
    notes = Note.query.filter_by(notebook_id=notebook.id).all()

    return render_template('notes.html', 
                            notebook=notebook,
                            notes=notes)

@notes.route('/go_to_notes/<int:id>')
def move_to_notes(id):
    return redirect(f'/notes/{id}')

@notes.route('/create_note/<int:notebook_id>', methods=['POST'])
def write_note(notebook_id):
    content = request.form.get('note_content')
    new_note = Note(title='Title', content=content, notebook_id=notebook_id)
    db.session.add(new_note)
    db.session.commit()
    return redirect(f'/notes/{notebook_id}')

def delete_note():
    pass

def modify_note():
    pass
