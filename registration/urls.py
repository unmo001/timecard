from django.urls import path

from registration import views

app_name = 'registration'

urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Login.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup")
]
