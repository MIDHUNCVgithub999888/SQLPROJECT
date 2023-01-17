
from django.urls import path
from. import views
app_name = 'Newapp'

urlpatterns=[

    path('', views.Register, name='Register'),
    path('Delete/<int:id>/',views.Delete,name="Delete"),
    path('Profile/<int:id>/',views.Profile,name="Profile"),
    path('Staff/',views.Staff,name="Staff"),


]