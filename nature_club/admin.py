from django.contrib import admin
from .models import Contact, Gallery, Events, LeaderShip

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Events)
admin.site.register(LeaderShip)
admin.site.register(Contact)
