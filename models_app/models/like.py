from django.db import models


class Like(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='likes', related_query_name='like')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='likes', related_query_name='like')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = [['photo', 'user']]
        db_table = 'likes'
