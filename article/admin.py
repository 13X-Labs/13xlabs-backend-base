from django.contrib import admin
from .models import Article, Category
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeRelatedFieldListFilter

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'active')
	list_filter = ('active', 'title')
	search_fields = ('title', 'content')

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
	list_display = ('title', 'slug')
	list_filter = ('title', 'slug')
	search_fields = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}
	DraggableMPTTAdmin.list_display = ('tree_actions', 'indented_title', 'related_articles_count', 'related_articles_cumulative_count')
	mptt_level_indent = 20