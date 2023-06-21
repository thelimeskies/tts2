"""
Celery tasks for the blogtts API.

Tasks
-----
- scrape_blog_post
- scrape_blog_posts
- synthesize_audio
"""

from blogtts.api.models import ScrapedArticle
from blogtts.utils.scrape_blog import Scrape
from config import celery_app


@celery_app.task(bind=True, max_retries=3)
def scrape_blog_post(url):
    """
    Scrape a blog post and save it to the database.

    Parameters
    ----------
    url : str
        URL of the blog post to scrape.
    """
    scrape = Scrape(url)
    for i in range(scrape.get_num_posts()):
        # if article already exists, skip it
        if not ScrapedArticle.objects.filter(url=scrape.get_url(i)).exists():
            ScrapedArticle.objects.create(
                url=scrape.get_url(i),
                title=scrape.clean_title(i),
                content=scrape.clean_body(i),
                date=scrape.get_date(i),
                author=scrape.get_author(i),
                source=url,
            )


@celery_app.task(bind=True, max_retries=3)
def content_to_audio(pk):
    """
    Synthesize audio from the content of a blog post.

    Parameters
    ----------
    pk : int
        Primary key of the blog post.
    """
    article = ScrapedArticle.objects.get(pk=pk)
    article.synthesize_audio()
