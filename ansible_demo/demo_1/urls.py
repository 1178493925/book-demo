import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf.urls import patterns, url, include

from rest_framework import routers
from api.api_demo_1 import *
from views import *
from django.core import urlresolvers

router = routers.SimpleRouter()
router.register(r'demo_api', DemoViewSet)

urlpatterns = [
        url(r'', include(router.urls)),
]


urlpatterns += [
        # url(r'^ip_info_main', ip_info_main),
]
