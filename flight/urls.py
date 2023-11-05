from rest_framework import routers

from flight.views import (
    AirplaneTypeViewSet,
    AirplaneViewSet,
    CrewViewSet,
    FlightViewSet,
)


app_name = "flight"


router = routers.DefaultRouter()
router.register("airplanetype", AirplaneTypeViewSet)
router.register("airplane", AirplaneViewSet)
router.register("crew", CrewViewSet)
router.register("flight", FlightViewSet)


urlpatterns = router.urls
