from django.contrib import admin
from django.urls import path
from mainApp import views

admin.site.site_header = "My Rest API"
admin.site.site_title = "My Resr API"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('api/',views.api)
]
