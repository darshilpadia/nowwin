from rest_framework import routers
from .views import Kiosk#,ModelAPIView

router = routers.DefaultRouter()
router.register(r'Kiosk', Kiosk)
# router.register(r'Model', ModelAPIView)

urlpatterns = []
urlpatterns += router.urls
