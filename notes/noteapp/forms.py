from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Note, Author


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class NoteForm(ModelForm):

    quote = CharField(min_length=3, max_length=500, required=True, widget=TextInput())

    class Meta:
        model = Note
        fields = ['quote']
        exclude = ['tags', 'authors']

