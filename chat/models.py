from django.db import models

from account.models import User


class Message(models.Model):
    body = models.TextField()
    sent_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return f'{self.sent_by}'


class Room(models.Model):
    WAITING = 'waiting'
    ACTIVE = 'active'
    CLOSED = 'closed'

    CHOICES_STATUS = (
        (WAITING, 'Waiting'),
        (ACTIVE, 'Active'),
        (CLOSED, 'Closed'),
    )

    uuid = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    agent = models.ForeignKey(User, related_name='rooms', blank=True, null=True, on_delete=models.SET_NULL)
    messages = models.ManyToManyField(Message, blank=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=WAITING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    
# class MsgRoom(models.Model):
#     room_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class MsgChat(models.Model):
    READ = 'read'
    UNREAD_CLIENT = 'unread_client'
    UNREAD_ADMIN = 'unread_admin'

    READ_RECEIPTS = (
        (READ, 'Read'),
        (UNREAD_CLIENT, 'Unread_client'),
        (UNREAD_ADMIN, 'Unread_admin'),
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    sender = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=READ_RECEIPTS, default=UNREAD_CLIENT)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{str(self.client)} - {self.sender}"