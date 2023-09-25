from .models import Comment, Writing, Genre
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writing_type','content')
        widgets = {
            'content': SummernoteWidget(),
        }

class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ('title', 'main_genre', 'sub_genre', 'content', 'featured_image', 'abstract')
        widgets = {
            'content': SummernoteWidget(),
            'abstract': SummernoteWidget(),
        }