"""
ESI URLs
URL:
  /esi/app_label/model_name/object_id[/timeout]/template_name
vars:
  app_label = 'news'
  model_name = 'story'
  object_id= 12345
  timeout = 300
  template_name = 'news/story_detail.html'

example URL:
  /esi/news/story/12345/300/news/story_detail.html

"""
from django.conf.urls import url

from esi import views


urlpatterns = [
    # Static urls
    url(r'^(?P<object_id>static)/(?P<timeout>\d+)/(?P<template>[\w\-\/\.]+)/$',
        views.esi, name='esi'),
    # For objects
    url(r'^(?P<app_label>[\w-]+)/(?P<model_name>[\w-]+)/'
        r'(?P<object_id>\d+)/$',
        views.esi,
        name='esi'),
    url(r'^(?P<app_label>[\w-]+)/(?P<model_name>[\w-]+)/'
        r'(?P<object_id>\d+)/(?P<timeout>\d+)/$',
        views.esi,
        name='esi'),
    url(r'^(?P<app_label>[\w-]+)/(?P<model_name>[\w-]+)/'
        r'(?P<object_id>\d+)/(?P<timeout>\d+)/(?P<template>[\w\-\/\.]+)/$',
        views.esi,
        name='esi'),
]
