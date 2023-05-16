from django.urls import path
from. import views

urlpatterns = [
    # Contact Path
    path('', views.contact, name="contact"),
]
