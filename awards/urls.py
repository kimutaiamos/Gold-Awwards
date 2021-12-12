from django.conf.urls import include,url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('registration/',views.registration, name='registration'),   
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('profile/', views.profile, name='profile'),
    url(r'^upload/$',views.new_project,name='add_project'),
    url(r'^project_details/(?P<id>\d+)', views.project_details, name='projectdetails'),
    url(r'^review/(?P<project_id>\d+)', views.review_project, name='review'),
    url(r'^searched/', views.search_projects, name='search'),
    url('api/profilelist',views.ProfileList.as_view(),name='profileEndpoint'),
    url('api/projectslist',views.ProjectList.as_view(),name='projectsEndpoint')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)