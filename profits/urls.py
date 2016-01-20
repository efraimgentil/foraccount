from django.conf.urls import include, url

urlpatterns=[
    url(r'profits/$' , "profits.views.index" , name="profits"),
    url(r'profits/search$' , "profits.views.search" , name="search_profits"),
    url(r'profits/new/$' , "profits.views.new" , name="new_profit"),
    url(r'profits/(?P<id>\d+)/edit/$' , 'profits.views.edit' , name='edit_profit'),
    url(r'profits/(?P<id>\d+)/delete/$', 'profits.views.delete' , name="delete_profit"),
    url(r'profit_types/$' , "profits.views.types_index" , name='profit_types'),
    url(r'profit_types/new/$' , "profits.views.types_new" , name='new_profit_type'),
    url(r'profit_types/(?P<id>\d+)/edit/$' , "profits.views.types_edit" , name="edit_profit_type"),
    url(r'profit_types/(?P<id>\d+)/delete/$' , "profits.views.types_delete" , name="delete_profit_type"),
]
