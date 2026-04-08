from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    HeroSlide, Program, ScheduleItem, StaffMember,
    GalleryImage, Testimonial, FeeItem, Inquiry, FAQ,
)
from .forms import ContactForm


def home(request):
    return render(request, "home.html", {
        "slides": HeroSlide.objects.filter(is_active=True),
        "featured_testimonials": Testimonial.objects.filter(is_featured=True, is_active=True)[:3],
        "programs": Program.objects.filter(is_active=True)[:4],
    })


def about(request):
    return render(request, "about.html")


def programs(request):
    return render(request, "programs.html", {
        "programs": Program.objects.filter(is_active=True),
    })


def schedule(request):
    return render(request, "schedule.html", {
        "items": ScheduleItem.objects.all(),
    })


def staff(request):
    return render(request, "staff.html", {
        "members": StaffMember.objects.filter(is_active=True),
    })


def gallery(request):
    return render(request, "gallery.html", {
        "images": GalleryImage.objects.filter(is_active=True),
        "categories": GalleryImage.CATEGORY_CHOICES,
    })


def testimonials(request):
    return render(request, "testimonials.html", {
        "testimonials": Testimonial.objects.filter(is_active=True),
    })


def rates(request):
    return render(request, "rates.html", {
        "fees": FeeItem.objects.filter(is_active=True),
    })


def faq(request):
    return render(request, "faq.html", {
        "faqs": FAQ.objects.filter(is_active=True),
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Honeypot check
            if form.cleaned_data.get("website"):
                return redirect("contact_success")

            data = form.cleaned_data
            Inquiry.objects.create(
                parent_name=data["parent_name"],
                email=data["email"],
                phone=data.get("phone", ""),
                child_name=data.get("child_name", ""),
                child_age=data.get("child_age", ""),
                message=data["message"],
            )

            send_mail(
                subject=f"New Inquiry from {data['parent_name']}",
                message=(
                    f"Name: {data['parent_name']}\n"
                    f"Email: {data['email']}\n"
                    f"Phone: {data.get('phone', 'N/A')}\n"
                    f"Child's Name: {data.get('child_name', 'N/A')}\n"
                    f"Child's Age: {data.get('child_age', 'N/A')}\n\n"
                    f"Message:\n{data['message']}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
            return redirect("contact_success")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def contact_success(request):
    return render(request, "contact_success.html")
