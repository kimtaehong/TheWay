from django.contrib import admin
from .models import WayPoint, Application, BaseStation

# Register your models here.
admin.site.register(Application)
admin.site.register(WayPoint)
admin.site.register(BaseStation)