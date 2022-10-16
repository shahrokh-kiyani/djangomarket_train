from django import forms

from .models import Comment


class CommnetForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'stars']
