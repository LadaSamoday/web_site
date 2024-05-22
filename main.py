from flask import Flask, render_template, request, redirect
from data_base import get_notes, get_tags, init_db, get_note, update_note_db, add_note_db, delete_note_db
from forms import NoteForm, TagForm



app = Flask(__name__)

init_db()
@app.route('/')
def start():
    notes = get_notes()
    return render_template('site.html', notes=notes)

@app.route('/<int:id>', methods=['GET', 'POST'])
def update_note(id):
    form = NoteForm(request.form)
    if request.method == 'POST' and form.validate():
        update_note_db(id, form.note_name.data, form.note.data)
        return redirect('/')
    note = get_note(id)
    form.note_name.data = note[1]
    form.note.data = note[2]
    # form.tag.data = get_tags(id)
    return render_template('update_note.html', form=form)


@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    form = NoteForm(request.form)
    if request.method == 'GET':
        return render_template('update_note.html', form=form)
    if request.method == 'POST':
        if form.validate():
            add_note_db(form.note_name.data, form.note.data)
            return redirect('/')

@app.route('/delete/<int:id>')
def delete_note(id):
    delete_note_db(id)
    return redirect('/')




@app.route('/about')
def about():
    return render_template('about.html')







