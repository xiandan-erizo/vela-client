# swagger_client.OamApplicationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_application**](OamApplicationApi.md#create_or_update_application) | **POST** /v1/namespaces/{namespace}/applications/{appname} | create or update oam application in the specified namespace
[**delete_oam_application**](OamApplicationApi.md#delete_oam_application) | **DELETE** /v1/namespaces/{namespace}/applications/{appname} | create or update oam application in the specified namespace
[**get_application**](OamApplicationApi.md#get_application) | **GET** /v1/namespaces/{namespace}/applications/{appname} | get the specified oam application in the specified namespace

# **create_or_update_application**
> create_or_update_application(body, namespace, appname, dry_run=dry_run)

create or update oam application in the specified namespace

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.OamApplicationApi()
body = vela_client.V1ApplicationRequest()  # V1ApplicationRequest | 
namespace = 'namespace_example'  # str | identifier of the namespace
appname = 'appname_example'  # str | identifier of the oam application
dry_run = 'dry_run_example'  # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)

try:
    # create or update oam application in the specified namespace
    api_instance.create_or_update_application(body, namespace, appname, dry_run=dry_run)
except ApiException as e:
    print("Exception when calling OamApplicationApi->create_or_update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ApplicationRequest**](V1ApplicationRequest.md)|  | 
 **namespace** | **str**| identifier of the namespace | 
 **appname** | **str**| identifier of the oam application | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oam_application**
> delete_oam_application(namespace, appname)

create or update oam application in the specified namespace

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.OamApplicationApi()
namespace = 'namespace_example'  # str | identifier of the namespace
appname = 'appname_example'  # str | identifier of the oam application

try:
    # create or update oam application in the specified namespace
    api_instance.delete_oam_application(namespace, appname)
except ApiException as e:
    print("Exception when calling OamApplicationApi->delete_oam_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| identifier of the namespace | 
 **appname** | **str**| identifier of the oam application | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> V1ApplicationResponse get_application(namespace, appname)

get the specified oam application in the specified namespace

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.OamApplicationApi()
namespace = 'namespace_example'  # str | identifier of the namespace
appname = 'appname_example'  # str | identifier of the oam application

try:
    # get the specified oam application in the specified namespace
    api_response = api_instance.get_application(namespace, appname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OamApplicationApi->get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| identifier of the namespace | 
 **appname** | **str**| identifier of the oam application | 

### Return type

[**V1ApplicationResponse**](V1ApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

