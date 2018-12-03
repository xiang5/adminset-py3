from django.contrib import admin
from django.urls import include, path
from adminset.views import index
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('navi/', include('navi.urls')),
    path('cmdb/', include('cmdb.urls')),

]
