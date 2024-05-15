from django.contrib import admin
from .models import Family, Person, Register


admin.site.register([Family, Person, Register])
