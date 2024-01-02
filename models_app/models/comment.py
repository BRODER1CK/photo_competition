from django.db import models


class Comment(models.Model):
    text = models.TextField(blank=False)
    photo = models.ForeignKey('Photo',
                              on_delete=models.CASCADE,
                              related_name='comments',
                              related_query_name='comment')
    user = models.ForeignKey('User',
                             on_delete=models.CASCADE,
                             related_name='comments',
                             related_query_name='comment')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comments'