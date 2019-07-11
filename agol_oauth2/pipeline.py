from django.contrib.auth.models import User
from social_core.exceptions import AuthException


def associate_by_username(backend, details, user=None, *args, **kwargs):
    if user:
        return None

    username = details.get('username')
    if username:
        # Try to associate accounts registered with the same username,
        # only if it's a single object. AuthException is raised if multiple
        # objects are returned.
        users = list(User.objects.filter(agol_info__agol_username=username))
        if len(users) == 0:
            return None
        elif len(users) > 1:
            raise AuthException(
                backend,
                'The given username is associated with another account'
            )
        else:
            return {'user': users[0],
                    'is_new': False}


