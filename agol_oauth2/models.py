from django.db import models
from django.contrib.auth.models import User


class AGOLUserFields(models.Model):
    """ required to match agol user to django """
    agol_username = models.CharField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agol_info')

