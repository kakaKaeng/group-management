from rest_framework.routers import DefaultRouter

from management.apps.profiles.views import ProfileViewSet

app_name = 'api_urls'
router = DefaultRouter()

router.register(r'profiles', ProfileViewSet, basename='profiles')

urlpatterns = [

]

urlpatterns += router.urls
