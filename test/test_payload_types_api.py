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
from vela_client.api.payload_types_api import PayloadTypesApi  # noqa: E501
from vela_client.rest import ApiException


class TestPayloadTypesApi(unittest.TestCase):
    """PayloadTypesApi unit test stubs"""

    def setUp(self):
        self.api = PayloadTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_payload_types(self):
        """Test case for list_payload_types

        list application trigger payload types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
