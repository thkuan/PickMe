from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import index, draw, history, reset

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^draw/$', draw, name='draw'),
    url(r'^history/$', history, name='history'),
    url(r'^reset/$', reset, name='reset'),
]
