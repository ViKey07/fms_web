from datetime import timedelta
from django.utils import timezone
from django.db import models

class User(models.Model):
    class Meta(object):
        db_table = 'user'

    user_name = models.CharField(
        'User Name', blank=False, null=False, max_length=50, db_index=True
    )
    password = models.CharField(
        'Password', blank=False, null=False, max_length=500, db_index=True
    )
    email = models.EmailField(
        'email', blank=False, null=False, max_length=254, db_index=True
    )
    token = models.CharField(
        'token', blank=True, null=True, max_length=500, db_index=True
    )
    token_expires_at = models.DateTimeField(
        'Token Expires Datetime', null=True, default=timezone.now() + timedelta(days=360)
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )

    def __str__(self):
        return self.user_name
