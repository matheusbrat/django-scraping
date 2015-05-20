from scrapingapp.models  import Outlet, Writer, Article
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from scraprest.filters.filters import ArticleFilter
from scraprest.serializers.serializers import OutletSerializer, WriterSerializer, ArticleSerializer

class OutletViewSet(viewsets.ModelViewSet):
	filter_backends = (filters.DjangoFilterBackend,)
	queryset = Outlet.objects.all()
	serializer_class = OutletSerializer
	filter_fields = ('name', 'url', 'description')

class WriterViewSet(viewsets.ModelViewSet):
	filter_backends = (filters.DjangoFilterBackend,)
	queryset = Writer.objects.all()
	serializer_class = WriterSerializer
	filter_fields = ('name', 'twitter', 'profile')

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
	filter_backends = (filters.DjangoFilterBackend,)
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filter_class = ArticleFilter