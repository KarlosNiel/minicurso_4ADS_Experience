from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'streamings', StreamingViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls