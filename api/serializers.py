from rest_framework import serializers
from api.models import Advisers, Services, Features, Offers, Blog, Clients, Admin, Comments, Review


class AdvisersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisers
        fields = ('id', 'slug', 'first_name', 'last_name', 'seen', 'image', 'education')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'adviser', 'rating', 'comment', 'created_at']


class AdvisersSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Advisers
        fields = ['id', 'first_name', 'last_name', 'reviews', 'seen', 'image', 'education']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'slug', 'title', 'description', 'seen', 'image')


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('id', 'slug', 'title', 'description', 'seen', 'logo')


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = ('id', 'slug', 'title', 'description', 'seen', 'image')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'slug', 'first_name', 'last_name', 'username', 'image', 'seen', 'password')


class BlogSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()

    class Meta:
        model = Blog
        fields = ('id', 'slug', 'title', 'description', 'seen', 'admin', 'image')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'slug', 'first_name', 'last_name', 'nickname', 'seen', 'education', 'image')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'service', 'client')
