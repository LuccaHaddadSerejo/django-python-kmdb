from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from .models import Review
from .permissions import IsAdminOrCritic
from .serializers import ReviewSerializer


class ReviewView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCritic]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(movie_id=self.kwargs["movie_id"])

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs["movie_id"])
        serializer.save(critic=self.request.user, movie=movie)
