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
from vela_client.api.repository_api import RepositoryApi  # noqa: E501
from vela_client.rest import ApiException


class TestRepositoryApi(unittest.TestCase):
    """RepositoryApi unit test stubs"""

    def setUp(self):
        self.api = RepositoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chart_values(self):
        """Test case for chart_values

        get chart value  # noqa: E501
        """
        pass

    def test_get_image_info(self):
        """Test case for get_image_info

        get the oci repos  # noqa: E501
        """
        pass

    def test_get_image_repos(self):
        """Test case for get_image_repos

        get the oci repos  # noqa: E501
        """
        pass

    def test_list_charts(self):
        """Test case for list_charts

        list charts  # noqa: E501
        """
        pass

    def test_list_repo(self):
        """Test case for list_repo

        list chart repo  # noqa: E501
        """
        pass

    def test_list_versions(self):
        """Test case for list_versions

        list versions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
