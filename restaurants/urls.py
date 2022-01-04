from django.urls import path

from .views      import CategoryMainView

urlpatterns = [
    path('/categories',CategoryMainView.as_view()),
]
