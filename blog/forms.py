from blog.models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import Comment
from django.forms import ModelForm
from django.urls import reverse
from django.views.generic import ListView, DetailView


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name',
                  'email': 'Email', }
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),

                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'password1': forms.TextInput(attrs={'class': 'form-control'}),
                   'password2': forms.TextInput(attrs={'class': 'form-control'}),

                   }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control '}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', ]
        labels = {'title': 'Title', 'desc': 'Description'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.Textarea(attrs={'class': 'form-control', 'id': "richtext"}),
                   }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        labels = {'name': 'Name', 'comment': 'Comment'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', },),
                   'comment': forms.Textarea(attrs={'class': 'form-control'}),
                   }

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'samuel':
            raise ValidationError("Sorry, you cannot use this name.")
        return data
