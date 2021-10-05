from django.contrib import admin

from Web_App.views import eventform


from .models import *

# Register your models here.
admin.site.register(Product),
admin.site.register(Organizer),
admin.site.register(Storef),
admin.site.register(Eventform),


