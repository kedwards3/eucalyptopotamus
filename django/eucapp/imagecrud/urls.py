from django.conf.urls import patterns, url

from imagecrud import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /create/myimage
    url(r'^(?P<image_name>\w+)/create($|/)$', views.create, name='create'),
    # ex: /update/myimage
    url(r'^(?P<image_name>\w+)/update($|/)$', views.update, name='update'),
    # ex: /delete/myimage
    url(r'^(?P<image_name>\w+)/delete($|/)$', views.delete, name='delete'),
    # ex: /read/myimage
    url(r'^(?P<image_name>\w+)($|/)', views.read, name='read'),
)
