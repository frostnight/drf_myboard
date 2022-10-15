from rest_framework import serializers

from .models import Post
from users.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    # nested serializer
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date", "likes")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")
