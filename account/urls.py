from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import LoginForm

from .views import (
    CustomAuthToken, UserListView, UserDetailView, UserDetailView2, 
    ChangePasswordView, LogoutView, SignupView,
    DepositView, WithdrawView, TransferView 
)

app_name = 'account'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html', form_class=LoginForm), name='login'),

    path('api/registration/', SignupView.as_view()),
    path('api/login/', CustomAuthToken.as_view(), name ='auth-token'),
    path('api/userlist/', UserListView.as_view()),
    path('api/user-detail/', UserDetailView.as_view()),
    path('api/user-detail/<pk>/', UserDetailView2.as_view()),
    path('api/change-password/', ChangePasswordView.as_view()),
    path('api/auth/logout', LogoutView.as_view()),

    path('api/deposit/', DepositView.as_view(), name='deposit'),
    path('api/withdraw/', WithdrawView.as_view(), name='withdraw'),
    path('api/transfer/', TransferView.as_view(), name='transfer'),

]
