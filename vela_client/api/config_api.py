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


class ConfigApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_config(self, body, **kwargs):  # noqa: E501
        """create or update a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_config(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateConfigRequest body: (required)
        :return: V1Config
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_config_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_config_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_config_with_http_info(self, body, **kwargs):  # noqa: E501
        """create or update a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_config_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateConfigRequest body: (required)
        :return: V1Config
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
                    " to method create_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_config`")  # noqa: E501

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
            '/api/v1/configs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1Config',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_config(self, config_name, **kwargs):  # noqa: E501
        """delete a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_config(config_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_name: identifier of the config (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_config_with_http_info(config_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_config_with_http_info(config_name, **kwargs)  # noqa: E501
            return data

    def delete_config_with_http_info(self, config_name, **kwargs):  # noqa: E501
        """delete a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_config_with_http_info(config_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_name: identifier of the config (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_name' is set
        if ('config_name' not in params or
                params['config_name'] is None):
            raise ValueError("Missing the required parameter `config_name` when calling `delete_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'config_name' in params:
            path_params['configName'] = params['config_name']  # noqa: E501

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
            '/api/v1/configs/{configName}', 'DELETE',
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

    def get_config(self, config_name, **kwargs):  # noqa: E501
        """detail a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config(config_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_name: identifier of the config (required)
        :return: list[V1Config]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_config_with_http_info(config_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_config_with_http_info(config_name, **kwargs)  # noqa: E501
            return data

    def get_config_with_http_info(self, config_name, **kwargs):  # noqa: E501
        """detail a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_with_http_info(config_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_name: identifier of the config (required)
        :return: list[V1Config]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_name' is set
        if ('config_name' not in params or
                params['config_name'] is None):
            raise ValueError("Missing the required parameter `config_name` when calling `get_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'config_name' in params:
            path_params['configName'] = params['config_name']  # noqa: E501

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
            '/api/v1/configs/{configName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[V1Config]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_config_template(self, template_name, **kwargs):  # noqa: E501
        """Detail a template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_template(template_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_name: identifier of the config template (required)
        :param str namespace: the name of the namespace
        :return: V1ConfigTemplateDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_config_template_with_http_info(template_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_config_template_with_http_info(template_name, **kwargs)  # noqa: E501
            return data

    def get_config_template_with_http_info(self, template_name, **kwargs):  # noqa: E501
        """Detail a template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_template_with_http_info(template_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_name: identifier of the config template (required)
        :param str namespace: the name of the namespace
        :return: V1ConfigTemplateDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_name', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_name' is set
        if ('template_name' not in params or
                params['template_name'] is None):
            raise ValueError("Missing the required parameter `template_name` when calling `get_config_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_name' in params:
            path_params['templateName'] = params['template_name']  # noqa: E501

        query_params = []
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

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
            '/api/v1/config_templates/{templateName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ConfigTemplateDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_configs(self, **kwargs):  # noqa: E501
        """list all configs that belong to the system scope  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template: the name of the template
        :return: V1ListConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_configs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_configs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_configs_with_http_info(self, **kwargs):  # noqa: E501
        """list all configs that belong to the system scope  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template: the name of the template
        :return: V1ListConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_configs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template' in params:
            query_params.append(('template', params['template']))  # noqa: E501

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
            '/api/v1/configs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListConfigResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_config_templates(self, **kwargs):  # noqa: E501
        """List all config templates from the system namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_config_templates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListConfigTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_config_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_config_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_config_templates_with_http_info(self, **kwargs):  # noqa: E501
        """List all config templates from the system namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_config_templates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListConfigTemplateResponse
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
                    " to method list_config_templates" % key
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
            '/api/v1/config_templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListConfigTemplateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_config(self, config_name, **kwargs):  # noqa: E501
        """update a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_config(config_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_name: identifier of the config (required)
        :return: list[V1UpdateConfigRequest]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_config_with_http_info(config_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_config_with_http_info(config_name, **kwargs)  # noqa: E501
            return data

    def update_config_with_http_info(self, config_name, **kwargs):  # noqa: E501
        """update a config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_config_with_http_info(config_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_name: identifier of the config (required)
        :return: list[V1UpdateConfigRequest]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_name' is set
        if ('config_name' not in params or
                params['config_name'] is None):
            raise ValueError("Missing the required parameter `config_name` when calling `update_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'config_name' in params:
            path_params['configName'] = params['config_name']  # noqa: E501

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
            '/api/v1/configs/{configName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[V1UpdateConfigRequest]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
