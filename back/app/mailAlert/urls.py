from rest_framework import routers
from .api import MailAlertViewSet

router = routers.DefaultRouter()

router.register('api/mailAlert', MailAlertViewSet, 'mailAlert')

urlpatterns = router.urls