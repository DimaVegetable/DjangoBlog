from django.urls import path
from django.contrib import admin
from article import views
from django.conf.urls import include, url


urlpatterns = [
    path('', views.articles),
    url('admin/', admin.site.urls),
    url(r'^articles/get/(?P<article_id>\d+)', views.article, name='articles')
]