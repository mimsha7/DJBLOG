from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError

# Create your models here.
def min_length_check(val):
    if len(val) <= 10:
        raise ValidationError("There is lenth {}".format(len(val)))
class Posts(models.Model):
    title = models.CharField(validators=[min_length_check],max_length=150,null=True)
    content = models.TextField(validators=[min_length_check],max_length=300,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']