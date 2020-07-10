from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'input-control'}))
    password = forms.CharField(label='password',
                               max_length=32, widget=forms.PasswordInput(attrs={'class': 'input-control'}))

    class Meta:
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-control'}),
            'content': forms.Textarea(attrs={'class': 'input-control'}),
            'image': forms.FileInput(attrs={'class': 'file-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'input-control'}),
        }
