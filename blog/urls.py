from django.urls import path
from blog import views

urlpatterns = [
    path("", views.get_index, name="index-page"),
    path("about/", views.get_about, name="about-view"),
    path("contacts/", views.get_contacts, name="contacts-view"),
    path("post/<int:pk>", views.get_post, name="post-detail"),
    path("delete/", views.get_delete_post, name="delete-view"),
    path("update/", views.get_update_post, name="update-view"),

    
]
