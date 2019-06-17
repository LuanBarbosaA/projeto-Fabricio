from django.contrib import admin
from .models import Booking, BookTime, Place, Building

# Register your models here.
admin.site.register(Booking)
admin.site.register(BookTime)
admin.site.register(Place)
admin.site.register(Building)
