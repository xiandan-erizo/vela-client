# swagger_client.PayloadTypesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payload_types**](PayloadTypesApi.md#list_payload_types) | **GET** /api/v1/payload_types | list application trigger payload types

# **list_payload_types**
> list_payload_types()

list application trigger payload types

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PayloadTypesApi()

try:
    # list application trigger payload types
    api_instance.list_payload_types()
except ApiException as e:
    print("Exception when calling PayloadTypesApi->list_payload_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

