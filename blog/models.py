from django.db import models
from django.db.models import Model, CharField, DateTimeField, ImageField,  ForeignKey, TextField, BooleanField
from django_extensions.db.fields import AutoSlugField


class Blog(Model):
    author = ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE)
    title = CharField(max_length=100, verbose_name='Başlık')
    slug = AutoSlugField(populate_from='title')
    content = TextField(verbose_name='İçerik')
    is_active = BooleanField(default=False, verbose_name='Aktif')
    created_at = DateTimeField(auto_now_add=True, editable=False, verbose_name='Oluşturma Tarihi')
    updated_at = DateTimeField(auto_now=True, editable=False, verbose_name='Güncelleme Tarihi')


    class Meta:
        ordering = ('-id',)
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'

    def __str__(self):
        return self.title