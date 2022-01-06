from django.urls import path

from .views      import CategoryMainView, RestaurantDetailView

urlpatterns = [
    path('/categories',CategoryMainView.as_view()),
    path("/<int:restaurant_id>", RestaurantDetailView.as_view())
]
