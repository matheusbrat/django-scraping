from scrapingapp.models  import Outlet, Writer, Article
from rest_framework import viewsets
from scraprest.serializers.serializers import OutletSerializer, WriterSerializer, ArticleSerializer

class OutletViewSet(viewsets.ModelViewSet):
	queryset = Outlet.objects.all()
	serializer_class = OutletSerializer

class WriterViewSet(viewsets.ModelViewSet):
	queryset = Writer.objects.all()
	serializer_class = WriterSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
