# swagger_client.SystemInfoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_info**](SystemInfoApi.md#get_system_info) | **GET** /api/v1/system_info | 
[**update_system_info**](SystemInfoApi.md#update_system_info) | **PUT** /api/v1/system_info | 

# **get_system_info**
> V1SystemInfoResponse get_system_info()



### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.SystemInfoApi()

try:
    api_response = api_instance.get_system_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInfoApi->get_system_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1SystemInfoResponse**](V1SystemInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_info**
> V1SystemInfoResponse update_system_info(body)



### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.SystemInfoApi()
body = vela_client.V1SystemInfoRequest()  # V1SystemInfoRequest | 

try:
    api_response = api_instance.update_system_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInfoApi->update_system_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SystemInfoRequest**](V1SystemInfoRequest.md)|  | 

### Return type

[**V1SystemInfoResponse**](V1SystemInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

