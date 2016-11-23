from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),      # index page url
    url(r'^result/(?P<application_id>[0-9]+)/$', views.detail, name="detail"), # detail page url
    url(r'^result$',views.result, name="result"),
    url(r'^result/gallery$',views.gallery, name="gallery"),
    url(r'^parsing$',views.parsing,name="parsing"),
]