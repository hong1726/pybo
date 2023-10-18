from django.contrib import admin
from .models import Question


class QuetionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuetionAdmin)

# Register your models here.
