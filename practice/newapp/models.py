from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.urls import reverse



class FormModel(models.Model):

    def __str__(self):
        return self.first_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    phone = PhoneField(blank=True, help_text='Contact phone number')


    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})