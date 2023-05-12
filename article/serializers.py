from rest_framework import serializers
from article.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    image = serializers.ImageField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Article
        fields = ["title", "content", "finished_at",
                  "category", "product", "image"]


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title", "content", "category"]


class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ["title", "user", "finished_at", "product"]


class BookmarkSerializer(serializers.ModelSerializer):
    bookmarked = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = [
            'bookmarked',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content",]


class BiddingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'max_user', 'max_point']
