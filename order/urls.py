from rest_framework import routers

from order.views import OrderViewSet


app_name = "order"


router = routers.DefaultRouter()
router.register("order", OrderViewSet)


urlpatterns = router.urls
