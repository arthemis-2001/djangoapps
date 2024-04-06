from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        """
        Meta options for the SignUpForm class.

        Attributes:
        - model: The User model
        - fields: The fields to include in the form
        """
        model = User
        fields = ["username", "email", "password1", "password2"]
    
