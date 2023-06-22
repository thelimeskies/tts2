import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from blogtts.api.tasks import convert_content_to_audio


class ScrapedArticle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    summary = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to="audio/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

# @receiver(post_save, sender=ScrapedArticle)
# def create_audio(sender, instance, created, **kwargs):
#     if created:
#         convert_content_to_audio.delay(instance.id)