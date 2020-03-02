from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError

# Create your models here.


class Posts(models.Model):
    def min_length_check(val):
        if len(val) <= 10:
            raise ValidationError("%(val)s must be greater than 10", params={'val' : val})

    title = models.CharField(validators=[min_length_check],max_length=255)
    content = models.TextField(validators=[min_length_check])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']