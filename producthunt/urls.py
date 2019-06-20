from django.contrib import admin
from django.urls import path, include
import products.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
