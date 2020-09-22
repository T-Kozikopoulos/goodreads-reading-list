from django.contrib import admin
from .models import Book


# Adding Book model to the admin panel.
class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)
