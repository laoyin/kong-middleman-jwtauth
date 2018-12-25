#coding=utf-8
"""
learn from maas
"""
__all__ = [
    "UserHandler",
    "JwtHandler",
]

import re

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from api.jwt.support import OperationsHandler
from api.jwt.support import (
    admin_method,
    operation,
)
from api.models import User
import yaml


# User's fields exposed on the API.
DISPLAYED_User_FIELDS = (
    'id',
    'user_name',
    'service',
)


class UserHandler(OperationsHandler):
    """Manage User Login.
    """
    api_doc_section_name = "Node"

    # Disable create and update
    create = update = None
    model = User
    fields = DISPLAYED_User_FIELDS

    def delete(self, request, system_id):
        pass

    def get(self):
        pass

    @classmethod
    def resource_uri(cls, node=None):
        return ('user_handler', [])

    @operation(idempotent=True)
    def details(self, request, system_id):
        pass


class JwtHandler(OperationsHandler):
    api_doc_section_name = "Machines"
    model = User
    fields = DISPLAYED_User_FIELDS

    def list(self, request):
        return []

    def get(self, request):
        return {"nihao":"awewf"}

    def create(self, request):
        return []

    @operation(idempotent=True)
    def list_allocated(self, request):
        return []

    @operation(idempotent=False)
    def allocate(self, request):
        return []

    @classmethod
    def resource_uri(cls, *args, **kwargs):
        return ('jwt_handler', [])