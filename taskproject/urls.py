"""
URL configuration for taskproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from riderapp.views import UserViewSet, LoginViewSet,MatchRideView

router = routers.DefaultRouter()
router.register('create', UserViewSet, basename='user')
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('',include('riderapp.urls')),
    path('rides/match/', MatchRideView.as_view(), name='ride-match'),
    # path('rides/<int:pk>/accept/', AcceptRideView.as_view(), name='ride-accept'),
]

