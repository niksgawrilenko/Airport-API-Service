from rest_framework import routers

from airport.views import AirportViewSet, RouteViewSet


app_name = "route"


router = routers.DefaultRouter()
router.register("airport", AirportViewSet)
router.register("route", RouteViewSet)


urlpatterns = router.urls
