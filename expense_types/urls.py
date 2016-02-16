from django.conf.urls import url



urlpatterns=[
    url(r'^expense_types/$' , "expense_types.views.index"   , name='expense_types'),
    url(r'^expense_types/search$' , "expense_types.views.search"   , name='search_expense_types'),
    url(r'^expense_types/new/$' , "expense_types.views.form" , name="new_expense_type"),
    url(r'^expense_types/(?P<id>\d+)/edit/$' , "expense_types.views.edit" , name="edit_expense_type"),
    url(r'^expense_types/(?P<id>\d+)/delete/$' , "expense_types.views.delete" , name="delete_expense_type"),
    url(r'^expense_types/(?P<id>\d+)/subtypes/$' , "expense_types.views.subtypes" , name="subtypes_expense_type"),
]