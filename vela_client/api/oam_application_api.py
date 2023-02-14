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


class OamApplicationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_or_update_application(self, body, namespace, appname, **kwargs):  # noqa: E501
        """create or update oam application in the specified namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_update_application(body, namespace, appname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1ApplicationRequest body: (required)
        :param str namespace: identifier of the namespace (required)
        :param str appname: identifier of the oam application (required)
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_or_update_application_with_http_info(body, namespace, appname, **kwargs)  # noqa: E501
        else:
            (data) = self.create_or_update_application_with_http_info(body, namespace, appname, **kwargs)  # noqa: E501
            return data

    def create_or_update_application_with_http_info(self, body, namespace, appname, **kwargs):  # noqa: E501
        """create or update oam application in the specified namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_or_update_application_with_http_info(body, namespace, appname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1ApplicationRequest body: (required)
        :param str namespace: identifier of the namespace (required)
        :param str appname: identifier of the oam application (required)
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'namespace', 'appname', 'dry_run']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_update_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_or_update_application`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `create_or_update_application`")  # noqa: E501
        # verify the required parameter 'appname' is set
        if ('appname' not in params or
                params['appname'] is None):
            raise ValueError("Missing the required parameter `appname` when calling `create_or_update_application`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'appname' in params:
            path_params['appname'] = params['appname']  # noqa: E501

        query_params = []
        if 'dry_run' in params:
            query_params.append(('dryRun', params['dry_run']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/namespaces/{namespace}/applications/{appname}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_oam_application(self, namespace, appname, **kwargs):  # noqa: E501
        """create or update oam application in the specified namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_oam_application(namespace, appname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: identifier of the namespace (required)
        :param str appname: identifier of the oam application (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_oam_application_with_http_info(namespace, appname, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_oam_application_with_http_info(namespace, appname, **kwargs)  # noqa: E501
            return data

    def delete_oam_application_with_http_info(self, namespace, appname, **kwargs):  # noqa: E501
        """create or update oam application in the specified namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_oam_application_with_http_info(namespace, appname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: identifier of the namespace (required)
        :param str appname: identifier of the oam application (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'appname']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_oam_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `delete_oam_application`")  # noqa: E501
        # verify the required parameter 'appname' is set
        if ('appname' not in params or
                params['appname'] is None):
            raise ValueError("Missing the required parameter `appname` when calling `delete_oam_application`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'appname' in params:
            path_params['appname'] = params['appname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/namespaces/{namespace}/applications/{appname}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_application(self, namespace, appname, **kwargs):  # noqa: E501
        """get the specified oam application in the specified namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application(namespace, appname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: identifier of the namespace (required)
        :param str appname: identifier of the oam application (required)
        :return: V1ApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_application_with_http_info(namespace, appname, **kwargs)  # noqa: E501
        else:
            (data) = self.get_application_with_http_info(namespace, appname, **kwargs)  # noqa: E501
            return data

    def get_application_with_http_info(self, namespace, appname, **kwargs):  # noqa: E501
        """get the specified oam application in the specified namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_with_http_info(namespace, appname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: identifier of the namespace (required)
        :param str appname: identifier of the oam application (required)
        :return: V1ApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'appname']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `get_application`")  # noqa: E501
        # verify the required parameter 'appname' is set
        if ('appname' not in params or
                params['appname'] is None):
            raise ValueError("Missing the required parameter `appname` when calling `get_application`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'appname' in params:
            path_params['appname'] = params['appname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/namespaces/{namespace}/applications/{appname}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ApplicationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
