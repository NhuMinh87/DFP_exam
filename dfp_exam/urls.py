from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('/books/')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('', include('accounts.urls')),
]