from django.core.exceptions import ValidationError

VALIDATE_ONLY_LETTER_EXCEPTION_MESSAGE = "Ensure this value contains only letter"


def validate_only_alphabetical(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTER_EXCEPTION_MESSAGE)