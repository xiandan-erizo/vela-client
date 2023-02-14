# swagger_client.EnvApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**envcreate**](EnvApi.md#envcreate) | **POST** /api/v1/envs | create an env
[**envdelete**](EnvApi.md#envdelete) | **DELETE** /api/v1/envs/{envName} | delete one env
[**envlist**](EnvApi.md#envlist) | **GET** /api/v1/envs | list all envs
[**envupdate**](EnvApi.md#envupdate) | **PUT** /api/v1/envs/{envName} | update an env

# **envcreate**
> V1Env envcreate(body)

create an env

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.EnvApi()
body = vela_client.V1CreateEnvRequest()  # V1CreateEnvRequest | 

try:
    # create an env
    api_response = api_instance.envcreate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvApi->envcreate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateEnvRequest**](V1CreateEnvRequest.md)|  | 

### Return type

[**V1Env**](V1Env.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **envdelete**
> V1EmptyResponse envdelete(env_name)

delete one env

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.EnvApi()
env_name = 'env_name_example'  # str | identifier of the environment

try:
    # delete one env
    api_response = api_instance.envdelete(env_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvApi->envdelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_name** | **str**| identifier of the environment | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **envlist**
> V1ListEnvResponse envlist()

list all envs

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.EnvApi()

try:
    # list all envs
    api_response = api_instance.envlist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvApi->envlist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1ListEnvResponse**](V1ListEnvResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **envupdate**
> V1Env envupdate(body, env_name)

update an env

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.EnvApi()
body = vela_client.V1CreateEnvRequest()  # V1CreateEnvRequest | 
env_name = 'env_name_example'  # str | identifier of the environment

try:
    # update an env
    api_response = api_instance.envupdate(body, env_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvApi->envupdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateEnvRequest**](V1CreateEnvRequest.md)|  | 
 **env_name** | **str**| identifier of the environment | 

### Return type

[**V1Env**](V1Env.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

