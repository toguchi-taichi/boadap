from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logout_func, detailfunc, goodfunc, readfunc, BoadCreate
 
urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logout_func, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoadCreate.as_view(), name='create')
]