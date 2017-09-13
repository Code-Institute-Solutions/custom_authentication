from django.contrib.auth.models import User


class EmailAuth(object):
    def authenticate(self, username=None, password=None):
        """
       Get an instance of User using the supplied email and check its password
       """
        try:
            # Get a User instance using the supplied email or username
            user = User.objects.get(email=username)
            # Check if the password submitted matches that of this User
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
       Used by the django authentication system to retrieve an instance of User
       """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            
        except User.DoesNotExist:
            return None
