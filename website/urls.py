from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("programs/", views.programs, name="programs"),
    path("schedule/", views.schedule, name="schedule"),
    path("staff/", views.staff, name="staff"),
    path("gallery/", views.gallery, name="gallery"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("rates/", views.rates, name="rates"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),
]
