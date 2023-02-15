# swagger_client.VelaQLApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_view**](VelaQLApi.md#query_view) | **GET** /api/v1/query | use velaQL to query resource status

# **query_view**
> V1VelaQLViewResponse query_view(velaql=velaql)

use velaQL to query resource status

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.VelaQLApi()
velaql = 'velaql_example'  # str | velaql query statement (optional)

try:
    # use velaQL to query resource status
    api_response = api_instance.query_view(velaql=velaql)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VelaQLApi->query_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **velaql** | **str**| velaql query statement | [optional] 

### Return type

[**V1VelaQLViewResponse**](V1VelaQLViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

