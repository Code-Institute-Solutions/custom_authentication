from django.contrib.auth.models import User
from django.db.models import Q


class CaseInsensitiveAuth(object):
    """
    Authenticate an instance of User by using a case-insensitive query to check a 
    combination of the supplied email/username and password. 
    To avoid the risk of having two users with similar usernames, distinguished 
    only by capitalisations (e.g. 'john' and 'John'), consider updating your 
    User model to save usernames as lower case entries to the database. 
    This will ensure all usernames have unique spellings. As a result, our case 
    insensitive query will return one result only if all usernames are uniquely spelled. 
    """
    def authenticate(self, username=None, password=None):
        """
        Get an instance of User using the supplied username
        or email and check its password
        """
        try:
            # Filter all users by searching for a match by username/ email. 
            # Then get the first result of the query (which is your user).
            user = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username))[:1].get()
            # If the password is correct, return user object
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

