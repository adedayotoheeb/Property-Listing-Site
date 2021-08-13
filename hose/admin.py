from django.contrib import admin
from .models import *

# Register your models here.


class AgentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'agent_name', 'email', 'agent_phone')


admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(UserProfile)
admin.site.register(Agents, AgentsAdmin)
admin.site.register(Service)
