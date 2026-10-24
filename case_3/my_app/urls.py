from django.urls import path
from .views import index, main
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', index, name='index'),
    path('user/<str:name>/', views.main, name='hello'),
]

