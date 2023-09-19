from .models import Comment, Writing
from django import forms
# from django.utils.text import slugify
# from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writing_type','content')

class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ('title', 'main_genre', 'sub_genre', 'content', 'featured_image', 'abstract')

    # def slug_title(self, title):
    #     slug = slugify(title)

    #     if Writing.objects.filter(slug=slug).exists():
    #         raise ValidationError('A writing with this title already exists.')

    #     return title