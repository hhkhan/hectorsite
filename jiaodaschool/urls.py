from django.conf.urls import url
from . import views


app_name = 'jiaodaschool'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^exam/$', views.ExmIndexView.as_view(), name='exm_index'),
    url(r'^exam/detail/(?P<exm_id>[0-9]+)/$', views.exm_detail, name='exm_detail'),
    url(r'^students/$', views.index, name='index')
]