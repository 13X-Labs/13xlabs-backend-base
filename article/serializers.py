from rest_framework import serializers, viewsets
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'