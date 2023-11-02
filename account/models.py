from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserWords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_word = models.CharField(max_length=100)
    second_word = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     unique_together = ['user', 'first_word', 'second_word']