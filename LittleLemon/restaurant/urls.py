from django.urls import path
from . import views


urlpatterns = [
    path('menu', views.MenuItemsView.as_view()),
]
