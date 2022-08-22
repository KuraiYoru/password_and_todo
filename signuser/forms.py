from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(UserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].help_text = ''
    #     self.fields['password1'].help_text = ''
    #     self.fields['password2'].help_text = ''
    username = forms.CharField(label='username', min_length=5, max_length=30)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("username")

        if cc_myself:
            # Only do something if both fields are valid so far.
                raise ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )
