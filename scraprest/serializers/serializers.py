from scrapingapp.models  import Outlet, Writer, Article
from rest_framework import serializers, viewsets

class OutletSerializer(serializers.ModelSerializer):
	class Meta:
		model = Outlet
		fields = ('name', 'url', 'description')

class WriterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Writer
		fields = ('name', 'twitter', 'profile')

class ArticleSerializer(serializers.ModelSerializer):
	writers = WriterSerializer(many=True, read_only=True)
	outlet = OutletSerializer()
	class Meta:
		model = Article

		fields = ('writers', 'outlet', 'publication_date', 'content')