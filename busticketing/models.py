from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models 
from django.utils import timezone
from django.conf import settings
# from django.contrib.auth.models import User
from .validators import validate_file_extension     
class UserProfile(models.Model): 
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_user = models.BooleanField(default=False)
	is_agent = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username
