from rest_framework import serializers
from .models import Review
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    critic = serializers.SerializerMethodField()

    def get_critic(self, obj: User):
        return {
            "id": obj.critic.id,
            "first_name": obj.critic.first_name,
            "last_name": obj.critic.last_name,
        }

    class Meta:
        model = Review
        fields = ["id", "stars", "review", "spoilers", "critic", "movie_id"]
