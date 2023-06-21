from rest_framework import serializers

from blogtts.api import models


class ScrapedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ScrapedArticle
        fields = "__all__"
        read_only_fields = ["audio"]
