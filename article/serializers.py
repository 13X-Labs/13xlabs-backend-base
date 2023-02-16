from rest_framework import serializers, viewsets
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        base_url = 'http://127.0.0.1:8000/api/post/'
        return base_url + obj.slug

    class Meta:
        model = Article
        fields = '__all__'