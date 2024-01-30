from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from core.views import frontpage, sobre, promocao
from userprofile.views import vendor_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promocao/',promocao, name = 'promocao'),
    path('sobre/',sobre, name = 'sobre'),
    path('vendors/',vendor_details, name = 'vendors'),
    path('',include('userprofile.urls')),
    path('',include('loja.urls')),
    path('',frontpage, name = 'frontpage'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
