from django.urls import path
from blog import views

urlpatterns = [ 
    path("hello/", views.get_index, name = "index-page"),
    path("contacts/", views.get_contacts, name="contacts-view"),
    path("about/", views.get_about, name ="about-view"),
]