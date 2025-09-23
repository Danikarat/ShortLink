from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home, name='shorten_url'),
    path('<str:shortcode>/', views.redirect_url, name='redirect_url'),
]