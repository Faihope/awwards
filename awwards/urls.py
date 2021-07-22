
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
        path('',views.index,name = 'index'),
        path('register/', views.registeruser, name="register"),
	path('login/', views.loginpage, name="login"), 
        path('logoutuser/',views.logoutuser,name='logoutuser'),
        path('create/profile/',views.create_profile, name='e create_profile'),
        path('profiles/',views.profile, name='profile'),
        path('new/project/',views.new_project, name='new_project'),








]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
