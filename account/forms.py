from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'email'}))

    # password1 = forms.PasswordInput()
    # password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        
        password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
        password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name in ['username','password1', 'password2']:
            self.fields[field_name].widget.attrs['placeholder'] = self.fields[field_name].label
            self.fields[field_name].help_text = None


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput()
