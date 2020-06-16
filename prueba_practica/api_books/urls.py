from django.urls import path
from . import views
from .views import AuthorApiView, AuthorDetailApiView, BooksApiView

urlpatterns = [
    # path(r'', views.home, name=''),
    #API's urls
    path(r'',views.home, name= 'home'),
    path(r'api/autor/',AuthorApiView.as_view(), name ='autorapiview' ),
    path(r'api/autor/<int:pk>',AuthorDetailApiView.as_view(), name ='authordetailapiview' ),
    path(r'api/libro/',BooksApiView.as_view(), name ='booksapiview' ),
]