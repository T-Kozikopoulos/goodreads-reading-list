from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy


# Setting up the homepage of the site. Making sure the user must sing up/in to use it.
@login_required
def index(request):
    # Users can see only list associated with them.
    books = Book.objects.filter(user=request.user)

    # Use the form created in forms.py and make sure all data provided is legit.
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        saved = form.save(commit=False)
        saved.save()
        # Upon successfully adding a new book to the self, reload the page.
        return redirect('books_index')

    context = {
        'books': books,
        'form': form
    }
    return render(request, 'books/index.html', context)


# Make deleting objects easier by using Django's DeleteView.
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books_index')
    template_name = 'books/delete_book.html'
