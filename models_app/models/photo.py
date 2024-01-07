from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django_fsm import FSMField, transition

from models_app.models.comment import Comment


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='P')


class Photo(models.Model):
    STATUS_CHOICES = [
        ('M', 'Ожидает модерацию'),
        ('P', 'Опубликовано'),
        ('D', 'На удалении')
    ]

    title = models.CharField(max_length=255, verbose_name='Название')
    status = FSMField(choices=STATUS_CHOICES, default='M', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    description = models.TextField(verbose_name='Описание')
    current_photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фотография')
    previous_photo = models.ImageField(blank=True, null=True, verbose_name='Предыдущая фотография')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='photos', related_query_name='photo', verbose_name='Автор')
    comments = GenericRelation(Comment)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
        db_table = 'photos'
        ordering = ['-updated_at']
        indexes = [
            models.Index(fields=['-updated_at'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('web_site:photo', kwargs={'photo_id': self.id})