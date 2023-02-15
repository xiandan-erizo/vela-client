# swagger_client.ProjectApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_distribution**](ProjectApi.md#apply_distribution) | **POST** /api/v1/projects/{projectName}/distributions | apply the distribution job of the config
[**create_config**](ProjectApi.md#create_config) | **POST** /api/v1/projects/{projectName}/configs | create a config in a project
[**create_project**](ProjectApi.md#create_project) | **POST** /api/v1/projects | create a project
[**create_project_permission**](ProjectApi.md#create_project_permission) | **POST** /api/v1/projects/{projectName}/permissions | create a project level perm policy
[**create_project_role**](ProjectApi.md#create_project_role) | **POST** /api/v1/projects/{projectName}/roles | create project level role
[**create_project_user**](ProjectApi.md#create_project_user) | **POST** /api/v1/projects/{projectName}/users | add a user to a project
[**delete_config**](ProjectApi.md#delete_config) | **DELETE** /api/v1/projects/{projectName}/configs/{configName} | delete a config from a project
[**delete_distribution**](ProjectApi.md#delete_distribution) | **DELETE** /api/v1/projects/{projectName}/distributions/{distributionName} | delete a distribution job of the config
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /api/v1/projects/{projectName} | delete a project
[**delete_project_permission**](ProjectApi.md#delete_project_permission) | **DELETE** /api/v1/projects/{projectName}/permissions/{permissionName} | delete a project level perm policy
[**delete_project_role**](ProjectApi.md#delete_project_role) | **DELETE** /api/v1/projects/{projectName}/roles/{roleName} | delete project level role
[**delete_project_user**](ProjectApi.md#delete_project_user) | **DELETE** /api/v1/projects/{projectName}/users/{userName} | delete a user from a project
[**detail_config**](ProjectApi.md#detail_config) | **GET** /api/v1/projects/{projectName}/configs/{configName} | detail a config in a project
[**detail_project**](ProjectApi.md#detail_project) | **GET** /api/v1/projects/{projectName} | detail a project
[**get_config_template**](ProjectApi.md#get_config_template) | **GET** /api/v1/projects/{projectName}/config_templates/{templateName} | Detail a template
[**get_config_templates**](ProjectApi.md#get_config_templates) | **GET** /api/v1/projects/{projectName}/config_templates | get the templates which are in a project
[**get_configs**](ProjectApi.md#get_configs) | **GET** /api/v1/projects/{projectName}/configs | get configs which are in a project
[**get_providers**](ProjectApi.md#get_providers) | **GET** /api/v1/projects/{projectName}/providers | get providers which are in a project
[**list_distributions**](ProjectApi.md#list_distributions) | **GET** /api/v1/projects/{projectName}/distributions | list the distribution jobs of the config
[**list_project_permissions**](ProjectApi.md#list_project_permissions) | **GET** /api/v1/projects/{projectName}/permissions | list all project level perm policies
[**list_project_roles**](ProjectApi.md#list_project_roles) | **GET** /api/v1/projects/{projectName}/roles | list all project level roles
[**list_project_targets**](ProjectApi.md#list_project_targets) | **GET** /api/v1/projects/{projectName}/targets | get targets list belong to a project
[**list_project_user**](ProjectApi.md#list_project_user) | **GET** /api/v1/projects/{projectName}/users | list all users belong to a project
[**list_projects**](ProjectApi.md#list_projects) | **GET** /api/v1/projects | list all projects
[**update_config**](ProjectApi.md#update_config) | **PUT** /api/v1/projects/{projectName}/configs/{configName} | update a config in a project
[**update_project**](ProjectApi.md#update_project) | **PUT** /api/v1/projects/{projectName} | update a project
[**update_project_role**](ProjectApi.md#update_project_role) | **PUT** /api/v1/projects/{projectName}/roles/{roleName} | update project level role
[**update_project_user**](ProjectApi.md#update_project_user) | **PUT** /api/v1/projects/{projectName}/users/{userName} | update a user from a project

# **apply_distribution**
> V1EmptyResponse apply_distribution(body, project_name)

apply the distribution job of the config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1CreateConfigDistributionRequest()  # V1CreateConfigDistributionRequest | 
project_name = 'project_name_example'  # str | identifier of the project

try:
    # apply the distribution job of the config
    api_response = api_instance.apply_distribution(body, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->apply_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateConfigDistributionRequest**](V1CreateConfigDistributionRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_config**
> V1Config create_config(body, project_name)

create a config in a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1CreateConfigRequest()  # V1CreateConfigRequest | 
project_name = 'project_name_example'  # str | identifier of the project

try:
    # create a config in a project
    api_response = api_instance.create_config(body, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateConfigRequest**](V1CreateConfigRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1Config**](V1Config.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_project**
> V1ProjectBase create_project(body)

create a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1CreateProjectRequest()  # V1CreateProjectRequest | 

try:
    # create a project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateProjectRequest**](V1CreateProjectRequest.md)|  | 

### Return type

[**V1ProjectBase**](V1ProjectBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_project_permission**
> list[V1PermissionBase] create_project_permission(project_name)

create a project level perm policy

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # create a project level perm policy
    api_response = api_instance.create_project_permission(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**list[V1PermissionBase]**](V1PermissionBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_project_role**
> V1RoleBase create_project_role(body, project_name)

create project level role

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1CreateRoleRequest()  # V1CreateRoleRequest | 
project_name = 'project_name_example'  # str | identifier of the project

try:
    # create project level role
    api_response = api_instance.create_project_role(body, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateRoleRequest**](V1CreateRoleRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1RoleBase**](V1RoleBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_project_user**
> V1ProjectUserBase create_project_user(body, project_name)

add a user to a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1AddProjectUserRequest()  # V1AddProjectUserRequest | 
project_name = 'project_name_example'  # str | identifier of the project

try:
    # add a user to a project
    api_response = api_instance.create_project_user(body, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AddProjectUserRequest**](V1AddProjectUserRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1ProjectUserBase**](V1ProjectUserBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_config**
> V1EmptyResponse delete_config(project_name, config_name)

delete a config from a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project
config_name = 'config_name_example'  # str | identifier of the config

try:
    # delete a config from a project
    api_response = api_instance.delete_config(project_name, config_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 
 **config_name** | **str**| identifier of the config | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_distribution**
> V1EmptyResponse delete_distribution(project_name, distribution_name)

delete a distribution job of the config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project
distribution_name = 'distribution_name_example'  # str | identifier of the distribution

try:
    # delete a distribution job of the config
    api_response = api_instance.delete_distribution(project_name, distribution_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 
 **distribution_name** | **str**| identifier of the distribution | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_project**
> V1EmptyResponse delete_project(project_name)

delete a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # delete a project
    api_response = api_instance.delete_project(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_project_permission**
> list[V1PermissionBase] delete_project_permission(project_name, permission_name)

delete a project level perm policy

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project
permission_name = 'permission_name_example'  # str | identifier of the permission

try:
    # delete a project level perm policy
    api_response = api_instance.delete_project_permission(project_name, permission_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 
 **permission_name** | **str**| identifier of the permission | 

### Return type

[**list[V1PermissionBase]**](V1PermissionBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_project_role**
> V1EmptyResponse delete_project_role(project_name, role_name)

delete project level role

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project
role_name = 'role_name_example'  # str | identifier of the project role

try:
    # delete project level role
    api_response = api_instance.delete_project_role(project_name, role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 
 **role_name** | **str**| identifier of the project role | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_project_user**
> V1EmptyResponse delete_project_user(body, project_name, user_name)

delete a user from a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1UpdateProjectUserRequest()  # V1UpdateProjectUserRequest | 
project_name = 'project_name_example'  # str | identifier of the project
user_name = 'user_name_example'  # str | identifier of the project user

try:
    # delete a user from a project
    api_response = api_instance.delete_project_user(body, project_name, user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateProjectUserRequest**](V1UpdateProjectUserRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 
 **user_name** | **str**| identifier of the project user | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_config**
> V1Config detail_config(body, project_name, config_name)

detail a config in a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1UpdateConfigRequest()  # V1UpdateConfigRequest | 
project_name = 'project_name_example'  # str | identifier of the project
config_name = 'config_name_example'  # str | identifier of the config

try:
    # detail a config in a project
    api_response = api_instance.detail_config(body, project_name, config_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->detail_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateConfigRequest**](V1UpdateConfigRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 
 **config_name** | **str**| identifier of the config | 

### Return type

[**V1Config**](V1Config.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_project**
> V1ProjectBase detail_project(project_name)

detail a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # detail a project
    api_response = api_instance.detail_project(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->detail_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1ProjectBase**](V1ProjectBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_config_template**
> V1ConfigTemplateDetail get_config_template(template_name, namespace=namespace)

Detail a template

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
template_name = 'template_name_example'  # str | identifier of the config template
namespace = 'namespace_example'  # str | the name of the namespace (optional)

try:
    # Detail a template
    api_response = api_instance.get_config_template(template_name, namespace=namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_config_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| identifier of the config template | 
 **namespace** | **str**| the name of the namespace | [optional] 

### Return type

[**V1ConfigTemplateDetail**](V1ConfigTemplateDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_config_templates**
> V1ListConfigTemplateResponse get_config_templates(project_name, namespace)

get the templates which are in a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project
namespace = 'namespace_example'  # str | the namespace of the template

try:
    # get the templates which are in a project
    api_response = api_instance.get_config_templates(project_name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_config_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 
 **namespace** | **str**| the namespace of the template | 

### Return type

[**V1ListConfigTemplateResponse**](V1ListConfigTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_configs**
> V1ListConfigResponse get_configs(project_name, template=template)

get configs which are in a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project
template = 'template_example'  # str | the template name (optional)

try:
    # get configs which are in a project
    api_response = api_instance.get_configs(project_name, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 
 **template** | **str**| the template name | [optional] 

### Return type

[**V1ListConfigResponse**](V1ListConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_providers**
> V1ListTerraformProviderResponse get_providers(project_name)

get providers which are in a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # get providers which are in a project
    api_response = api_instance.get_providers(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1ListTerraformProviderResponse**](V1ListTerraformProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_distributions**
> V1ListConfigDistributionResponse list_distributions(project_name)

list the distribution jobs of the config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # list the distribution jobs of the config
    api_response = api_instance.list_distributions(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1ListConfigDistributionResponse**](V1ListConfigDistributionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_project_permissions**
> list[V1PermissionBase] list_project_permissions(project_name)

list all project level perm policies

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # list all project level perm policies
    api_response = api_instance.list_project_permissions(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_project_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**list[V1PermissionBase]**](V1PermissionBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_project_roles**
> V1ListRolesResponse list_project_roles(project_name)

list all project level roles

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # list all project level roles
    api_response = api_instance.list_project_roles(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_project_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1ListRolesResponse**](V1ListRolesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_project_targets**
> V1EmptyResponse list_project_targets(project_name)

get targets list belong to a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # get targets list belong to a project
    api_response = api_instance.list_project_targets(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_project_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_project_user**
> V1ListProjectUsersResponse list_project_user(project_name)

list all users belong to a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
project_name = 'project_name_example'  # str | identifier of the project

try:
    # list all users belong to a project
    api_response = api_instance.list_project_user(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1ListProjectUsersResponse**](V1ListProjectUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_projects**
> V1ListProjectResponse list_projects()

list all projects

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()

try:
    # list all projects
    api_response = api_instance.list_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1ListProjectResponse**](V1ListProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_config**
> V1Config update_config(body, project_name, config_name)

update a config in a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1UpdateConfigRequest()  # V1UpdateConfigRequest | 
project_name = 'project_name_example'  # str | identifier of the project
config_name = 'config_name_example'  # str | identifier of the config

try:
    # update a config in a project
    api_response = api_instance.update_config(body, project_name, config_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateConfigRequest**](V1UpdateConfigRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 
 **config_name** | **str**| identifier of the config | 

### Return type

[**V1Config**](V1Config.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_project**
> V1ProjectBase update_project(body, project_name)

update a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1UpdateProjectRequest()  # V1UpdateProjectRequest | 
project_name = 'project_name_example'  # str | identifier of the project

try:
    # update a project
    api_response = api_instance.update_project(body, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateProjectRequest**](V1UpdateProjectRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 

### Return type

[**V1ProjectBase**](V1ProjectBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_project_role**
> V1RoleBase update_project_role(body, project_name, role_name)

update project level role

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1UpdateRoleRequest()  # V1UpdateRoleRequest | 
project_name = 'project_name_example'  # str | identifier of the project
role_name = 'role_name_example'  # str | identifier of the project role

try:
    # update project level role
    api_response = api_instance.update_project_role(body, project_name, role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateRoleRequest**](V1UpdateRoleRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 
 **role_name** | **str**| identifier of the project role | 

### Return type

[**V1RoleBase**](V1RoleBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_project_user**
> V1ProjectUserBase update_project_user(body, project_name, user_name)

update a user from a project

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ProjectApi()
body = vela_client.V1UpdateProjectUserRequest()  # V1UpdateProjectUserRequest | 
project_name = 'project_name_example'  # str | identifier of the project
user_name = 'user_name_example'  # str | identifier of the project user

try:
    # update a user from a project
    api_response = api_instance.update_project_user(body, project_name, user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateProjectUserRequest**](V1UpdateProjectUserRequest.md)|  | 
 **project_name** | **str**| identifier of the project | 
 **user_name** | **str**| identifier of the project user | 

### Return type

[**V1ProjectUserBase**](V1ProjectUserBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

