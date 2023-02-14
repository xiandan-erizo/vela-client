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


class RbacApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_platform_permission(self, body, **kwargs):  # noqa: E501
        """create the platform perm policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_platform_permission(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreatePermissionRequest body: (required)
        :return: V1PermissionBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_platform_permission_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_platform_permission_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_platform_permission_with_http_info(self, body, **kwargs):  # noqa: E501
        """create the platform perm policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_platform_permission_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreatePermissionRequest body: (required)
        :return: V1PermissionBase
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
                    " to method create_platform_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_platform_permission`")  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/permissions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1PermissionBase',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_platform_role(self, body, **kwargs):  # noqa: E501
        """create platform level role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_platform_role(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateRoleRequest body: (required)
        :return: V1RoleBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_platform_role_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_platform_role_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_platform_role_with_http_info(self, body, **kwargs):  # noqa: E501
        """create platform level role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_platform_role_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1CreateRoleRequest body: (required)
        :return: V1RoleBase
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
                    " to method create_platform_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_platform_role`")  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/roles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1RoleBase',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_platform_permission(self, permission_name, **kwargs):  # noqa: E501
        """delete a platform perm policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_platform_permission(permission_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str permission_name: identifier of the permission (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_platform_permission_with_http_info(permission_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_platform_permission_with_http_info(permission_name, **kwargs)  # noqa: E501
            return data

    def delete_platform_permission_with_http_info(self, permission_name, **kwargs):  # noqa: E501
        """delete a platform perm policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_platform_permission_with_http_info(permission_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str permission_name: identifier of the permission (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_platform_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission_name' is set
        if ('permission_name' not in params or
                params['permission_name'] is None):
            raise ValueError("Missing the required parameter `permission_name` when calling `delete_platform_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'permission_name' in params:
            path_params['permissionName'] = params['permission_name']  # noqa: E501

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
            '/api/v1/permissions/{permissionName}', 'DELETE',
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

    def delete_platform_role(self, role_name, **kwargs):  # noqa: E501
        """update platform level role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_platform_role(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: identifier of the role (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_platform_role_with_http_info(role_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_platform_role_with_http_info(role_name, **kwargs)  # noqa: E501
            return data

    def delete_platform_role_with_http_info(self, role_name, **kwargs):  # noqa: E501
        """update platform level role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_platform_role_with_http_info(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: identifier of the role (required)
        :return: V1EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_platform_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params or
                params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `delete_platform_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_name' in params:
            path_params['roleName'] = params['role_name']  # noqa: E501

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
            '/api/v1/roles/{roleName}', 'DELETE',
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

    def list_platform_permissions(self, **kwargs):  # noqa: E501
        """list all platform level perm policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_platform_permissions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[V1PermissionBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_platform_permissions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_platform_permissions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_platform_permissions_with_http_info(self, **kwargs):  # noqa: E501
        """list all platform level perm policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_platform_permissions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[V1PermissionBase]
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
                    " to method list_platform_permissions" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/permissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[V1PermissionBase]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_platform_roles(self, **kwargs):  # noqa: E501
        """list all platform level roles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_platform_roles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListRolesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_platform_roles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_platform_roles_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_platform_roles_with_http_info(self, **kwargs):  # noqa: E501
        """list all platform level roles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_platform_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListRolesResponse
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
                    " to method list_platform_roles" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListRolesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_platform_role(self, body, role_name, **kwargs):  # noqa: E501
        """update platform level role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_platform_role(body, role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1UpdateRoleRequest body: (required)
        :param str role_name: identifier of the role (required)
        :return: V1RoleBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_platform_role_with_http_info(body, role_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_platform_role_with_http_info(body, role_name, **kwargs)  # noqa: E501
            return data

    def update_platform_role_with_http_info(self, body, role_name, **kwargs):  # noqa: E501
        """update platform level role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_platform_role_with_http_info(body, role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1UpdateRoleRequest body: (required)
        :param str role_name: identifier of the role (required)
        :return: V1RoleBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'role_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_platform_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_platform_role`")  # noqa: E501
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params or
                params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `update_platform_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_name' in params:
            path_params['roleName'] = params['role_name']  # noqa: E501

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
            '/api/v1/roles/{roleName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1RoleBase',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)