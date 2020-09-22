from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='books_index'),
    path('delete/<pk>', views.BookDelete.as_view(), name="delete_book"),
]
