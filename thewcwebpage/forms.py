from .models import Comment, Writing, Genre
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from allauth.account.forms import SignupForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writing_type', 'content')
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


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
