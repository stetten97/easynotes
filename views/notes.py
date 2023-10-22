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

@notes.route('/delete_note/<int:id>', methods=['GET'])
def delete_note(id):
    note_to_delete = Note.query.get_or_404(id)
    db.session.delete(note_to_delete)
    db.session.commit()
    return redirect(f'/notes/{note_to_delete.notebook_id}')
    
@notes.route('/edit_note/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note_to_edit = Note.query.get_or_404(id)
    if request.method == 'POST':
        note_to_edit.content = request.form.get('note_content')
        db.session.commit()
        return redirect(f'/notes/{note_to_edit.notebook_id}')
    else:
        return render_template('edit_note.html', note=note_to_edit)
