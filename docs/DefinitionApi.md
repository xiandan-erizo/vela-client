# swagger_client.DefinitionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detail_definition**](DefinitionApi.md#detail_definition) | **GET** /api/v1/definitions/{definitionName} | Detail a definition
[**list_definitions**](DefinitionApi.md#list_definitions) | **GET** /api/v1/definitions | list all definitions
[**update_definition_status**](DefinitionApi.md#update_definition_status) | **PUT** /api/v1/definitions/{definitionName}/status | Update the status for a definition
[**update_ui_schema**](DefinitionApi.md#update_ui_schema) | **PUT** /api/v1/definitions/{definitionName}/uischema | Update the UI schema for a definition

# **detail_definition**
> V1SimpleResponse detail_definition(definition_name, type=type)

Detail a definition

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.DefinitionApi()
definition_name = 'definition_name_example'  # str | identifier of the definition
type = 'type_example'  # str | query the definition type (optional)

try:
    # Detail a definition
    api_response = api_instance.detail_definition(definition_name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionApi->detail_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_name** | **str**| identifier of the definition | 
 **type** | **str**| query the definition type | [optional] 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_definitions**
> V1SimpleResponse list_definitions(type, query_all=query_all, applied_workload=applied_workload, owner_addon=owner_addon, scope=scope)

list all definitions

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.DefinitionApi()
type = 'type_example'  # str | query the definition type
query_all = false  # bool | query all definitions include hidden in UI (optional) (default to false)
applied_workload = 'applied_workload_example'  # str | if specified, query the trait definition applied to the workload (optional)
owner_addon = 'owner_addon_example'  # str | query by which addon created the definition (optional)
scope = 'scope_example'  # str | query by the specified scope like WorkflowRun or Application (optional)

try:
    # list all definitions
    api_response = api_instance.list_definitions(type, query_all=query_all, applied_workload=applied_workload,
                                                 owner_addon=owner_addon, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionApi->list_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| query the definition type | 
 **query_all** | **bool**| query all definitions include hidden in UI | [optional] [default to false]
 **applied_workload** | **str**| if specified, query the trait definition applied to the workload | [optional] 
 **owner_addon** | **str**| query by which addon created the definition | [optional] 
 **scope** | **str**| query by the specified scope like WorkflowRun or Application | [optional] 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_definition_status**
> V1SimpleResponse update_definition_status(body)

Update the status for a definition

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.DefinitionApi()
body = vela_client.V1UpdateDefinitionStatusRequest()  # V1UpdateDefinitionStatusRequest | 

try:
    # Update the status for a definition
    api_response = api_instance.update_definition_status(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionApi->update_definition_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateDefinitionStatusRequest**](V1UpdateDefinitionStatusRequest.md)|  | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_ui_schema**
> V1SimpleResponse update_ui_schema(body)

Update the UI schema for a definition

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.DefinitionApi()
body = vela_client.V1UpdateUISchemaRequest()  # V1UpdateUISchemaRequest | 

try:
    # Update the UI schema for a definition
    api_response = api_instance.update_ui_schema(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionApi->update_ui_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateUISchemaRequest**](V1UpdateUISchemaRequest.md)|  | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

