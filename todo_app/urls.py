from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from todo_list import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.todo, name='todo'),
    url(r'^add/$', views.add, name='add'),
    path('delete/<int:id>/',views.delete,name = 'delete'),
]
