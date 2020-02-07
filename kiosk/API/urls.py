from rest_framework import routers
from .views import Kiosk

router = routers.DefaultRouter()
router.register(r'Kiosk', Kiosk)

urlpatterns = []
urlpatterns += router.urls
