from django import forms
from blog.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','published_date']
