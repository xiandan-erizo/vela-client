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
from vela_client.api.webhook_api import WebhookApi  # noqa: E501
from vela_client.rest import ApiException


class TestWebhookApi(unittest.TestCase):
    """WebhookApi unit test stubs"""

    def setUp(self):
        self.api = WebhookApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_handle_application_webhook(self):
        """Test case for handle_application_webhook

        handle application webhook request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
