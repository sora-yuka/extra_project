from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView, TokenRefreshView    
)
from account.views import RegisterAPIView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="obtain_pair_view"),
    path("refresg/", TokenRefreshView.as_view(), name="refresh_view"),
    path("register/", RegisterAPIView.as_view(), name="register")
]
