from coldfront.config.base import INSTALLED_APPS, MIDDLEWARE
from coldfront.config.auth import AUTHENTICATION_BACKENDS

#------------------------------------------------------------------------------
# Enable Mokey/Hydra OpenID Connect Authentication Backend
#------------------------------------------------------------------------------
INSTALLED_APPS += [
    'mozilla_django_oidc',
    'coldfront.plugins.mokey_oidc',
]

AUTHENTICATION_BACKENDS += [
    'coldfront.plugins.mokey_oidc.auth.OIDCMokeyAuthenticationBackend',
]

MIDDLEWARE += [
    'mozilla_django_oidc.middleware.SessionRefresh',
]

OIDC_OP_JWKS_ENDPOINT = ''
OIDC_RP_SIGN_ALGO = ''
OIDC_RP_CLIENT_ID = ''
OIDC_RP_CLIENT_SECRET = ''
OIDC_OP_AUTHORIZATION_ENDPOINT = ''
OIDC_OP_TOKEN_ENDPOINT = ''
OIDC_OP_USER_ENDPOINT = ''
OIDC_VERIFY_SSL = True
OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS = 3600
