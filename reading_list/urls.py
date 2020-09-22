from django.contrib import admin
from django.urls import path, include


# Set up all the paths for the pages of the website. 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    # Include the urls from our books model. Doing it this way to increase readability.
    path('', include('books.urls')),
]
