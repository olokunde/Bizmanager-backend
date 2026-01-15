from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='customer'
    )

    # 🔑 FIX FOR GROUPS CLASH
    groups = models.ManyToManyField(
        Group,
        related_name="users_custom_set",
        blank=True
    )

    # 🔑 FIX FOR PERMISSIONS CLASH
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="users_custom_permissions_set",
        blank=True
    )

    def __str__(self):
        return self.username
