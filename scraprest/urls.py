from rest_framework import routers
from scraprest.views.views import ArticleViewSet, OutletViewSet, WriterViewSet

router = routers.DefaultRouter()
router.register(r'articles_test', ArticleViewSet)
router.register(r'outlets', OutletViewSet)
router.register(r'writers', WriterViewSet)