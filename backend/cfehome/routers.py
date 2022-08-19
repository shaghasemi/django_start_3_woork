from rest_framework.routers import DefaultRouter
from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
# print(router.urls)
# router.register('product', ProductViewSet, basename='products')
router.register('product', ProductGenericViewSet, basename='products')
print(router.urls)
urlpatterns = router.urls
