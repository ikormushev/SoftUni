from django.core.exceptions import ValidationError


def name_validator(value):
    for s in value:
        if not (s.isalpha() or s.isspace()):
            raise ValidationError("Name can only contain letters and spaces")