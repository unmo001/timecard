from django.urls import path

from post import views

app_name = 'post'

urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('front/',views.FrontView.as_view(),name="front"),
    # path('front/<int:pk>',views.UserDetailView.as_view(),name="user_detail")
]
