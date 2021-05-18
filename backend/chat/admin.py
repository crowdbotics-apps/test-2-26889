from django.contrib import admin
from .models import (
    ForwardedMessage,
    Message,
    ThreadMember,
    MessageAction,
    Thread,
    ThreadAction,
)

admin.site.register(ThreadMember)
admin.site.register(ForwardedMessage)
admin.site.register(Message)
admin.site.register(MessageAction)
admin.site.register(Thread)
admin.site.register(ThreadAction)

# Register your models here.
