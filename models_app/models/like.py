from django.db import models
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Like(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='likes', related_query_name='like')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='likes', related_query_name='like')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = [['photo', 'user']]
        db_table = 'likes'


@receiver(post_save, sender=Like)
def update_like_count_on_like_create(sender, instance, created, **kwargs):
    if created:
        photo = instance.photo
        photo.like_count = F('like_count') + 1
        photo.save(update_fields=['like_count'])


@receiver(post_delete, sender=Like)
def update_like_count_on_like_delete(sender, instance, **kwargs):
    photo = instance.photo
    photo.like_count = F('like_count') - 1
    photo.save(update_fields=['like_count'])
