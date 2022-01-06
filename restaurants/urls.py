from django.urls import path

from .views      import RestaurantDetailView
# , MenuOptionView, ReviewView

urlpatterns = [
    path("/<int:restaurant_id>", RestaurantDetailView.as_view())
    # path("/option/<int:menu_id>", MenuOptionView.as_view()),
    # path("/review/<int:restaurant_id>", ReviewView.as_view())
]
