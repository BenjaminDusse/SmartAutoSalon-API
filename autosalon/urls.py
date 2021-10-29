from django.urls import path
from .views import UserListView, CarModelListView, OrderListView, OrderDetailView

urlpatterns = [
    path("user-list/", UserListView.as_view(), name="user-list"),
    path("car-model-list/", CarModelListView.as_view(), name="car-model-list"),
    path("order-list/", OrderListView.as_view(), name="order-list"),
    path("order-detail/<int:pk>/", OrderDetailView.as_view(), name="order-detail")
]