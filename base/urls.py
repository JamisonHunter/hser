from django.urls import path
from .views import Home, ItemDetail, NewItem

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("item/<int:pk>/", ItemDetail.as_view(), name="item"),
    path("new-item", NewItem.as_view(), name="new-item"),
]   