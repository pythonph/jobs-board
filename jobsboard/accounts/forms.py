from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .validators import validate_user_email_exists


class CreateUser(UserCreationForm):
    email = forms.EmailField(
        required=True,
        validators=[validate_user_email_exists]
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username__iexact=username)
        if user.exists():
            err = 'That username already exists.'
            self.add_error('username', err)
        else:
            return username.lower()

    def save(self, **kwargs):
        from accounts.models import Account
        try:
            data = self.cleaned_data
            user = super().save()
            email = data.get('email')
            user.email = email
            user.save()
            Account.objects.create(user=user)
            return user
        except Exception as err:
            raise err


class ProfileUpdate(forms.ModelForm):
    """Updates the user and account record of a user
    Remember to initialize this form with an `initial` and `instance`
    parameters.

    This is the form to use for updating a user's account info

    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user = self.instance

        if not self.initial:
            raise ValidationError(
                'The initial parameter must be passed.'
            )

        if not isinstance(user, User):
            raise ValidationError(
                'A User instance must be passed.'
            )

        # If the email is the same as the old one, its all cool.
        try:
            validate_user_email_exists(email)
        except ValidationError as err:
            email_retained = email == user.email
            if not email_retained:
                self.add_error('email', err)
