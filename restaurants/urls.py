from django.urls import path

from .views      import CategoryMainView, RestaurantListView

urlpatterns = [
    path('/categories',CategoryMainView.as_view()),
    path('/list',RestaurantListView.as_view()),
]