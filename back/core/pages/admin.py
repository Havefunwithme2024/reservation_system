from django.contrib import admin
from .models import ContactUs, Reservation

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk']
    list_per_page = 6
    search_fields = ['name']
    ordering = ['pk']



@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'full_name', 'time', 'date', 'has_comment']
    list_display_links = ['pk', 'full_name']
    list_per_page = 6
    ordering = ['pk']
    search_fields = ['full_name']
    list_filter = ['date', 'create_datetime']

    @admin.action(description='Has comment')
    def has_comment(self, obj):
        if len(obj.comments) != 0:
            return '✔️'
        else:
            return '❌'





