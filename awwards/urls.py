from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
        url(r'^$',views.index,name = 'index'),
        url(r'registeruser/',views.registeruser,name='registeruser'),
        url(r'^loginpage/',views.loginpage,name='loginpage'),
        url(r'^logout/$',views.logoutuser,name='logoutuser'),
        url(r'^profile/$',views.create_profile, name='create_profile'),
        url(r'^profiles$',views.profile, name='profiles'),
        url(r'^new/project$',views.new_project, name='new_project'),








]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
