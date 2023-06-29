from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Define additional fields for your custom user model
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=128, blank=True, null=True, default=None)

    # Override the username field to be nullable
    username = models.CharField(max_length=150, null=True, blank=True)

    # Override the email field to be non-null
    email = models.EmailField(unique=True)

    # Set the USERNAME_FIELD to 'email' for authentication
    USERNAME_FIELD = 'email'
    # Set the REQUIRED_FIELDS to include 'email' for the createsuperuser management command
    REQUIRED_FIELDS = []

    # Add a related_name argument to avoid clashes
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
