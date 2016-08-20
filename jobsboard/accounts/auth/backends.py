from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class AccountVerificationMixin:

    def user_can_authenticate(self, user):
        """Reject is_active=False users. Allow them if they don't have that
        attribute

        """
        account = getattr(user, 'account', None)
        is_active = getattr(user, 'is_active', None)
        is_account_active = account and account.is_active
        return (
            (is_active or is_active is None) and
            (is_account_active or account is None)
        )


class UsernameBackend(AccountVerificationMixin, ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(username__iexact=username)
        except user_model.DoesNotExist:
            user_model().set_password(password)
        else:
            if (
                user.check_password(password) and
                self.user_can_authenticate(user)
            ):
                return user


class EmailBackend(AccountVerificationMixin, ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        # username in this context will be used in the email field instead
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            user_model().set_password(password)
        else:
            if (
                user.check_password(password) and
                self.user_can_authenticate(user)
            ):
                return user
