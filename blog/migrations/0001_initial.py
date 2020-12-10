# Generated by Django 3.1.4 on 2020-12-10 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(null=True, upload_to='images/blog/thumbnails/', verbose_name='Ufak Resim')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Tarih')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'verbose_name': 'Blog Yazısı',
                'verbose_name_plural': 'Blog Yazıları',
                'ordering': ('-id',),
            },
        ),
    ]
