from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top/', views.top, name='top'),
    path('after10/', views.after10, name='after10'),
    path('register/', views.register, name='register'),
    path('counselling/', views.counselling, name='counselling'),
    path('trusts/', views.trusts, name='trusts'),
    # url(r'^register/$', views.user_register, name='user_register')
]
