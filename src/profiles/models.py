from django.db import models
from django.conf import settings
from django.db.models.signals import post_save	
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from .choices import *


class MyUserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			username = username,
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(
			username,
			email,
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.save(using=self._db)
		return user

USERNAME_REGEX = '^[a-zA-Z0-9@.+-]*$'
class MyUser(AbstractBaseUser):
	username = models.CharField(
		verbose_name='İstifadəçi adı',
		max_length=255,
		validators=[
			RegexValidator(
				regex = USERNAME_REGEX,
				message = 'lalala',
				code = 'invalid username'
			)
		],
		unique=True,
	)
	email = models.EmailField(
		verbose_name='E-mail',
		max_length=255,
		unique=True,
	)
	blood_group 	= models.IntegerField(choices=BLOOD_GROUP,default=1, null=True)
	birth_date 		= models.DateField(auto_now=False, blank=True, null=True)
	last_blood_date	= models.DateField(blank=True, null=True)
	gender			= models.IntegerField(choices=GENDER_CHOICES,default=1, null=True)
	first_name  	= models.CharField(max_length=120,blank=False, null=True)
	last_name 		= models.CharField(max_length=120,blank=False, null=True)
	illness 		= models.IntegerField(choices=ILLNESS_CHOICES,default=1, null=True)
	illness1 		= models.IntegerField(choices=ILLNESS_CHOICES,default=1, null=True)
	illness2 		= models.IntegerField(choices=ILLNESS_CHOICES,default=1, null=True)
	weight			= models.IntegerField(blank=False,default=50)
	height 			= models.IntegerField(blank=False,default=160)




	is_active = models.BooleanField(default=True)
	is_staff  = models.BooleanField(default=False)
	is_admin  = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):              # __unicode__ on Python 2
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	

