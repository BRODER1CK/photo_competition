from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import F
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


class Comment(models.Model):
    text = models.TextField(blank=False)
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    comments = GenericRelation("self")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comments"


@receiver(post_save, sender=Comment)
def update_comment_count_on_comment_create(sender, instance, created, **kwargs):
    if created:
        parent = instance.content_object

        while parent.__class__.__name__ != "Photo":
            parent = parent.content_object

        parent.comment_count = F("comment_count") + 1
        parent.save(update_fields=["comment_count"])


@receiver(post_delete, sender=Comment)
def update_comment_count_on_comment_delete(sender, instance, **kwargs):
    parent = instance.content_object

    if parent:

        while parent.__class__.__name__ != "Photo":
            parent = parent.content_object

        parent.comment_count = F("comment_count") - 1
        parent.save(update_fields=["comment_count"])
