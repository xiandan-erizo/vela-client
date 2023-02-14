# swagger_client.ConfigApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config**](ConfigApi.md#create_config) | **POST** /api/v1/configs | create or update a config
[**delete_config**](ConfigApi.md#delete_config) | **DELETE** /api/v1/configs/{configName} | delete a config
[**get_config**](ConfigApi.md#get_config) | **GET** /api/v1/configs/{configName} | detail a config
[**get_config_template**](ConfigApi.md#get_config_template) | **GET** /api/v1/config_templates/{templateName} | Detail a template
[**get_configs**](ConfigApi.md#get_configs) | **GET** /api/v1/configs | list all configs that belong to the system scope
[**list_config_templates**](ConfigApi.md#list_config_templates) | **GET** /api/v1/config_templates | List all config templates from the system namespace
[**update_config**](ConfigApi.md#update_config) | **PUT** /api/v1/configs/{configName} | update a config

# **create_config**
> V1Config create_config(body)

create or update a config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ConfigApi()
body = vela_client.V1CreateConfigRequest()  # V1CreateConfigRequest | 

try:
    # create or update a config
    api_response = api_instance.create_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->create_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateConfigRequest**](V1CreateConfigRequest.md)|  | 

### Return type

[**V1Config**](V1Config.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config**
> V1EmptyResponse delete_config(config_name)

delete a config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ConfigApi()
config_name = 'config_name_example'  # str | identifier of the config

try:
    # delete a config
    api_response = api_instance.delete_config(config_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_name** | **str**| identifier of the config | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> list[V1Config] get_config(config_name)

detail a config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ConfigApi()
config_name = 'config_name_example'  # str | identifier of the config

try:
    # detail a config
    api_response = api_instance.get_config(config_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_name** | **str**| identifier of the config | 

### Return type

[**list[V1Config]**](V1Config.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_template**
> V1ConfigTemplateDetail get_config_template(template_name, namespace=namespace)

Detail a template

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ConfigApi()
template_name = 'template_name_example'  # str | identifier of the config template
namespace = 'namespace_example'  # str | the name of the namespace (optional)

try:
    # Detail a template
    api_response = api_instance.get_config_template(template_name, namespace=namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| identifier of the config template | 
 **namespace** | **str**| the name of the namespace | [optional] 

### Return type

[**V1ConfigTemplateDetail**](V1ConfigTemplateDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configs**
> V1ListConfigResponse get_configs(template=template)

list all configs that belong to the system scope

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ConfigApi()
template = 'template_example'  # str | the name of the template (optional)

try:
    # list all configs that belong to the system scope
    api_response = api_instance.get_configs(template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| the name of the template | [optional] 

### Return type

[**V1ListConfigResponse**](V1ListConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_templates**
> V1ListConfigTemplateResponse list_config_templates()

List all config templates from the system namespace

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ConfigApi()

try:
    # List all config templates from the system namespace
    api_response = api_instance.list_config_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_config_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1ListConfigTemplateResponse**](V1ListConfigTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config**
> list[V1UpdateConfigRequest] update_config(config_name)

update a config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ConfigApi()
config_name = 'config_name_example'  # str | identifier of the config

try:
    # update a config
    api_response = api_instance.update_config(config_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_name** | **str**| identifier of the config | 

### Return type

[**list[V1UpdateConfigRequest]**](V1UpdateConfigRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

