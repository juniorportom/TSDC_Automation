from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User  # gets the user_model django  default or your own custom
from django.db.models import Q

# Class to permit the athentication using email or username
class CustomBackend:  # requires to define two functions authenticate and get_user
    def authenticate(self, request, username=None, password=None):
        try:
            # below line gives query set,you can change the queryset as per your requirement
            user = User.objects.filter(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            ).distinct()

        except UserModel.DoesNotExist:
            return None

        if user.exists():
            ''' get the user object from the underlying query set,
            there will only be one object since username and email
            should be unique fields in your models.'''
            user_obj = user.first()
            if user_obj.check_password(password):
                return user_obj
            return None
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None