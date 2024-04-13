import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MsgChatSerializer

from account.forms import AddUserForm, EditUserForm
from account.models import User

from .models import Room, MsgChat

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'PageSize'

class MessageListView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = MsgChatSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = MsgChat.objects.all()

        # Filter based on request parameters
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            queryset = queryset.filter(client=user_id)
   
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        unread_msg_client = queryset.filter(status="unread_client").count()
        unread_msg_admin = queryset.filter(status="unread_admin").count()

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response_data = {
                'results': serializer.data,
                'unread_msg_client': unread_msg_client,
                'unread_msg_admin': unread_msg_admin,
            }
            return self.get_paginated_response(response_data)

        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'results': serializer.data,
            'unread_msg_client': unread_msg_client,
            'unread_msg_admin': unread_msg_admin,
        }

        return Response(response_data)
    
class UpdateMsgStatusAPIView(APIView):
    def get(self, request, pk, role, format=None):
        user = User.objects.get(id=pk)

        # print("role", role)
        if role == "client":
            instances_msg = MsgChat.objects.filter(client=user, status="unread_client")
            # print("Client")
            for instance in instances_msg:
                instance.status = "read"
                instance.save()
        else:
            instances_msg = MsgChat.objects.filter(client=user, status="unread_admin")
            # print("Admin")
            for instance in instances_msg:
                instance.status = "read"
                instance.save()

        return Response("Successfully updated for instances", status=status.HTTP_200_OK)
    
@require_POST
def create_room(request, uuid):
    name = request.POST.get('name', '')
    url = request.POST.get('url', '')

    Room.objects.create(uuid=uuid, client=name, url=url)

    return JsonResponse({'message': 'room created'})


@login_required
def admin(request):
    rooms = Room.objects.all()
    users = User.objects.filter(is_staff=True)

    return render(request, 'chat/admin.html', {
        'rooms': rooms,
        'users': users
    })


@login_required
def room(request, uuid):
    room = Room.objects.get(uuid=uuid)

    if room.status == Room.WAITING:
        room.status = Room.ACTIVE
        room.agent = request.user
        room.save()

    return render(request, 'chat/room.html', {
        'room': room
    })


@login_required
def delete_room(request, uuid):
    if request.user.has_perm('room.delete_room'):
        room = Room.objects.get(uuid=uuid)
        room.delete()
                
        messages.success(request, 'The room was deleted!')

        return redirect('/chat-admin/')
    else:
        messages.error(request, 'You don\'t have access to delete rooms!')

        return redirect('/chat-admin/')


@login_required
def user_detail(request, uuid):
    user = User.objects.get(pk=uuid)
    rooms = user.rooms.all()

    return render(request, 'chat/user_detail.html', {
        'user': user,
        'rooms': rooms
    })


@login_required
def edit_user(request, uuid):
    if request.user.has_perm('user.edit_user'):
        user = User.objects.get(pk=uuid)

        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user)

            if form.is_valid():
                form.save()
                
                messages.success(request, 'The changes was saved!')

                return redirect('/chat-admin/')
        else:
            form = EditUserForm(instance=user)

        return render(request, 'chat/edit_user.html', {
            'user': user,
            'form': form
        })
    else:
        messages.error(request, 'You don\'t have access to edit users!')

        return redirect('/chat-admin/')


@login_required
def add_user(request):
    if request.user.has_perm('user.add_user'):
        if request.method == 'POST':
            form = AddUserForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.is_staff = True
                user.set_password(request.POST.get('password'))
                user.save()

                if user.role == User.MANAGER: 
                    group = Group.objects.get(name='Managers')
                    group.user_set.add(user)
                
                messages.success(request, 'The user was added!')

                return redirect('/chat-admin/')
        else:
            form = AddUserForm()

        return render(request, 'chat/add_user.html', {
            'form': form
        })
    else:
        messages.error(request, 'You don\'t have access to add users!')

        return redirect('/chat-admin/')