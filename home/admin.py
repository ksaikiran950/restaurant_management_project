from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
        list_display = ('id', 'comment', 'created_at')
            list_filter = ('created_at',)