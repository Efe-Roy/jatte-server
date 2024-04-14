from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('', include('chat.urls')),
    path('', include('account.urls')),
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
]
