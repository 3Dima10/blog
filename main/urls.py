from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:pk>", views.nowels.as_view(), name="nowel"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("forma", views.create, name="create"),
    path("<int:pk>/delete", views.delete.as_view(), name="delete"),
]
