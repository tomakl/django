from django.contrib import admin
from django.db.models import Max

from .models import Competition, Competitor, Regulatory
from import_export.admin import ImportExportModelAdmin
from django.utils import timezone


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'reg_name', 'image', 'allowed', 'reported', 'status')
    list_per_page = 10
    list_filter = ['status']




class CompetitorAdmin(ImportExportModelAdmin):
    list_display = ('start_number','firstname', 'lastname','club', 'comp_name', 'gender', 'age', 'payment', 'payment_date',)
    list_per_page = 10
    list_filter = ['comp_name', 'gender']
    list_display_links = ['firstname','lastname']
    actions = ['change_payment','change_payment_down']
    def change_payment(self, request, queryset):
        queryset.update(payment='1')
    change_payment.short_description = "Płatność OK"

    def change_payment_down(self, request, queryset):
        queryset.update(payment='0')
    change_payment_down.short_description = "Wycofaj płatność"


class RegulatoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'published_date')
    list_per_page = 10
    list_filter = ['published_date']




admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Regulatory, RegulatoryAdmin)

# Register your models here.
