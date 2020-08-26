from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1',
            'password2'
        ]
