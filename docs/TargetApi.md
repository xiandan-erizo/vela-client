# swagger_client.TargetApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_target**](TargetApi.md#create_target) | **POST** /api/v1/targets | create Target
[**delete_target**](TargetApi.md#delete_target) | **DELETE** /api/v1/targets/{targetName} | deletet Target
[**detail_target**](TargetApi.md#detail_target) | **GET** /api/v1/targets/{targetName} | detail Target
[**list_targets**](TargetApi.md#list_targets) | **GET** /api/v1/targets | list Target
[**update_target**](TargetApi.md#update_target) | **PUT** /api/v1/targets/{targetName} | update application Target config

# **create_target**
> V1SimpleResponse create_target(body)

create Target

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.TargetApi()
body = vela_client.V1CreateTargetRequest()  # V1CreateTargetRequest | 

try:
    # create Target
    api_response = api_instance.create_target(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetApi->create_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateTargetRequest**](V1CreateTargetRequest.md)|  | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target**
> V1SimpleResponse delete_target(target_name)

deletet Target

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.TargetApi()
target_name = 'target_name_example'  # str | identifier of the Target

try:
    # deletet Target
    api_response = api_instance.delete_target(target_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetApi->delete_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_name** | **str**| identifier of the Target | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_target**
> V1SimpleResponse detail_target(target_name)

detail Target

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.TargetApi()
target_name = 'target_name_example'  # str | identifier of the Target.

try:
    # detail Target
    api_response = api_instance.detail_target(target_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetApi->detail_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_name** | **str**| identifier of the Target. | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_targets**
> V1SimpleResponse list_targets(page=page, page_size=page_size, project=project)

list Target

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.TargetApi()
page = 56  # int | Page for paging (optional)
page_size = 56  # int | PageSize for paging (optional)
project = 'project_example'  # str | list targets by project name (optional)

try:
    # list Target
    api_response = api_instance.list_targets(page=page, page_size=page_size, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetApi->list_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for paging | [optional] 
 **page_size** | **int**| PageSize for paging | [optional] 
 **project** | **str**| list targets by project name | [optional] 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target**
> V1SimpleResponse update_target(body, target_name)

update application Target config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.TargetApi()
body = vela_client.V1UpdateTargetRequest()  # V1UpdateTargetRequest | 
target_name = 'target_name_example'  # str | identifier of the Target

try:
    # update application Target config
    api_response = api_instance.update_target(body, target_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetApi->update_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateTargetRequest**](V1UpdateTargetRequest.md)|  | 
 **target_name** | **str**| identifier of the Target | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

