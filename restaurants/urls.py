from django.urls import path

from .views      import CategoryMainView, ListPageView

urlpatterns = [
    path('/categories',CategoryMainView.as_view()),
    path('/list',ListPageView.as_view()),
]
