import uuid
from rest_framework import generics, permissions, views

from rest_framework.response import Response

# import status
from rest_framework import status

from blogtts.api.models import ScrapedArticle
from blogtts.api.serializers import ScrapedArticleSerializer, TTSSerializer
from blogtts.utils.tts import MicrosoftT5TTS
from django.conf import settings


class ScrapedArticleList(generics.ListAPIView):
    queryset = ScrapedArticle.objects.all()
    serializer_class = ScrapedArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScrapedArticleDetail(generics.RetrieveAPIView):
    queryset = ScrapedArticle.objects.all()
    serializer_class = ScrapedArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ConvertTTSView(views.APIView):
    serializer_class = TTSSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        text = request.data["text"]
        tts = MicrosoftT5TTS()
        audio = tts.synthesize(text)
        filename = f"{uuid.uuid4()}.wav"
        with open(f"{settings.MEDIA_ROOT}/{filename}", "wb") as f:
            f.write(audio)
        if not audio:
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"audio": f"{settings.MEDIA_URL}{filename}"}, status=status.HTTP_200_OK)
