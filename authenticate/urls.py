from django.contrib import admin
from django.urls import path
from authenticate import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('',views.home,name='index'),
   path('login_user/',views.login_user,name='login_user'),
   path('logout_user/',views.logout_user,name='logout_user'),
   path('register_user/',views.register_user,name='register_user'),
]
