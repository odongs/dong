from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

# UserCreationForm이 가지고 있는
# ** username, password1, password2 속성에 부가 정보인 email 속성을 추가