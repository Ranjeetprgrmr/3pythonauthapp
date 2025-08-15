

from django.conf import settings
from django.conf.urls.static import static  #
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('Core.urls')),
    path('accounts/', include('allauth.urls')),
]
# ======= ADD THIS BLOCK ======= #
# Serve static files even in DEBUG=False mode (local testing only)
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


