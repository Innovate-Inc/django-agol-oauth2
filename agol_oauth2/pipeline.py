from django.contrib.auth.models import User
from social_core.exceptions import AuthException
from agol_oauth2.models import AGOLUserFields


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


def create_users_in_flagged_groups(backend, details, user=None, *args, **kwargs):
    if user:
        return None

    username = details.get('username')
    groups = details.get('groups')
    whitelist_groups = backend.setting('WHITELIST_GROUPS')
    matching_groups = set(groups) & set(whitelist_groups)

    if username and len(matching_groups) > 0:
        user = User.objects.create_user(username, details['email'], User.objects.make_random_password())
        AGOLUserFields.objects.create(user=user, agol_username=username)

        return {'user': user,
                'is_new': False}
