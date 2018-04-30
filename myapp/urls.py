from django.conf.urls import url
from myapp import views



urlpatterns = [
    url(r'^$', views.index.as_view(), name = "home"),
    url(r'^source',views.sources.as_view() , name = "sources"),
    url(r'^about',views.about.as_view() , name = "about"),
    url(r'^currency/(?P<currency>[\w\-]+)/$', views.detail, name="detail"),
]