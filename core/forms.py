from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username',
                                                             'class': 'w-full py-4 px-6 rounded-xl'
                                                             }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',
                                                                 'class': 'w-full py-4 px-6 rounded-xl'
                                                                 }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username',
                                                             'class': 'w-full py-4 px-6 rounded-xl'
                                                             }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your E-mail address',
                                                           'class': 'w-full py-4 px-6 rounded-xl'
                                                           }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',
                                                                  'class': 'w-full py-4 px-6 rounded-xl'
                                                                  }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password',
                                                                  'class': 'w-full py-4 px-6 rounded-xl'
                                                                  }))
