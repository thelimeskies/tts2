from django.shortcuts import render
from rest_framework import generics, permissions

from blogtts.api.models import ScrapedArticle
from blogtts.api.serializers import ScrapedArticleSerializer


class ScrapedArticleList(generics.ListAPIView):
    queryset = ScrapedArticle.objects.all()
    serializer_class = ScrapedArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScrapedArticleDetail(generics.RetrieveAPIView):
    queryset = ScrapedArticle.objects.all()
    serializer_class = ScrapedArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
