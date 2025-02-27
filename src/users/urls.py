from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView, TokenVerifyView

from users.views import UserRegistrationView



urlpatterns = [
    path("auth/sign-up/", UserRegistrationView.as_view(), name="signup"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("auth/token/verify/", TokenVerifyView.as_view(), name='token_verify')
]
