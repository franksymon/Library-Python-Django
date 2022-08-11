from rest_framework.routers import DefaultRouter

from .views import BookItemViewSet, BookViewset

router = DefaultRouter()
router.register("catalog", BookViewset)
router.register("book-item", BookItemViewSet)
urlpatterns = router.urls
