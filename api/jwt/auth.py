# Copyright 2012-2016 Canonical Ltd.  This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

"""keystone authentication for the various APIs."""

__all__ = [
    'jwt_auth',
    ]

from operator import xor


from piston3.authentication import (
    OAuthAuthentication,
    send_oauth_error,
)
from piston3.oauth import OAuthError
from piston3.utils import rc


from django.conf import settings
from django.contrib.auth.models import User
from api.jwt.jwt_helper import JwtHelper


class JWtAuthentication(object):
    """Use the currently logged-in user; resort to OAuth if there isn't one.

    There may be a user already logged-in via another mechanism, like a
    familiar in-browser user/pass challenge.
    """
    def __init__(self, realm='API'):
        self.realm = realm


    def is_authenticated(self, request):
        user = request.user
        if user.is_authenticated:
            # only authenticate if user is local and external auth is disabled
            # or viceversa
            return xor(
                bool(request.external_auth_info), user.userprofile.is_local)

        # The following is much the same as is_authenticated from ucmpkeystone
        # , with the difference that an OAuth request that
        # does not validate is rejected instead of being silently downgraded.
        if self.is_valid_request(request):
            try:
                token_status, ucmp_user = self.validate_token(request)
            except Exception as error:
                raise error

            # checkout keystone login and user
            if token_status and ucmp_user:
                # try:
                #     # system login root user, must check out settings
                #     user = User.objects.get(username=settings.UCMPROOT)
                # except User.DoesNotExist:
                #     raise Exception("you must set the first init user into django settings")
                #
                # request.user = user
                # request.ucmp_user = ucmp_user
                from collections import namedtuple
                User = namedtuple("User", ("is_active"))
                request.user = User(True)
                return True

            else:
                return False

        return False

    def challenge(self, request):
        # Beware: this returns 401: Unauthorized, not 403: Forbidden
        # as the name implies.
        return rc.FORBIDDEN

    @staticmethod
    def is_valid_request(request):
        """
        Checks whether the required parameters are either in
        the http-authorization header sent by some clients,
        which is by the way the preferred method according to
        keystone, but otherwise fall back to `GET` and `POST`.
        """
        # auth_params = request.META.get("HTTP_X_SUBJECT_TOKEN", None)

        auth_params = True
        return True if auth_params else False

    @staticmethod
    def validate_token(request):
        token = request.META.get("HTTP_X_SUBJECT_TOKEN","")
        import pdb
        toke_status, ucmp_user  = JwtHelper.validate(token)
        return toke_status, ucmp_user


# keystone and macaroon-based authentication for the APIs.
jwt_auth = (
    JWtAuthentication("API"),
)
