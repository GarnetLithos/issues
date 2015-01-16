# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from ranklist import views

urlpatterns = patterns('',
    url(r'^test/bullets1', views.bullets1, name='bullets1'),
    url(r'^test/bullets2', views.bullets2, name='bullets2'),
    url(r'^test/sortBarChart', views.sort_bar_chart, name='sort_bar_chart'),
    url(r'^base$', views.base, name='base'),
    url(r'^hours$', views.hours, name='hours'),
    url(r'^days$', views.days, name='days'),
    url(r'^months$', views.months, name='months'),
    url(r'^years$', views.years, name='years'),
    url(r'^(?P<site>\w+)/year/(?P<year>\d+)$', views.year_data, name='year_data'),
    url(r'^(?P<site>\w+)/month/(?P<year>\d+)/(?P<month>\d+)$', views.month_data, name='month_data'),
    url(r'^(?P<site>\w+)/day/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)$', views.day_data, name='day_data'),
    url(r'^(?P<site>\w+)/hour/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)$', views.hour_data, name='hour_data'),

    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)