# swagger_client.AddonRegistryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon_registry**](AddonRegistryApi.md#create_addon_registry) | **POST** /api/v1/addon_registries | create an addon registry
[**delete_addon_registry**](AddonRegistryApi.md#delete_addon_registry) | **DELETE** /api/v1/addon_registries/{addonRegName} | delete an addon registry
[**list_addon_registry**](AddonRegistryApi.md#list_addon_registry) | **GET** /api/v1/addon_registries | list all addon registry
[**update_addon_registry**](AddonRegistryApi.md#update_addon_registry) | **PUT** /api/v1/addon_registries/{addonRegName} | update an addon registry

# **create_addon_registry**
> V1AddonRegistry create_addon_registry(body)

create an addon registry

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonRegistryApi()
body = vela_client.V1CreateAddonRegistryRequest()  # V1CreateAddonRegistryRequest | 

try:
    # create an addon registry
    api_response = api_instance.create_addon_registry(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonRegistryApi->create_addon_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateAddonRegistryRequest**](V1CreateAddonRegistryRequest.md)|  | 

### Return type

[**V1AddonRegistry**](V1AddonRegistry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_addon_registry**
> V1AddonRegistry delete_addon_registry(addon_reg_name)

delete an addon registry

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonRegistryApi()
addon_reg_name = 'addon_reg_name_example'  # str | identifier of the addon registry

try:
    # delete an addon registry
    api_response = api_instance.delete_addon_registry(addon_reg_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonRegistryApi->delete_addon_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_reg_name** | **str**| identifier of the addon registry | 

### Return type

[**V1AddonRegistry**](V1AddonRegistry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_addon_registry**
> V1ListAddonRegistryResponse list_addon_registry()

list all addon registry

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonRegistryApi()

try:
    # list all addon registry
    api_response = api_instance.list_addon_registry()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonRegistryApi->list_addon_registry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1ListAddonRegistryResponse**](V1ListAddonRegistryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_addon_registry**
> V1AddonRegistry update_addon_registry(body, addon_reg_name)

update an addon registry

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonRegistryApi()
body = vela_client.V1UpdateAddonRegistryRequest()  # V1UpdateAddonRegistryRequest | 
addon_reg_name = 'addon_reg_name_example'  # str | identifier of the addon registry

try:
    # update an addon registry
    api_response = api_instance.update_addon_registry(body, addon_reg_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonRegistryApi->update_addon_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateAddonRegistryRequest**](V1UpdateAddonRegistryRequest.md)|  | 
 **addon_reg_name** | **str**| identifier of the addon registry | 

### Return type

[**V1AddonRegistry**](V1AddonRegistry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

