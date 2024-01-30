
from django.contrib import admin
from django.urls import path,include
from core.views import frontpage, sobre, promocao

urlpatterns = [
    path('',include('loja.urls')),
    path('',frontpage, name = 'frontpage'),
    path('promocao/',promocao, name = 'promocao'),
    path('sobre/',sobre, name = 'sobre'),
    path('admin/', admin.site.urls),
]
