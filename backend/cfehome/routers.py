from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet

# print('router.urls')
router = DefaultRouter()
# print(router.urls)
router.register('product', ProductViewSet, basename='products')
print(router.urls)
urlpatterns = router.urls
