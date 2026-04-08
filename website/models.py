from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="The Garden of Children")
    tagline = models.CharField(max_length=300, default="Nurturing growth, one child at a time")
    ages_served = models.CharField(max_length=100, default="30 months to kindergarten")
    about_text = models.TextField(blank=True)
    philosophy_text = models.TextField(blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100, default="Vancouver, BC")
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    hours_weekday = models.CharField(max_length=100, default="7:00 AM – 6:00 PM")
    hours_weekend = models.CharField(max_length=100, blank=True)
    google_maps_embed_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HeroSlide(models.Model):
    image = models.ImageField(upload_to="hero/")
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=200, default="Daycare photo")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.caption or f"Slide {self.pk}"


class Program(models.Model):
    title = models.CharField(max_length=200)
    age_range = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="content/", blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class ScheduleItem(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()
    activity = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.time_start:%H:%M} - {self.activity}"


class StaffMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to="staff/", blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ("indoor", "Indoor Activities"),
        ("outdoor", "Outdoor Play"),
        ("events", "Events & Celebrations"),
        ("meals", "Meals & Snacks"),
        ("art", "Arts & Crafts"),
    ]

    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=200, default="Gallery photo")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="indoor")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.caption or f"Photo {self.pk}"


class Testimonial(models.Model):
    parent_name = models.CharField(max_length=200)
    child_age_at_time = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.parent_name


class FeeItem(models.Model):
    PERIOD_CHOICES = [
        ("monthly", "Per Month"),
        ("daily", "Per Day"),
        ("weekly", "Per Week"),
    ]

    title = models.CharField(max_length=200)
    age_group = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default="monthly")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} - ${self.amount}/{self.get_period_display()}"


class Inquiry(models.Model):
    parent_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    child_name = models.CharField(max_length=200, blank=True)
    child_age = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"Inquiry from {self.parent_name} ({self.submitted_at:%Y-%m-%d})"


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
