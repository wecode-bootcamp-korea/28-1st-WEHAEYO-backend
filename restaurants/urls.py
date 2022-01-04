from django.urls import path

from .views      import CategoryMainView

urlpatterns = [
    path('/main_page',CategoryMainView.as_view()),
]
