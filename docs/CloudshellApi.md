# swagger_client.CloudshellApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destroy_cloud_shell**](CloudshellApi.md#destroy_cloud_shell) | **DELETE** /api/v1/cloudshell | destroy the user&#x27;s cloud shell environment
[**prepare_cloud_shell**](CloudshellApi.md#prepare_cloud_shell) | **POST** /api/v1/cloudshell | prepare the user&#x27;s cloud shell environment
[**proxy**](CloudshellApi.md#proxy) | **GET** /view/cloudshell | prepare the user&#x27;s cloud shell environment
[**proxy_0**](CloudshellApi.md#proxy_0) | **GET** /view/cloudshell/{subpath} | prepare the user&#x27;s cloud shell environment

# **destroy_cloud_shell**
> V1SimpleResponse destroy_cloud_shell()

destroy the user's cloud shell environment

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.CloudshellApi()

try:
    # destroy the user's cloud shell environment
    api_response = api_instance.destroy_cloud_shell()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudshellApi->destroy_cloud_shell: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_cloud_shell**
> V1SimpleResponse prepare_cloud_shell()

prepare the user's cloud shell environment

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.CloudshellApi()

try:
    # prepare the user's cloud shell environment
    api_response = api_instance.prepare_cloud_shell()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudshellApi->prepare_cloud_shell: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy**
> V1SimpleResponse proxy()

prepare the user's cloud shell environment

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.CloudshellApi()

try:
    # prepare the user's cloud shell environment
    api_response = api_instance.proxy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudshellApi->proxy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_0**
> V1SimpleResponse proxy_0()

prepare the user's cloud shell environment

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.CloudshellApi()

try:
    # prepare the user's cloud shell environment
    api_response = api_instance.proxy_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudshellApi->proxy_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

