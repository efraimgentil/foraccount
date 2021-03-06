"""foraccount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

urlpatterns = [
    url(r'^expenses/$', "expenses.views.index" ,  name="expenses" ),
    url(r'^expenses/search$', "expenses.views.search" ,  name="search_expenses" ),
    url(r'^expenses/new/$', "expenses.views.new" ,  name="new_expense" ),
    url(r'^expenses/(?P<id>\d+)/edit/$', "expenses.views.edit" ,  name="edit_expense" ),
    url(r'^expenses/(?P<id>\d+)/delete/$', "expenses.views.delete" ,  name="delete_expense" ),
]
