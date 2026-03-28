from django.contrib import admin
from .models import UserSubmission

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('phone', 'pin', 'created_at')
    search_fields = ('phone',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)