from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email"
        )
