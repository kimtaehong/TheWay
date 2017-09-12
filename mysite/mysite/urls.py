from django.conf.urls import url, include
from django.conf.urls.static import static, serve
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('twpoint.urls', namespace="twpoint")),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),

] + static(settings.MEDIA_URL, document_url=settings.MEDIA_ROOT)
