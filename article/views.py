from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	# def list(self, request):
	# 	queryset = Article.objects.all()
	# 	serializer_class = ArticleSerializer(queryset, many=True)
	# 	return Response(serializer_class.data)

	# def retrieve(self, request, pk=None, slug=None):
	# 	queryset = Article.objects.all()
	# 	articlepost = get_object_or_404(queryset, pk=pk)
	# 	serializer_class = ArticleSerializer(articlepost)
	# 	return Response(serializer_class.data)
	
	def retrieveSlug(self, request, slug=None):
		queryset = Article.objects.all()
		articlepost = get_object_or_404(queryset, slug=slug)
		serializer_class = ArticleSerializer(articlepost)
		return Response(serializer_class.data)