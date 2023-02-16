from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

class Category(MPTTModel):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=120, verbose_name='Title')
	slug = models.SlugField(max_length=120, verbose_name='Slug')
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Parent Category')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article:category', kwargs={'slug': self.slug})
	
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ['-id']
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class Article(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
	title = models.CharField(max_length=120, verbose_name='Title')
	slug = models.SlugField(max_length=120, verbose_name='Slug')
	background = models.ImageField(upload_to='article/images', verbose_name='Background Image')
	description = models.CharField(max_length=120, verbose_name='Description')
	content = RichTextField(config_name='default', verbose_name='Content')
	attachment = models.FileField(upload_to='article/files', verbose_name='Attachment')
	uploadtime = models.DateField(auto_now_add=True, verbose_name='Upload Time')
	active = models.BooleanField(default=True, verbose_name='Active')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article:article', kwargs={'slug': self.slug})
	
	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'
		ordering = ['-id']
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'