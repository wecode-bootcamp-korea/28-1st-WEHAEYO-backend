from django.urls import path

from .views      import CategoryMainView

urlpatterns = [
    path('/main-page',CategoryMainView.as_view()),
]
