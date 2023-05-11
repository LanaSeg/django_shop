from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from app_users.models import Profile


class Error:
    error = {
        "phone_exists": "Номер уже зарегистрирован",
        "email_exists": "Почта уже зарегистрирован",
    }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", 'fullName', 'email', 'phone', 'password1', 'password2')
        field_classes = {"username": UsernameField}
    fullName = forms.CharField(required=True, label='Ф.И.О.', widget=forms.TextInput)
    phone = forms.CharField(required=True, label='Номер телефона', widget=forms.TextInput)
    password1 = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(required=True, label='Подтвердите пароль', widget=forms.PasswordInput)
    email = forms.CharField(required=True, label='Адрес электронной почты', widget=forms.EmailInput)

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        phone_in_db = Profile.objects.filter(phone=phone)
        if phone_in_db:
            raise ValidationError(self.Error.error[0])
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_in_db = User.objects.filter(email=email)
        if email_in_db:
            raise ValidationError(self.Error.error[1])
        return email