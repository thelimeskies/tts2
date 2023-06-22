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
    def synthesize_audio(self):
        text = self.content

        # Synthesize audio
        tts = MicrosoftT5TTS()
        audio_path = f"media/audio/{self.pk}.wav"
        tts.to_wav_in_chunks(text, path=audio_path, chunk_size=100)
        self.audio.name = audio_path  # Assign the audio file path to the audio field
        self.save()


def create_audio(sender, instance, created, **kwargs):
    if created:
        ScrapedArticle.synthesize_audio()


post_save.connect(create_audio, sender=ScrapedArticle)
