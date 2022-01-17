
from django.urls import path
from django.urls.conf import include
from rest_framework import views
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from .views import isAdmin

router = DefaultRouter()
router.register('users', UserViewSet)
# router.register('isAdmin', IsAdmin)


urlpatterns = [
    path('', include(router.urls)),
    path('isAdmin', isAdmin)

]
