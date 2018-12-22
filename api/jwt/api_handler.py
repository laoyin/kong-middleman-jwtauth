#coding=utf-8
#author : yxp

"""
    api handler and privileges for api url
"""

__all__ = [
    'jwt_handler',
    'user_handler'
    ]

from api.jwt.user_handler import (
    JwtHandler,
    UserHandler
)

from api.jwt.support import (
    RestrictedResource
)

from api.jwt.auth import jwt_auth


jwt_handler = RestrictedResource(UserHandler, authentication=jwt_auth)
user_handler = RestrictedResource(JwtHandler, authentication=jwt_auth)