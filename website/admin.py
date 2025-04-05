from django.contrib import admin
# the model that we created
from .models import Record
# Register your models here.
# register and they will appear in the admin page after login
admin.site.register(Record)