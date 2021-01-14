from django.urls import path
from . import views
urlpatterns =  [
    path('test/', views.index, name='index'),
    path('thankyou/', views.responseform, name='responseform'),
    #path('response/', views.responseform, name='responseform'),
]