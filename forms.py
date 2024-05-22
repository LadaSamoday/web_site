from wtforms import Form, StringField, validators, SubmitField, TextAreaField,\
                    FieldList, FormField


class TagForm(Form):
    tag_name = StringField('tag', [validators.length(max=30, min=1)])
class NoteForm(Form):
    note_name = StringField('note_name', [validators.Length(max=30, min=1)])
    note = TextAreaField('note')
    tag = FieldList(FormField(TagForm))
    submit = SubmitField(label='Отправить')





