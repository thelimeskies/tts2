import uuid

from django.db import models
from django.db.models.signals import post_save

from blogtts.utils.tts import MicrosoftT5TTS


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

    @classmethod
    def syntenize_audio(cls, pk):
        article = cls.objects.get(pk=pk)
        text = article.content

        # Synthesize audio
        tts = MicrosoftT5TTS()
        audio = tts.to_wav_in_chunks(text, path=f"media/audio/{pk}.wav", chunk_size=100)
        article.audio = audio
        article.save()


def create_audio(sender, instance, created, **kwargs):
    if created:
        ScrapedArticle.syntenize_audio(instance.pk)


post_save.connect(create_audio, sender=ScrapedArticle)
