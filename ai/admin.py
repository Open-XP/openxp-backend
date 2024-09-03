from django.contrib import admin
from .models import ChatMessage, ChatSession, Subject, Topic    

admin.site.register(ChatSession)
admin.site.register(ChatMessage)
admin.site.register(Subject)
admin.site.register(Topic)
