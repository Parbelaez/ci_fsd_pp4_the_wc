from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writing_type','content')