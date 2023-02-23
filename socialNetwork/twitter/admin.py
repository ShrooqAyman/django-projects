from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import profile, Tweet

class ProfileInline(admin.StackedInline):
    model = profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]




admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
#admin.site.register(profile, ProfileAdmin)
admin.site.register(Tweet)

