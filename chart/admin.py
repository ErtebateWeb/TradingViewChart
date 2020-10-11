from django.contrib import admin
from .models import Event
# Register your models here.

class EventsMode(admin.ModelAdmin):
    list_display = ['id','name','text','date','timestamp']
    # search_fields=['SymbolTitle',
    # 'CreatedDate',
    # 'updatedDate',
    # 'Publisher',
    # ]
    # list_filter = ['CreatedDate']

admin.site.register(Event,EventsMode)