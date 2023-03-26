from .views import AllKeywordsView
from django.urls import path

urlpatterns = [
    path('',AllKeywordsView.as_view())
]
