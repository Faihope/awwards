from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
        url('',views.index,name='index'),
        url(r'^registeruser/',views.registeruser,name='registeruser'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)