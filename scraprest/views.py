from django.shortcuts import render

# Create your views here.
class OutletViewSet(viewsets.ModelViewSet):
	queryset = Outlet.objects.all()
	serializer_class = OutletSerializer

class WriterView(viewsets.ModelViewSet):
	queryset = Writer.objects.all()
	serializer_class = WriterSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer