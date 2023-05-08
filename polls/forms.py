import phonenumbers
from django import forms
from django.core.exceptions import ValidationError

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "year", "phone"]

    def clean_phone(self):
        phone_r = self.cleaned_data["phone"]
        try:
            phone = phonenumbers.parse(phone_r, None)
        except phonenumbers.NumberParseException:
            raise ValidationError("Phone is not valid!")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone is invalid")
        return phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
