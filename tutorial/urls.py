from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

router = routers.DefaultRouter() #massive, complicated - which routes
router.register(r'users', views.UserViewSet) #which view to use
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), #enables full authentication
    url(r'^', include('snippets.urls')),
    url('^schema/$', schema_view),
]