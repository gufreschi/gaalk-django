from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

#Unregister Groups and Initial User
admin.site.unregister(Group)
admin.site.unregister(User)

#Blend Profile into User
class ProfileInline(admin.StackedInline):
    model = Profile

#Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

#Re-register User
admin.site.register(User, UserAdmin)