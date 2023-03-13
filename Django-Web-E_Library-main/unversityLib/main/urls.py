from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('search/', include('search_book.urls'), name='search-book'),

]
