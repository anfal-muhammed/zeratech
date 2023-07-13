from django.urls import path
from . import views

urlpatterns = [
    path('trip/', views.RideListCreateAPIView.as_view(), name='ride-list'),
    path('trip/<int:pk>/', views.RideRetrieveAPIView.as_view(), name='ride-detail'),
path('trip/<int:pk>/update/', views.RideStatusUpdateAPIView.as_view(), name='ride-status-update'),


]
