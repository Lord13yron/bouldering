from django.contrib import admin

from .models import Zone, Area, Problem, Profile, Rating, Comment

class AreaAdmin(admin.ModelAdmin):
    filter_horizontal =("zone",)

class ProblemAdmin(admin.ModelAdmin):
    filter_horizontal =("area",)

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal =("favorites", "sends")

# Register your models here.
admin.site.register(Zone)
admin.site.register(Area)
admin.site.register(Problem)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Rating)
admin.site.register(Comment)