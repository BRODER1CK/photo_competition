from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    text = models.TextField(blank=False)
    # photo = models.ForeignKey('Photo',
    #                           on_delete=models.CASCADE,
    #                           related_name='comments',
    #                           related_query_name='comment')
    user = models.ForeignKey('User',
                             on_delete=models.CASCADE,
                             related_name='comments',
                             related_query_name='comment')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    comments = GenericRelation('self')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comments'
