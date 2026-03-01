from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

    


def validate_username(username):
    if " " in username:
        raise ValidationError(
            _("Username cannot contain spaces"),
        )
        
def validate_password_strength(password):
    if len(password) < 8:
        raise ValidationError(
            _("Password must be at least 8 characters long"),
        )
    if not any(char.isdigit() for char in password):
        raise ValidationError(
            _("Password must contain at least one digit"),
        )
    if not any(char.isalpha() for char in password):
        raise ValidationError(
            _("Password must contain at least one letter"),
        )

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, email):
        return True
    
    else:
        raise ValidationError(
            _("Please enter a valid email address"),
        )
        
def validate_date_of_birth(date_of_birth):
    from datetime import date
    if date_of_birth >= date.today():
        raise ValidationError(
            _("Date of birth must be in the past"),
        )
