from django.urls import path
from .views import Login, SignUpView

urlpatterns = [
    path('login/', Login.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
