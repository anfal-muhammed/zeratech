

# Create your views here.
from rest_framework import viewsets, status, generics
from .models import Ride
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer, RideSerializer, RideStatusUpdateSerializer


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'})
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RideListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class RideRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class RideStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideStatusUpdateSerializer


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MatchRideView(generics.ListAPIView):
    serializer_class = RideSerializer

    def get_queryset(self):
        user = self.request.user
        # Implement your matching algorithm here (e.g., proximity-based matching)
        rides = Ride.objects.filter(status='PENDING')
        # Return the matched rides for the user (driver)
        return rides


class AcceptRideView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer