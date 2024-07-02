from django.urls import path
from .views import Home, ItemDetail, NewItem, UpdateItem, DeleteItem, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", Home.as_view(), name="home"),
    path("item/<int:pk>/", ItemDetail.as_view(), name="item"),
    path("new-item/", NewItem.as_view(), name="new-item"),
    path("edit-item/<int:pk>/", UpdateItem.as_view(), name="edit-item"),
    path("delete-item/<int:pk>/", DeleteItem.as_view(), name="delete-item"),
]   