"""
Celery tasks for the blogtts API.

Tasks
-----
- scrape_blog_post
- scrape_blog_posts
- synthesize_audio
"""

from blogtts.utils.scrape_blog import Scrape
from config import celery_app
from blogtts.utils.tts import MicrosoftT5TTS
from celery import shared_task
from celery import chord
from celery import Task


@celery_app.task(bind=True, max_retries=3)
def scrape_blog_post(url):
    """
    Scrape a blog post and save it to the database.

    Parameters
    ----------
    url : str
        URL of the blog post to scrape.
    """
    from blogtts.api.models import ScrapedArticle

    scrape = Scrape("https://fedgen.ml/content/latest")
    for i in range(scrape.number_of_posts()):
        # if article already exists, skip it
        if not ScrapedArticle.objects.filter(url=scrape.get_url(i)).exists():
            ScrapedArticle.objects.create(
                url=scrape.get_url(i),
                title=scrape.clean_title(i),
                content=scrape.clean_body(i),
                date=scrape.get_post_date(i),
                author=scrape.clean_author(i),
                source="https://fedgen.ml/content/latest",
            )


@celery_app.task(
    bind=True,
    max_retries=3,
    time_limit=3600,
    soft_time_limit=3600,
)
def text_to_audio(self, instance_pk):
    """
    Synthesize audio from text.

    Parameters
    ----------
    instance_pk : str
        Primary key of the ScrapedArticle instance.
    """
    from blogtts.api.models import ScrapedArticle

    article = ScrapedArticle.objects.get(pk=instance_pk)
    text = article.content

    # Synthesize audio
    tts = MicrosoftT5TTS()
    audio = tts.to_wav_in_chunks(
        text, path=f"media/audio/{instance_pk}.wav", chunk_size=100
    )
    article.audio = audio
    article.save()


@shared_task
def convert_content_to_audio(article_id):
    from blogtts.api.models import ScrapedArticle

    article = ScrapedArticle.objects.get(id=article_id)
    text = article.content

    # Synthesize audio
    tts = MicrosoftT5TTS()
    audio = tts.to_wav_in_chunks(
        text, path=f"media/audio/{article_id}.wav", chunk_size=100
    )
    article.audio = audio
    article.save()


@celery_app.task(bind=True, max_retries=3)
def generate_audio(omo):
    """
    Check if there are any articles without audio and synthesize audio for them.
    """
    from blogtts.api.models import ScrapedArticle

    articles = ScrapedArticle.objects.all()

    for article in articles:
        if not article.audio:
            # text_to_audio.delay(article.pk)
            text_to_audio.apply_async(args=[article.pk], queue="dedicated_queue")
