from django.contrib import admin
from .models import PostCard, Location, Photo
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
# Register your models here.

admin.site.register(PostCard)
admin.site.register(Location)
admin.site.register(Photo)


class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
