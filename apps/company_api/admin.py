from django.contrib import admin
from apps.company_api.models import Company
@admin.register(Company)


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "company_id","name","organisation",
        "type","location","ceo","active","added_date",)
    list_filter = ("organisation", "type", "active", "added_date")
    search_fields = ("name", "ceo", "location")
    ordering = ("-added_date",)
    list_per_page = 20
    readonly_fields = ("added_date",)

    fieldsets = (
        ("Company Information", {
            "fields": ("name", "organisation", "type", "about")
        }),
        ("Additional Details", {
            "fields": ("location", "ceo", "active", "added_date")
        }),
    )
