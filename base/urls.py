from django.urls import path
from .views import Home, ItemDetail, NewItem, UpdateItem, DeleteItem, CustomLoginView

urlpatterns = [
    path("login", CustomLoginView.as_view(), name="login"),
    path("", Home.as_view(), name="home"),
    path("item/<int:pk>/", ItemDetail.as_view(), name="item"),
    path("new-item", NewItem.as_view(), name="new-item"),
    path("edit-item/<int:pk>/", UpdateItem.as_view(), name="edit-item"),
    path("delete-item/<int:pk>/", DeleteItem.as_view(), name="delete-item"),
]   