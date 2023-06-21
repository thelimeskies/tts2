from django.urls import path
from blogtts.api import views

urlpatterns = [
    path("scraped-articles/", views.ScrapedArticleList.as_view()),
    path("scraped-articles/<int:pk>/", views.ScrapedArticleDetail.as_view()),
]
