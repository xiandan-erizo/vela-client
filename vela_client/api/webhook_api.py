# coding: utf-8

"""
    Kubevela api doc

    Kubevela api doc  # noqa: E501

    OpenAPI spec version: v1beta1
    Contact: feedback@mail.kubevela.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vela_client.api_client import ApiClient


class WebhookApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def handle_application_webhook(self, body, token, **kwargs):  # noqa: E501
        """handle application webhook request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_application_webhook(body, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1HandleApplicationTriggerWebhookRequest body: (required)
        :param str token: webhook token (required)
        :return: V1ApplicationDeployResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_application_webhook_with_http_info(body, token, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_application_webhook_with_http_info(body, token, **kwargs)  # noqa: E501
            return data

    def handle_application_webhook_with_http_info(self, body, token, **kwargs):  # noqa: E501
        """handle application webhook request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_application_webhook_with_http_info(body, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1HandleApplicationTriggerWebhookRequest body: (required)
        :param str token: webhook token (required)
        :return: V1ApplicationDeployResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_application_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `handle_application_webhook`")  # noqa: E501
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `handle_application_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ["BearerToken"]  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/webhook/{token}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ApplicationDeployResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
