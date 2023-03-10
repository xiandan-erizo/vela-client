# coding: utf-8

"""
    Kubevela api doc

    Kubevela api doc  # noqa: E501

    OpenAPI spec version: v1beta1
    Contact: feedback@mail.kubevela.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vela_client
from vela_client.api.rbac_api import RbacApi  # noqa: E501
from vela_client.rest import ApiException


class TestRbacApi(unittest.TestCase):
    """RbacApi unit test stubs"""

    def setUp(self):
        self.api = RbacApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_platform_permission(self):
        """Test case for create_platform_permission

        create the platform perm policy  # noqa: E501
        """
        pass

    def test_create_platform_role(self):
        """Test case for create_platform_role

        create platform level role  # noqa: E501
        """
        pass

    def test_delete_platform_permission(self):
        """Test case for delete_platform_permission

        delete a platform perm policy  # noqa: E501
        """
        pass

    def test_delete_platform_role(self):
        """Test case for delete_platform_role

        update platform level role  # noqa: E501
        """
        pass

    def test_list_platform_permissions(self):
        """Test case for list_platform_permissions

        list all platform level perm policies  # noqa: E501
        """
        pass

    def test_list_platform_roles(self):
        """Test case for list_platform_roles

        list all platform level roles  # noqa: E501
        """
        pass

    def test_update_platform_role(self):
        """Test case for update_platform_role

        update platform level role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
