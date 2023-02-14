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


class AddonApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def detail_addon(self, name, addon_name, **kwargs):  # noqa: E501
        """show details of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detail_addon(name, addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: addon name to query detail (required)
        :param str addon_name: addon name to query detail (required)
        :param str version: specify addon version to enable
        :param str registry: filter addons from given registry
        :return: V1DetailAddonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.detail_addon_with_http_info(name, addon_name, **kwargs)  # noqa: E501
        else:
            (data) = self.detail_addon_with_http_info(name, addon_name, **kwargs)  # noqa: E501
            return data

    def detail_addon_with_http_info(self, name, addon_name, **kwargs):  # noqa: E501
        """show details of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detail_addon_with_http_info(name, addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: addon name to query detail (required)
        :param str addon_name: addon name to query detail (required)
        :param str version: specify addon version to enable
        :param str registry: filter addons from given registry
        :return: V1DetailAddonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'addon_name', 'version', 'registry']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method detail_addon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `detail_addon`")  # noqa: E501
        # verify the required parameter 'addon_name' is set
        if ('addon_name' not in params or
                params['addon_name'] is None):
            raise ValueError("Missing the required parameter `addon_name` when calling `detail_addon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'addon_name' in params:
            path_params['addonName'] = params['addon_name']  # noqa: E501

        query_params = []
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'registry' in params:
            query_params.append(('registry', params['registry']))  # noqa: E501

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
            '/api/v1/addons/{addonName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1DetailAddonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def disable_addon(self, addon_name, **kwargs):  # noqa: E501
        """disable an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_addon(addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str addon_name: addon name to enable (required)
        :param bool force: force disable an addon
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.disable_addon_with_http_info(addon_name, **kwargs)  # noqa: E501
        else:
            (data) = self.disable_addon_with_http_info(addon_name, **kwargs)  # noqa: E501
            return data

    def disable_addon_with_http_info(self, addon_name, **kwargs):  # noqa: E501
        """disable an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_addon_with_http_info(addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str addon_name: addon name to enable (required)
        :param bool force: force disable an addon
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_name', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_addon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_name' is set
        if ('addon_name' not in params or
                params['addon_name'] is None):
            raise ValueError("Missing the required parameter `addon_name` when calling `disable_addon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_name' in params:
            path_params['addonName'] = params['addon_name']  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

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
            '/api/v1/addons/{addonName}/disable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1AddonStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_addon(self, body, addon_name, **kwargs):  # noqa: E501
        """enable an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_addon(body, addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1EnableAddonRequest body: (required)
        :param str addon_name: addon name to enable (required)
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enable_addon_with_http_info(body, addon_name, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_addon_with_http_info(body, addon_name, **kwargs)  # noqa: E501
            return data

    def enable_addon_with_http_info(self, body, addon_name, **kwargs):  # noqa: E501
        """enable an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_addon_with_http_info(body, addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1EnableAddonRequest body: (required)
        :param str addon_name: addon name to enable (required)
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'addon_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_addon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `enable_addon`")  # noqa: E501
        # verify the required parameter 'addon_name' is set
        if ('addon_name' not in params or
                params['addon_name'] is None):
            raise ValueError("Missing the required parameter `addon_name` when calling `enable_addon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_name' in params:
            path_params['addonName'] = params['addon_name']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/addons/{addonName}/enable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1AddonStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """list all enabled addons  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str registry: filter addons from given registry
        :param str query: Fuzzy search based on name and description.
        :return: V1ListEnabledAddonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """list all enabled addons  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str registry: filter addons from given registry
        :param str query: Fuzzy search based on name and description.
        :return: V1ListEnabledAddonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registry', 'query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'registry' in params:
            query_params.append(('registry', params['registry']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

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
            '/api/v1/enabled_addon', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListEnabledAddonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_addons(self, **kwargs):  # noqa: E501
        """list all addons  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addons(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str registry: filter addons from given registry
        :param str query: Fuzzy search based on name and description.
        :return: V1ListAddonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_addons_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_addons_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_addons_with_http_info(self, **kwargs):  # noqa: E501
        """list all addons  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addons_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str registry: filter addons from given registry
        :param str query: Fuzzy search based on name and description.
        :return: V1ListAddonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registry', 'query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_addons" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'registry' in params:
            query_params.append(('registry', params['registry']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

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
            '/api/v1/addons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListAddonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def status_addon(self, addon_name, **kwargs):  # noqa: E501
        """show status of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.status_addon(addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str addon_name: addon name to query status (required)
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.status_addon_with_http_info(addon_name, **kwargs)  # noqa: E501
        else:
            (data) = self.status_addon_with_http_info(addon_name, **kwargs)  # noqa: E501
            return data

    def status_addon_with_http_info(self, addon_name, **kwargs):  # noqa: E501
        """show status of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.status_addon_with_http_info(addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str addon_name: addon name to query status (required)
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method status_addon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_name' is set
        if ('addon_name' not in params or
                params['addon_name'] is None):
            raise ValueError("Missing the required parameter `addon_name` when calling `status_addon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_name' in params:
            path_params['addonName'] = params['addon_name']  # noqa: E501

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
            '/api/v1/addons/{addonName}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1AddonStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_addon(self, body, addon_name, **kwargs):  # noqa: E501
        """update an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon(body, addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1EnableAddonRequest body: (required)
        :param str addon_name: addon name to update (required)
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_addon_with_http_info(body, addon_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_addon_with_http_info(body, addon_name, **kwargs)  # noqa: E501
            return data

    def update_addon_with_http_info(self, body, addon_name, **kwargs):  # noqa: E501
        """update an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon_with_http_info(body, addon_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1EnableAddonRequest body: (required)
        :param str addon_name: addon name to update (required)
        :return: V1AddonStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'addon_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_addon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_addon`")  # noqa: E501
        # verify the required parameter 'addon_name' is set
        if ('addon_name' not in params or
                params['addon_name'] is None):
            raise ValueError("Missing the required parameter `addon_name` when calling `update_addon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_name' in params:
            path_params['addonName'] = params['addon_name']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/addons/{addonName}/update', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1AddonStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
