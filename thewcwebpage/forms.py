from .models import Comment, Writing, Genre
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writing_type','content')

class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ('title', 'main_genre', 'sub_genre', 'content', 'featured_image', 'abstract')