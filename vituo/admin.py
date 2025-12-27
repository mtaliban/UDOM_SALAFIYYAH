from django.contrib import admin
from vituo.models import College, Muswallah, ExternalIslamicFacility

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_salafi', 'created_at']
    search_fields = ['name']
    list_filter = ['is_salafi', 'created_at']

@admin.register(Muswallah)
class MuswallahAdmin(admin.ModelAdmin):
    list_display = ['name', 'college', 'is_salafi', 'created_at']
    search_fields = ['name']
    list_filter = ['college', 'is_salafi', 'created_at']

@admin.register(ExternalIslamicFacility)
class ExternalIslamicFacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'college', 'created_at']
    search_fields = ['name', 'location']
    list_filter = ['college', 'created_at']
# Register your models here.
