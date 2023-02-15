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


class EnvApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def envcreate(self, body, **kwargs):  # noqa: E501
        """create an env  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envcreate(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateEnvRequest body: (required)
        :return: V1Env
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.envcreate_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.envcreate_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def envcreate_with_http_info(self, body, **kwargs):  # noqa: E501
        """create an env  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envcreate_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateEnvRequest body: (required)
        :return: V1Env
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method envcreate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `envcreate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/api/v1/envs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1Env',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def envdelete(self, env_name, **kwargs):  # noqa: E501
        """delete one env  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envdelete(env_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str env_name: identifier of the environment (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.envdelete_with_http_info(env_name, **kwargs)  # noqa: E501
        else:
            (data) = self.envdelete_with_http_info(env_name, **kwargs)  # noqa: E501
            return data

    def envdelete_with_http_info(self, env_name, **kwargs):  # noqa: E501
        """delete one env  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envdelete_with_http_info(env_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str env_name: identifier of the environment (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['env_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method envdelete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'env_name' is set
        if ('env_name' not in params or
                params['env_name'] is None):
            raise ValueError("Missing the required parameter `env_name` when calling `envdelete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'env_name' in params:
            path_params['envName'] = params['env_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ["BearerToken"]  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/envs/{envName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1EmptyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def envlist(self, **kwargs):  # noqa: E501
        """list all envs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envlist(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListEnvResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.envlist_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.envlist_with_http_info(**kwargs)  # noqa: E501
            return data

    def envlist_with_http_info(self, **kwargs):  # noqa: E501
        """list all envs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envlist_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListEnvResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method envlist" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ["BearerToken"]  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/envs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListEnvResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def envupdate(self, body, env_name, **kwargs):  # noqa: E501
        """update an env  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envupdate(body, env_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateEnvRequest body: (required)
        :param str env_name: identifier of the environment (required)
        :return: V1Env
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.envupdate_with_http_info(body, env_name, **kwargs)  # noqa: E501
        else:
            (data) = self.envupdate_with_http_info(body, env_name, **kwargs)  # noqa: E501
            return data

    def envupdate_with_http_info(self, body, env_name, **kwargs):  # noqa: E501
        """update an env  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.envupdate_with_http_info(body, env_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateEnvRequest body: (required)
        :param str env_name: identifier of the environment (required)
        :return: V1Env
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'env_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method envupdate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `envupdate`")  # noqa: E501
        # verify the required parameter 'env_name' is set
        if ('env_name' not in params or
                params['env_name'] is None):
            raise ValueError("Missing the required parameter `env_name` when calling `envupdate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'env_name' in params:
            path_params['envName'] = params['env_name']  # noqa: E501

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
            '/api/v1/envs/{envName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1Env',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
