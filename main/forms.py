from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *

from .models import Aweitr
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class Ahop(ModelForm):
    class Meta:
        model = Aweitr
        fields = ["title", "anons", "text", "data"]

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Тема"},
            ),
            "anons": TextInput(
                attrs={"class": "form-control", "placeholder": "Анонс"},
            ),
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Текст"},
            ),
            "data": DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Дата публикацый",
                    "type": "datetime-local",
                },
            ),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-input", "id": "form-input1", "placeholder": "Логин"}
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "id": "form-input2", "placeholder": "Пароль"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password1")
