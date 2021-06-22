from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name="home"),
    path('login', views.login, name="login"),
    path('registrar', views.registro, name="registro"),
    path('tienda', views.tienda, name="tienda"),
    path('registro/', views.registro, name="registro"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)