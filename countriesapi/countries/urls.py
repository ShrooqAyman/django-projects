from django.urls import path, include
from .views import CountryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
