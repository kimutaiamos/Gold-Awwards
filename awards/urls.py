from django.conf.urls import include,url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('registration/',views.registration, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
]