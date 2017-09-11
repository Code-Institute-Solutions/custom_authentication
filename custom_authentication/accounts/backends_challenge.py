from django.contrib.auth.models import User


class CaseInsensitiveAuth(object):
    def authenticate(self, username=None, password=None):
        """
       Get an instance of User using the supplied username or email and check its password
       """
        try:
            try:
                # Use a case insensitive query to check username
                user = User.objects.get(username__iexact=username)
                if user.check_password(password):
                    return user
                    
            except:
                # Use a case insensitive query to check email
                user = User.objects.get(email__iexact=username)
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
            return None
        except User.DoesNotExist:
            return None