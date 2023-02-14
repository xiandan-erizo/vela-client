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
from vela_client.api.users_api import UsersApi  # noqa: E501
from vela_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        create a user  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        delete a user  # noqa: E501
        """
        pass

    def test_detail_user(self):
        """Test case for detail_user

        get user detail  # noqa: E501
        """
        pass

    def test_disable_user(self):
        """Test case for disable_user

        disable a user  # noqa: E501
        """
        pass

    def test_enable_user(self):
        """Test case for enable_user

        enable a user  # noqa: E501
        """
        pass

    def test_list_user(self):
        """Test case for list_user

        list users  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        update a user's alias or password  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()