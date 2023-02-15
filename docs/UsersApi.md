# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /api/v1/users | create a user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /api/v1/users/{username} | delete a user
[**detail_user**](UsersApi.md#detail_user) | **GET** /api/v1/users/{username} | get user detail
[**disable_user**](UsersApi.md#disable_user) | **GET** /api/v1/users/{username}/disable | disable a user
[**enable_user**](UsersApi.md#enable_user) | **GET** /api/v1/users/{username}/enable | enable a user
[**list_user**](UsersApi.md#list_user) | **GET** /api/v1/users | list users
[**update_user**](UsersApi.md#update_user) | **PUT** /api/v1/users/{username} | update a user&#x27;s alias or password

# **create_user**
> V1UserBase create_user(body)

create a user

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.UsersApi()
body = vela_client.V1CreateUserRequest()  # V1CreateUserRequest | 

try:
    # create a user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateUserRequest**](V1CreateUserRequest.md)|  | 

### Return type

[**V1UserBase**](V1UserBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_user**
> V1EmptyResponse delete_user()

delete a user

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.UsersApi()

try:
    # delete a user
    api_response = api_instance.delete_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_user**
> V1DetailUserResponse detail_user()

get user detail

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.UsersApi()

try:
    # get user detail
    api_response = api_instance.detail_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->detail_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1DetailUserResponse**](V1DetailUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **disable_user**
> V1EmptyResponse disable_user()

disable a user

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.UsersApi()

try:
    # disable a user
    api_response = api_instance.disable_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->disable_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **enable_user**
> V1EmptyResponse enable_user()

enable a user

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.UsersApi()

try:
    # enable a user
    api_response = api_instance.enable_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->enable_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_user**
> V1ListUserResponse list_user(page=page, page_size=page_size, name=name, email=email, alias=alias)

list users

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.UsersApi()
page = 56  # int | query the page number (optional)
page_size = 56  # int | query the page size number (optional)
name = 'name_example'  # str | fuzzy search based on name (optional)
email = 'email_example'  # str | fuzzy search based on email (optional)
alias = 'alias_example'  # str | fuzzy search based on alias (optional)

try:
    # list users
    api_response = api_instance.list_user(page=page, page_size=page_size, name=name, email=email, alias=alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| query the page number | [optional] 
 **page_size** | **int**| query the page size number | [optional] 
 **name** | **str**| fuzzy search based on name | [optional] 
 **email** | **str**| fuzzy search based on email | [optional] 
 **alias** | **str**| fuzzy search based on alias | [optional] 

### Return type

[**V1ListUserResponse**](V1ListUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_user**
> V1UserBase update_user(body)

update a user's alias or password

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.UsersApi()
body = vela_client.V1UpdateUserRequest()  # V1UpdateUserRequest | 

try:
    # update a user's alias or password
    api_response = api_instance.update_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateUserRequest**](V1UpdateUserRequest.md)|  | 

### Return type

[**V1UserBase**](V1UserBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

