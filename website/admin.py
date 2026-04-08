from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, HeroSlide, Program, ScheduleItem,
    StaffMember, GalleryImage, Testimonial, FeeItem, Inquiry, FAQ,
)

admin.site.site_header = "The Garden of Children — Admin"
admin.site.site_title = "Garden of Children"
admin.site.index_title = "Manage Your Website"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("General", {"fields": ("site_name", "tagline", "ages_served")}),
        ("About Page Content", {"fields": ("about_text", "philosophy_text")}),
        ("Contact Information", {"fields": ("address", "city", "phone", "email")}),
        ("Hours", {"fields": ("hours_weekday", "hours_weekend")}),
        ("Links", {"fields": ("google_maps_embed_url", "facebook_url", "instagram_url")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "caption", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("caption",)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;" />', obj.image.url)
        return "—"
    thumbnail.short_description = "Preview"


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "age_range", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ("activity", "time_start", "time_end", "order")
    list_editable = ("order",)


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "name", "role", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("name",)

    def thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height:50px;border-radius:50%%;" />', obj.photo.url)
        return "—"
    thumbnail.short_description = "Photo"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "caption", "category", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("category",)
    list_display_links = ("caption",)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;" />', obj.image.url)
        return "—"
    thumbnail.short_description = "Preview"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("parent_name", "short_quote", "is_featured", "is_active")
    list_editable = ("is_featured", "is_active")
    list_filter = ("is_featured", "is_active")

    def short_quote(self, obj):
        return obj.quote[:80] + "..." if len(obj.quote) > 80 else obj.quote
    short_quote.short_description = "Quote"


@admin.register(FeeItem)
class FeeItemAdmin(admin.ModelAdmin):
    list_display = ("title", "age_group", "amount", "period", "order", "is_active")
    list_editable = ("order", "is_active", "amount")


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("parent_name", "email", "child_name", "submitted_at", "is_read")
    list_filter = ("is_read", "submitted_at")
    list_editable = ("is_read",)
    readonly_fields = ("parent_name", "email", "phone", "child_name", "child_age", "message", "submitted_at")

    def has_add_permission(self, request):
        return False


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "is_active")
    list_editable = ("order", "is_active")
