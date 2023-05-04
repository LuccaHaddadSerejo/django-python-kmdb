import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stars = models.IntegerField(
        validators=[
            MinValueValidator(
                1, message="O valor mínimo permitido para as estrelas é 1."
            ),
            MaxValueValidator(
                5, message="O valor máximo permitido para as estrelas é 5."
            ),
        ]
    )
    review = models.TextField()
    spoilers = models.BooleanField(blank=True, default=False)
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
