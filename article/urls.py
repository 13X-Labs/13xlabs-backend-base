from django.urls import path
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')

urlpatterns = [
	path('', include(router.urls)),
	path('post/<str:slug>', ArticleViewSet.as_view({'get': 'retrieveSlug'}), name='article-detail'),
	path('post/<str:slug>/', ArticleViewSet.as_view({'get': 'retrieveSlug'}), name='article-detail'),
	path('api-auth/', include('rest_framework.urls')),
]