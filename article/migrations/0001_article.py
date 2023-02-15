# Generated by Django 4.1.6 on 2023-02-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('slug', models.SlugField(max_length=120, verbose_name='Slug')),
                ('background', models.ImageField(upload_to='article/images', verbose_name='Background Image')),
                ('description', models.CharField(max_length=120, verbose_name='Description')),
                ('content', models.TextField(verbose_name='Content')),
                ('attachment', models.FileField(upload_to='article/files', verbose_name='Attachment')),
                ('uploadtime', models.DateField(auto_now_add=True, verbose_name='Upload Time')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-id'],
            },
        ),
    ]
