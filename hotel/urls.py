"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from Restrarent import views as vi2
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_admin/',views.main_admin,name='main_admin'),
#rooms
    path('room_mgmt/',views.room_mgmt,name='room_mgmt'),
    path('add_room/',views.add_room,name='add_room'),
    path('view_room',views.view_room,name='view_room'),
    path('update_room/<int:id>',views.update_room,name="update_room"),
    path('delete_room/<int:id>',views.delete_room,name='delete_room'),


#staffs
    path('staff_mgmt/',views.staff_mgmt,name='staff_mgmt'),
    path('add_staff/',views.add_staff,name='add_staff'),
    path('view_staff',views.view_staff,name='view_staff'),
    path('update_staff/<int:id>',views.update_staff,name="update_staff"),
    path('del_staff/<int:id>',views.delete_staff,name='delete_staff'),


#restrarent

    path('rest_mgmt/',views.rest_mgmt,name='rest_mgmt'),
    path('add_rest/',views.add_rest,name='add_rest'),
    path('view_rest',views.view_rest,name='view_rest'),
    path('update_rest/<int:id>',views.update_rest,name="update_rest"),
    path('delete_rest/<int:id>',views.delete_rest,name='delete_rest'),

#users

    path('user_mgmt/',views.user_mgmt,name='user_mgmt'),
    path('add_user',views.add_user,name='add_user'),
    path('view_user',views.view_user,name='view_user'),
    path('update_user/<int:id>',views.update_user,name="update_user"),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),





#RESTRARENT
    path('restrarent_reg',vi2.restrarent_reg,name='restrarent_reg'),



]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)