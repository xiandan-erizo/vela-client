# swagger_client.HelmApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chart_values**](HelmApi.md#chart_values) | **GET** /api/v1/repository/charts/{chart}/versions/{version}/values | get chart value
[**get_image_info**](HelmApi.md#get_image_info) | **GET** /api/v1/repository/image/info | get the oci repos
[**get_image_repos**](HelmApi.md#get_image_repos) | **GET** /api/v1/repository/image/repos | get the oci repos
[**list_charts**](HelmApi.md#list_charts) | **GET** /api/v1/repository/charts | list charts
[**list_repo**](HelmApi.md#list_repo) | **GET** /api/v1/repository/chart_repos | list chart repo
[**list_versions**](HelmApi.md#list_versions) | **GET** /api/v1/repository/charts/{chart}/versions | list versions

# **chart_values**
> MapStringinterface207B7D chart_values(repo_url=repo_url, secret_name=secret_name)

get chart value

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.HelmApi()
repo_url = 'repo_url_example'  # str | helm repository url (optional)
secret_name = 'secret_name_example'  # str | secret of the repo (optional)

try:
    # get chart value
    api_response = api_instance.chart_values(repo_url=repo_url, secret_name=secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->chart_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_url** | **str**| helm repository url | [optional] 
 **secret_name** | **str**| secret of the repo | [optional] 

### Return type

[**MapStringinterface207B7D**](MapStringinterface207B7D.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_info**
> V1ImageInfo get_image_info(project, name, secret_name=secret_name)

get the oci repos

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.HelmApi()
project = 'project_example'  # str | the config project
name = 'name_example'  # str | the image name
secret_name = 'secret_name_example'  # str | the secret name of the image repository (optional)

try:
    # get the oci repos
    api_response = api_instance.get_image_info(project, name, secret_name=secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->get_image_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| the config project | 
 **name** | **str**| the image name | 
 **secret_name** | **str**| the secret name of the image repository | [optional] 

### Return type

[**V1ImageInfo**](V1ImageInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_repos**
> V1ListImageRegistryResponse get_image_repos(project)

get the oci repos

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.HelmApi()
project = 'project_example'  # str | the config project

try:
    # get the oci repos
    api_response = api_instance.get_image_repos(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->get_image_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| the config project | 

### Return type

[**V1ListImageRegistryResponse**](V1ListImageRegistryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_charts**
> list[str] list_charts(repo_url=repo_url, secret_name=secret_name)

list charts

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.HelmApi()
repo_url = 'repo_url_example'  # str | helm repository url (optional)
secret_name = 'secret_name_example'  # str | secret of the repo (optional)

try:
    # list charts
    api_response = api_instance.list_charts(repo_url=repo_url, secret_name=secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->list_charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_url** | **str**| helm repository url | [optional] 
 **secret_name** | **str**| secret of the repo | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repo**
> list[str] list_repo(project)

list chart repo

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.HelmApi()
project = 'project_example'  # str | the config project

try:
    # list chart repo
    api_response = api_instance.list_repo(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->list_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| the config project | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> V1ChartVersionListResponse list_versions(repo_url=repo_url, secret_name=secret_name)

list versions

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.HelmApi()
repo_url = 'repo_url_example'  # str | helm repository url (optional)
secret_name = 'secret_name_example'  # str | secret of the repo (optional)

try:
    # list versions
    api_response = api_instance.list_versions(repo_url=repo_url, secret_name=secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->list_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_url** | **str**| helm repository url | [optional] 
 **secret_name** | **str**| secret of the repo | [optional] 

### Return type

[**V1ChartVersionListResponse**](V1ChartVersionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

