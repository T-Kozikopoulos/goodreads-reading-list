from django import forms
from .models import Book


# Setting up a form for adding new books to the collection,
# using Django's built-in ModelForm.
class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Book
        fields = ['url', 'title', 'author']
        required = ['url', 'title', 'author']
