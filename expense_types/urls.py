from django.conf.urls import url



urlpatterns=[
    url(r'^expense_types/$' , "expense_types.views.index"   , name='expense_types'),
    url(r'^expense_types/form/$' , "expense_types.views.form" , name="new_expense_type"),
    url(r'^expense_types/(?P<id>\d+)/form/' , "expense_types.views.edit" , name="edit_expense_type"),
    url(r'^expense_types/(?P<id>\d+)/delete/' , "expense_types.views.delete" , name="delete_expense_type"),
]