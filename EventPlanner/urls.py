from django.contrib import admin
from django.urls import include, path
from EventPlanner import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('eventpost/<slug:slug>', views.eventpost, name='eventpost')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)