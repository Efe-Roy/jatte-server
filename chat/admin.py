from django.contrib import admin

from .models import Room, Message, MsgChat


admin.site.register(Room)
admin.site.register(Message)

# class MsgRoomAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'room_user',
#     ]
#     list_filter = ['id']
#     search_fields = ['room_user']

# admin.site.register(MsgRoom, MsgRoomAdmin)

admin.site.register(MsgChat)