from rest_framework import serializers
from .models import MsgChat

class MsgChatSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = MsgChat
        fields = ['id', 'client', 'sender', 'message', 'created_at']

    # def get_room(self, obj):
    #     return UserSerializer(obj.room).data
    