from rest_framework.routers import DefaultRouter

app_name = 'api_urls'
router = DefaultRouter()

# router.register(r'announcement', AnnouncementViewSet, basename='announcement')
# router.register()

urlpatterns = [

]

urlpatterns += router.urls
