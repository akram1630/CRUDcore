from django.urls import path
from . import views

app_name = 'siteui' #for navigation
#              app_name=|name=
#<a href="{% url 'siteui:index' %}">Blog</a>
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    #pk === primary key
    path('show/<int:pk>/', views.show, name='show'),
]
