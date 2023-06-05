from django.urls import path
from .views import signupfunc, loginfucn, listfunc, logoutfunc, detailfunc, goodfunc ,readfunc, ImgCreate
urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfucn, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/',logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/',ImgCreate.as_view(), name='create'),
]
