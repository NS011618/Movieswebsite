from django.contrib import admin
from mvapp.models import mshow
# Register your models here.
class mvAdmin(admin.ModelAdmin):
    list_display=['Moviename','Heroname','Heroiename','Director','Releasedate','rating','mimage']
admin.site.register(mshow,mvAdmin)