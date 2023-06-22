from django.contrib import admin

# Register your models here.
from blogtts.api.models import ScrapedArticle

admin.site.register(ScrapedArticle)