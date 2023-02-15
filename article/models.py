from django.db import models

# Create your models here.
class Article(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=120, verbose_name='Title')
	slug = models.SlugField(max_length=120, verbose_name='Slug')
	background = models.ImageField(upload_to='article/images', verbose_name='Background Image')
	description = models.CharField(max_length=120, verbose_name='Description')
	content = models.TextField(verbose_name='Content')
	attachment = models.FileField(upload_to='article/files', verbose_name='Attachment')
	uploadtime = models.DateField(auto_now_add=True, verbose_name='Upload Time')
	active = models.BooleanField(default=True, verbose_name='Active')

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'
		ordering = ['-id']
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'