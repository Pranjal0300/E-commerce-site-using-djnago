from django.urls import path
from authcart import views


urlpatterns =[
    path('signup/',views.signup,name='Signup'),
    path('logout/',views.handlelogout,name='Logout'),
    path('login/',views.handlelogin,name='Login'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]