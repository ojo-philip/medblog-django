from django import forms
from django.contrib.auth.forms import UserCreationForm,  PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import UserProfile


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'input-control'}))

    class Meta:
        fields = ['email']


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', max_length=32,
                                    widget=forms.PasswordInput(attrs={'class': 'input-control'}))
    new_password2 = forms.CharField(label='New Password Confirmation', max_length=32,
                                    widget=forms.PasswordInput(attrs={'class': 'input-control'}))

    class Meta:
        fields = ['new_password1', 'new_password2']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'input-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'input-control'}))
    password1 = forms.CharField(label='password',
                                max_length=32, widget=forms.PasswordInput(attrs={'class': 'input-control'}))
    password2 = forms.CharField(label='password confirmation',
                                max_length=32, widget=forms.PasswordInput(attrs={'class': 'input-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-control'}),
            'email': forms.EmailInput(attrs={'class': 'input-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'image', 'about_you']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-control'}),
            'last_name': forms.TextInput(attrs={'class': 'input-control'}),
            'about_you': forms.Textarea(attrs={'class': 'input-control'}),
            'image': forms.FileInput(attrs={'class': 'file-control'}),
        }
