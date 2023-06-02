from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index, name="request" ),
    path( 'selenium/', views.selenium, name="selenium" ),
    path( 'about/', views.about, name="about" )
]