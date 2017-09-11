from django.conf.urls import url
from .views import get_index, register, profile, logout, login


urlpatterns = [
    url(r'^$', get_index, name='get_index'),
    url(r'^register$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout$', logout, name='logout'),
    url(r'^login$', login, name='login'),
]
