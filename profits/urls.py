

from django.conf.urls import include, url

urlpatterns=[
    url(r'^profits/$' , "profits.views.index" , name="profits"),
    url(r'^profits/search$' , "profits.views.search" , name="search_profits"),
    url(r'^profits/new/$' , "profits.views.new" , name="new_profit"),
    url(r'^profits/(?P<id>\d+)/edit/$' , 'profits.views.edit' , name='edit_profit'),
    url(r'^profits/(?P<id>\d+)/delete/$', 'profits.views.delete' , name="delete_profit"),
]
