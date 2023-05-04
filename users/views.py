from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrCreateUser
from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreateUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer
