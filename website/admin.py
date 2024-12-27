from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject','first_name','email','created_date','updated_date']
    list_filter = ('subject',)


admin.site.register(Contact,ContactAdmin)
