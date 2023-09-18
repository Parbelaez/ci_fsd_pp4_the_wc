from .models import Comment, Writing
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_type','content')

class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ('title', 'main_genre', 'sub_genre', 'content', 'featured_image', 'abstract')