from django.urls import path

from .views      import DetailView

urlpatterns = [
    path("/<int:restaurant_id>", DetailView.as_view()),
]
