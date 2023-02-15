# swagger_client.RbacApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_platform_permission**](RbacApi.md#create_platform_permission) | **POST** /api/v1/permissions | create the platform perm policy
[**create_platform_role**](RbacApi.md#create_platform_role) | **POST** /api/v1/roles | create platform level role
[**delete_platform_permission**](RbacApi.md#delete_platform_permission) | **DELETE** /api/v1/permissions/{permissionName} | delete a platform perm policy
[**delete_platform_role**](RbacApi.md#delete_platform_role) | **DELETE** /api/v1/roles/{roleName} | update platform level role
[**list_platform_permissions**](RbacApi.md#list_platform_permissions) | **GET** /api/v1/permissions | list all platform level perm policies
[**list_platform_roles**](RbacApi.md#list_platform_roles) | **GET** /api/v1/roles | list all platform level roles
[**update_platform_role**](RbacApi.md#update_platform_role) | **PUT** /api/v1/roles/{roleName} | update platform level role

# **create_platform_permission**
> V1PermissionBase create_platform_permission(body)

create the platform perm policy

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.RbacApi()
body = vela_client.V1CreatePermissionRequest()  # V1CreatePermissionRequest | 

try:
    # create the platform perm policy
    api_response = api_instance.create_platform_permission(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacApi->create_platform_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreatePermissionRequest**](V1CreatePermissionRequest.md)|  | 

### Return type

[**V1PermissionBase**](V1PermissionBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_platform_role**
> V1RoleBase create_platform_role(body)

create platform level role

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.RbacApi()
body = vela_client.V1CreateRoleRequest()  # V1CreateRoleRequest | 

try:
    # create platform level role
    api_response = api_instance.create_platform_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacApi->create_platform_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateRoleRequest**](V1CreateRoleRequest.md)|  | 

### Return type

[**V1RoleBase**](V1RoleBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_platform_permission**
> V1EmptyResponse delete_platform_permission(permission_name)

delete a platform perm policy

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.RbacApi()
permission_name = 'permission_name_example'  # str | identifier of the permission

try:
    # delete a platform perm policy
    api_response = api_instance.delete_platform_permission(permission_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacApi->delete_platform_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_name** | **str**| identifier of the permission | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_platform_role**
> V1EmptyResponse delete_platform_role(role_name)

update platform level role

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.RbacApi()
role_name = 'role_name_example'  # str | identifier of the role

try:
    # update platform level role
    api_response = api_instance.delete_platform_role(role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacApi->delete_platform_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| identifier of the role | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_platform_permissions**
> list[V1PermissionBase] list_platform_permissions()

list all platform level perm policies

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.RbacApi()

try:
    # list all platform level perm policies
    api_response = api_instance.list_platform_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacApi->list_platform_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1PermissionBase]**](V1PermissionBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_platform_roles**
> V1ListRolesResponse list_platform_roles()

list all platform level roles

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.RbacApi()

try:
    # list all platform level roles
    api_response = api_instance.list_platform_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacApi->list_platform_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1ListRolesResponse**](V1ListRolesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_platform_role**
> V1RoleBase update_platform_role(body, role_name)

update platform level role

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.RbacApi()
body = vela_client.V1UpdateRoleRequest()  # V1UpdateRoleRequest | 
role_name = 'role_name_example'  # str | identifier of the role

try:
    # update platform level role
    api_response = api_instance.update_platform_role(body, role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacApi->update_platform_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateRoleRequest**](V1UpdateRoleRequest.md)|  | 
 **role_name** | **str**| identifier of the role | 

### Return type

[**V1RoleBase**](V1RoleBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

