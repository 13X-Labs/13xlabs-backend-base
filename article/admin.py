from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'active')
	list_filter = ('active', 'title')
	search_fields = ('title', 'content')