from django.contrib.auth.models import User
from django.db.models import Q


class CaseInsensitiveAuth(object):
    #To do this, you need to update your models to username and email entries to 
    #the database case-insensitive. Otherwise, you can have two users named John as
    # 'John' and 'john'
    def authenticate(self, username=None, email=None, password=None):
        """
        Get an instance of User using the supplied username
        or email and check its password
        """
        try:
            # Filter all users by searching for a match by username/ email. Get the first instance returned
            # in the QuerySet
            user = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username))[:1].get()
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

