from django.urls import path
from basic_app import views



#TEMPLATE TAGGING
app_name='basic_app'

urlpatterns=[
    path('relative_url_templates/',views.relative_url_templates,name='relative'),
    path('other/',views.other,name='other'),
]