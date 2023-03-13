from django.urls import path
from . import views

def ret_req(request):
    print(request)
    return request.POST['searched']

urlpatterns = [
    path('', views.index, name='search-book'),
    path('book-info/<int:book_id>/', views.show_book, name='book-info')
]
