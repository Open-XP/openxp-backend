from django.contrib import admin
from .models import ChatMessage, ChatSession, Subject, Topic, TestInstance    

admin.site.register(ChatSession)
admin.site.register(ChatMessage)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(TestInstance)

