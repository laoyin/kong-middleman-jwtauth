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
        #
        # This method is called by Piston in two different contexts:
        #
        # 1. When generating a URI template to be used in the documentation,
        #    in which case it is called with `node=None`. We return argument
        #    *names* instead of their values. Frustratingly, Piston itself
        #    discards these names and instead uses names derived from Django's
        #    URL patterns for the resource.
        #
        # 2. When populating the `resource_uri` field of an object returned by
        #    the API, in which case `node` is an instance of `Node`.
        #
        # There is a check made at handler class creation time to ensure that
        # the names from #1 match up to the handler's `fields`. In this way we
        # can declare which fields are required to render a resource's URI and
        # be sure that they are all present in a rendering of said resource.
        #
        # There is an additional unit test (see `TestResourceURIs`) to check
        # that the fields in each URI template match up to those fields
        # declared in a handler's `resource_uri` method.
        #
            # node_system_id = "system_id"
            # if node is not None:
            #     node_system_id = node.system_id
            # return ('node_handler', (node_system_id, ))
        return ('user_handler', [])

    @operation(idempotent=True)
    def details(self, request, system_id):
        pass


class JwtHandler(OperationsHandler):
    """Manage the collection of all the machines in the MAAS."""
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