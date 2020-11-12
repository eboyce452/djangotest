from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Model_Name(models.Model):
        #     f_name = models.CharField(max_length = 256)
        #     l_name = models.CharField(max_length = 256)

        #     def __str__(self):
        #         return str(self.f_name + ' ' + self.l_name)

class UserProfileInfo(models.Model):

	user = models.OneToOneField(User)

	portfolio_site = models.URLField(blank = True)
	profile_pic = models.ImageField(upload_to='ppic', blank=True)

	def __str__(self):
		return self.user.username