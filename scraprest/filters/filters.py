from scrapingapp.models  import Article
import django_filters

class ArticleFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(name="title", lookup_type='icontains')
	url = django_filters.CharFilter(name="url", lookup_type='icontains')
	image = django_filters.CharFilter(name="image", lookup_type='icontains')
	content = django_filters.CharFilter(name="content", lookup_type='icontains')
	publication_date = django_filters.DateTimeFilter(name="publication_date", lookup_type='gte')

	writers_name = django_filters.CharFilter(name="writers__name", lookup_type='icontains')
	writers_twitter = django_filters.CharFilter(name="writers__twitter", lookup_type='icontains')
	writers_profile = django_filters.CharFilter(name="writers__profile", lookup_type='icontains')
	outlet_name = django_filters.CharFilter(name="outlet__name", lookup_type='icontains')

	class Meta:
		model = Article
		fields = ('title','url','image','content', 'publication_date', 'writers_name','writers_twitter','writers_profile','outlet_name')

