#coding=utf-8
"""URL API routing configuration.  UCMP"""

from django.conf.urls import url
from api.jwt.api_handler import (
    jwt_handler,
    user_handler
)
# from maasserver.api.not_found import not_found_handler


urlpatterns = [
    url(
        r'^jwt/(?P<system_id>[^/]+)/$', jwt_handler,
        name='jwt_handler'),
    url(r'^token/$', user_handler, name='user_handler'),
]

# Last resort: return an API 404 response.
# urlpatterns += [
#     url(r'^.*', not_found_handler, name='handler_404')
# ]