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
        filename = f"{uuid.uuid4()}.wav"
        tts.to_wav_in_chunks(text, chunk_size=100, path=f"{settings.MEDIA_ROOT}audio/{filename}")
        # get audio from the path

        audio_path = "http://3.145.65.58:8000"
        audio_url = f"{audio_path}{settings.MEDIA_URL}audio/{filename}"

        if not audio_url:
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"audio": audio_url}, status=status.HTTP_200_OK)
