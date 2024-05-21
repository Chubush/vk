from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register"),
     
    #Email doğrulama url leri
    path("email-verification/<str:uidb64>/<str:token>/", views.email_verification, name="email-verification"),
    path("email-verification-sent/", views.EmailVerificationSentView.as_view(), name="email-verification-sent"),
    path("email-verification-success/", views.EmailVerificationSuccessView.as_view(), name="email-verification-success"),
    path("email-verification-failed/", views.EmailVerificationFailedView.as_view(), name="email-verification-failed"),
    
    # login/logout url's
    path("my-login/", views.LoginView.as_view(), name="my-login"),
    path("user-logout/", views.UserLogoutView.as_view(), name="user-logout"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    
    # dashboard/profile url's
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("profile-management/", views.ProfileManagementView.as_view(), name="profile-management"),    
    
    # password reset url's
    # 1 ) E-posta formumuzu gönderin
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="account/password/password-reset.html"), name='reset_password'),

    # 2) Parola sıfırlama e-postasının gönderildiğini belirten başarı mesajı
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="account/password/password-reset-sent.html"), name='password_reset_done'),

    # 3) Şifre sıfırlama bağlantısı
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password/password-reset-form.html"), name='password_reset_confirm'),

    # 4) Şifremizin sıfırlandığını belirten başarı mesajı
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="account/password/password-reset-complete.html"), name='password_reset_complete'),
      
]


