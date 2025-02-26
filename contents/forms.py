from django import forms
from . models import Contents

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ['content', 'image']