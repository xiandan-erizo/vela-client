# swagger_client.AddonApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detail_addon**](AddonApi.md#detail_addon) | **GET** /api/v1/addons/{addonName} | show details of an addon
[**disable_addon**](AddonApi.md#disable_addon) | **POST** /api/v1/addons/{addonName}/disable | disable an addon
[**enable_addon**](AddonApi.md#enable_addon) | **POST** /api/v1/addons/{addonName}/enable | enable an addon
[**list**](AddonApi.md#list) | **GET** /api/v1/enabled_addon | list all enabled addons
[**list_addons**](AddonApi.md#list_addons) | **GET** /api/v1/addons | list all addons
[**status_addon**](AddonApi.md#status_addon) | **GET** /api/v1/addons/{addonName}/status | show status of an addon
[**update_addon**](AddonApi.md#update_addon) | **PUT** /api/v1/addons/{addonName}/update | update an addon

# **detail_addon**
> V1DetailAddonResponse detail_addon(name, addon_name, version=version, registry=registry)

show details of an addon

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonApi()
name = 'name_example'  # str | addon name to query detail
addon_name = 'addon_name_example'  # str | addon name to query detail
version = 'version_example'  # str | specify addon version to enable (optional)
registry = 'registry_example'  # str | filter addons from given registry (optional)

try:
    # show details of an addon
    api_response = api_instance.detail_addon(name, addon_name, version=version, registry=registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonApi->detail_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| addon name to query detail | 
 **addon_name** | **str**| addon name to query detail | 
 **version** | **str**| specify addon version to enable | [optional] 
 **registry** | **str**| filter addons from given registry | [optional] 

### Return type

[**V1DetailAddonResponse**](V1DetailAddonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **disable_addon**
> V1AddonStatusResponse disable_addon(addon_name, force=force)

disable an addon

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonApi()
addon_name = 'addon_name_example'  # str | addon name to enable
force = true  # bool | force disable an addon (optional)

try:
    # disable an addon
    api_response = api_instance.disable_addon(addon_name, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonApi->disable_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_name** | **str**| addon name to enable | 
 **force** | **bool**| force disable an addon | [optional] 

### Return type

[**V1AddonStatusResponse**](V1AddonStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **enable_addon**
> V1AddonStatusResponse enable_addon(body, addon_name)

enable an addon

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonApi()
body = vela_client.V1EnableAddonRequest()  # V1EnableAddonRequest | 
addon_name = 'addon_name_example'  # str | addon name to enable

try:
    # enable an addon
    api_response = api_instance.enable_addon(body, addon_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonApi->enable_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1EnableAddonRequest**](V1EnableAddonRequest.md)|  | 
 **addon_name** | **str**| addon name to enable | 

### Return type

[**V1AddonStatusResponse**](V1AddonStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list**
> V1ListEnabledAddonResponse list(registry=registry, query=query)

list all enabled addons

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonApi()
registry = 'registry_example'  # str | filter addons from given registry (optional)
query = 'query_example'  # str | Fuzzy search based on name and description. (optional)

try:
    # list all enabled addons
    api_response = api_instance.list(registry=registry, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**| filter addons from given registry | [optional] 
 **query** | **str**| Fuzzy search based on name and description. | [optional] 

### Return type

[**V1ListEnabledAddonResponse**](V1ListEnabledAddonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_addons**
> V1ListAddonResponse list_addons(registry=registry, query=query)

list all addons

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonApi()
registry = 'registry_example'  # str | filter addons from given registry (optional)
query = 'query_example'  # str | Fuzzy search based on name and description. (optional)

try:
    # list all addons
    api_response = api_instance.list_addons(registry=registry, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonApi->list_addons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**| filter addons from given registry | [optional] 
 **query** | **str**| Fuzzy search based on name and description. | [optional] 

### Return type

[**V1ListAddonResponse**](V1ListAddonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **status_addon**
> V1AddonStatusResponse status_addon(addon_name)

show status of an addon

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonApi()
addon_name = 'addon_name_example'  # str | addon name to query status

try:
    # show status of an addon
    api_response = api_instance.status_addon(addon_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonApi->status_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_name** | **str**| addon name to query status | 

### Return type

[**V1AddonStatusResponse**](V1AddonStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_addon**
> V1AddonStatusResponse update_addon(body, addon_name)

update an addon

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AddonApi()
body = vela_client.V1EnableAddonRequest()  # V1EnableAddonRequest | 
addon_name = 'addon_name_example'  # str | addon name to update

try:
    # update an addon
    api_response = api_instance.update_addon(body, addon_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonApi->update_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1EnableAddonRequest**](V1EnableAddonRequest.md)|  | 
 **addon_name** | **str**| addon name to update | 

### Return type

[**V1AddonStatusResponse**](V1AddonStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

