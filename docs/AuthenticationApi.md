# swagger_client.AuthenticationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dex_config**](AuthenticationApi.md#get_dex_config) | **GET** /api/v1/auth/dex_config | get Dex config
[**get_login_type**](AuthenticationApi.md#get_login_type) | **GET** /api/v1/auth/login_type | get login type
[**get_login_user_info**](AuthenticationApi.md#get_login_user_info) | **GET** /api/v1/auth/user_info | get login user detail info
[**login**](AuthenticationApi.md#login) | **POST** /api/v1/auth/login | handle login request
[**refresh_token**](AuthenticationApi.md#refresh_token) | **GET** /api/v1/auth/refresh_token | refresh token

# **get_dex_config**
> V1DexConfigResponse get_dex_config()

get Dex config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AuthenticationApi()

try:
    # get Dex config
    api_response = api_instance.get_dex_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_dex_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1DexConfigResponse**](V1DexConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_type**
> V1GetLoginTypeResponse get_login_type()

get login type

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AuthenticationApi()

try:
    # get login type
    api_response = api_instance.get_login_type()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_login_type: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1GetLoginTypeResponse**](V1GetLoginTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_user_info**
> V1LoginUserInfoResponse get_login_user_info()

get login user detail info

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AuthenticationApi()

try:
    # get login user detail info
    api_response = api_instance.get_login_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_login_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1LoginUserInfoResponse**](V1LoginUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> V1LoginResponse login(body)

handle login request

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AuthenticationApi()
body = vela_client.V1LoginRequest()  # V1LoginRequest | 

try:
    # handle login request
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LoginRequest**](V1LoginRequest.md)|  | 

### Return type

[**V1LoginResponse**](V1LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> V1RefreshTokenResponse refresh_token()

refresh token

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.AuthenticationApi()

try:
    # refresh token
    api_response = api_instance.refresh_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->refresh_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1RefreshTokenResponse**](V1RefreshTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

