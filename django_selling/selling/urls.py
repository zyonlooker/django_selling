from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base, name = 'index'),
    path('free/', views.free, name = 'free'),
    path('half/', views.half, name = 'half')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
