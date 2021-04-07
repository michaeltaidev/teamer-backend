from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from teammates import views

urlpatterns = [
    url(r'^departments/$', views.departmentApi),
    url(r'^departments/([0-9]+)$', views.departmentApi),
    url(r'^teammates/$', views.teammateApi),
    url(r'^teammates/([0-9]+)$', views.teammateApi),
    url(r'^saveFile$', views.saveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)