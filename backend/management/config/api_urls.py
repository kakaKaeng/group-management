from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from management.apps.customers.views import CustomerViewSet
from management.apps.profiles.views import ProfileViewSet

app_name = 'api_urls'
router = DefaultRouter()

router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
