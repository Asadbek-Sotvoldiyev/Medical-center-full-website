from django.contrib import admin
from .models import Family, Person, Register


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profession', 'phone_number', 'gender')


admin.site.register(Family, FamilyAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Register)
