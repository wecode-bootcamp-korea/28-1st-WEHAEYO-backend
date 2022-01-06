from django.urls import path

from .views      import CategoryMainView, RestaurantDetailView, RestaurantListView

urlpatterns = [
    path('/categories',CategoryMainView.as_view()),
    path('/list',RestaurantListView.as_view()),
    path('/<int:restaurant_id>', RestaurantDetailView.as_view()),
]