from django.contrib import admin
from .models import Competition, Competitor, Regulatory
from import_export.admin import ImportExportModelAdmin
from .resources import CompetitorResource


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'reg_name', 'image', 'allowed', 'reported', 'status')
    list_per_page = 10
    list_filter = ['status']


class CompetitorAdmin(ImportExportModelAdmin):
    list_display = ('firstname', 'lastname', 'club', 'comp_name',)
    list_per_page = 10
    list_filter = ['comp_name']
    person_resource = CompetitorResource()
    dataset = person_resource.export()
    dataset.csv



class RegulatoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'published_date')
    list_per_page = 10
    list_filter = ['published_date']


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Regulatory, RegulatoryAdmin)

# Register your models here.
