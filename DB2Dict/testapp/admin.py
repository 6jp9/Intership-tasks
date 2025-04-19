from django.contrib import admin
from testapp.models import Test

# Register your models here.
class TestAdmin(admin.ModelAdmin):
    list_display = ['id','name','address']
admin.site.register(Test,TestAdmin)
