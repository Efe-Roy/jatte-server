# Generated by Django 4.2.1 on 2024-04-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_msgchat_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgchat',
            name='status',
            field=models.CharField(choices=[('read', 'Read'), ('unread_client', 'Unread_client'), ('unread_admin', 'Unread_admin')], default='unread_client', max_length=20),
        ),
    ]
