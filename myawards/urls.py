from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^profile/edit$',views.update_profile,name='edit'),
    url('profile/', views.profile, name='profile'),
    url(r'^new$', views.post, name='post'),
    url(r'^project/(?P<project_id>[0-9])$',views.project,name='project'),
    url(r'^search/', views.search,name='search'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'api/projects/id/(?P<pk>[0-9]+)/$', views.ProjectDescription.as_view()),
    url(r'api/profiles/id/(?P<pk>[0-9]+)/$', views.ProfileDescription.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)