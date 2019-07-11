from social_core.backends.oauth import BaseOAuth2
from django.conf import settings


class AGOLOAuth2(BaseOAuth2):
    name = 'agol'
    ID_KEY = 'username'
    _AUTHORIZATION_URL = 'https://{}/sharing/rest/oauth2/authorize'
    _ACCESS_TOKEN_URL = 'https://{}/sharing/rest/oauth2/token'
    REQUIRES_EMAIL_VALIDATION = False
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token'),
        ('expires_in', 'expires'),
        ('username', 'username')
    ]

    def _base_url(self):
        _domain = self.setting('DOMAIN')
        domain = _domain if _domain else 'www.arcgis.com'
        return domain

    def authorization_url(self):
        return self._AUTHORIZATION_URL.format(self._base_url())

    def access_token_url(self):
        return self._ACCESS_TOKEN_URL.format(self._base_url())

    def get_user_details(self, response):
        if 'error' in response:
            return {}

        return {
            'username': response['username'],
            'email': response['email'],
            'fullname': response['fullName'],
            'first_name': response['fullName'].split()[0],
            'last_name': response['fullName'].split()[1]
        }

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json(
            'https://{}/sharing/rest/community/self'.format(self._base_url()),
            params={
                'token': access_token,
                'f': 'json'
            }
        )

    # api does support state... need to remove this and test
    def validate_state(self):
        return None

    # added so we can verify redirect_uri without having to actually redirect there
    # a slight hack to allow us to redirect to frontend oauthcallback page
    def get_redirect_uri(self, state=None):
        return self.setting('REDIRECT_URI')
