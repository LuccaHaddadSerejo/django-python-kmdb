from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict):
        genre_data = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)

        for genre_dict in genre_data:
            genre_obj, created = Genre.objects.get_or_create(name=genre_dict["name"])
            movie.genres.add(genre_obj)
            movie.genres.reverse

        return movie

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]
