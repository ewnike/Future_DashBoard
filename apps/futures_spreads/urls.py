from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^spreads$', views.spreads, name="spreads"),
    url(r'^add_future$', views.add_future, name='add_future'),
    url(r'^add_symbols$', views.add_symbols, name = 'add_symbols'),
    # url(r'displayfuture/(?P<future_id>\d+)$', views.displayfuture, name = 'displayfuture'),
    url(r'^create_spread$', views.create_spread, name = 'create_spread'),
    url(r'^assign/(?P<back_id>\d+)/to/(?P<front_id>\d+)$', views.assign_future, name = 'assign'),
    url(r'^remove/(?P<back_id>\d+)/to/(?P<front_id>\d+)$', views.remove_future, name = 'remove'),
    url(r'^update_future/(?P<future_id>\d+)$', views.update_future, name = 'update_future'),
    url(r'^make_spreads/(?P<future_id>\d+)$', views.make_spreads, name = 'make_spreads')
]
