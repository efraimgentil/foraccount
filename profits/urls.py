

from django.conf.urls import include, url

urlpatterns=[
    url(r'^profits/$' , "profits.views.index" , name="profits"),
    url(r'^profits/search$' , "profits.views.search" , name="search_profits")
]