from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class NfcAuthenticationBackend(ModelBackend):
    def authenticate(self, username=None, password=None, nfc_token=None):
        UserModel = get_user_model()

        if nfc_token is not None:
            return UserModel._default_manager.get(nfc_login_id=nfc_token)

        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)