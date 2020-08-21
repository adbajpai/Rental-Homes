from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/',views.register),
    path('login/',views.login),
    path('profile/',views.profile),
    path('search/',views.search),
    path('lastproject/search/',views.search),
    path('lastproject/profile/',views.profile),
    path('rentee/',views.rentee),
    path('renter/',views.renter),
    path('rentersearch/',views.rentersearch),
    path('lastproject/rentersearch/',views.rentersearch),
    path('logout/',views.logout),

]
