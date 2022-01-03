from django.urls import path

from .views      import CategoryMainView

urlpatterns = [
    path('',CategoryMainView.as_view()),
]
