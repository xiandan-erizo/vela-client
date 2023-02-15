# swagger_client.ClusterApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_cloud_cluster**](ClusterApi.md#connect_cloud_cluster) | **POST** /api/v1/clusters/cloud_clusters/{provider}/connect | create cluster from cloud cluster
[**create_cloud_cluster**](ClusterApi.md#create_cloud_cluster) | **POST** /api/v1/clusters/cloud_clusters/{provider}/create | create cloud cluster
[**create_kube_cluster**](ClusterApi.md#create_kube_cluster) | **POST** /api/v1/clusters | create cluster
[**create_namespace**](ClusterApi.md#create_namespace) | **POST** /api/v1/clusters/{clusterName}/namespaces | create namespace in cluster
[**delete_cloud_cluster_creation**](ClusterApi.md#delete_cloud_cluster_creation) | **DELETE** /api/v1/clusters/cloud_clusters/{provider}/creation/{cloudClusterName} | delete cloud cluster creation
[**delete_kube_cluster**](ClusterApi.md#delete_kube_cluster) | **DELETE** /api/v1/clusters/{clusterName} | delete cluster
[**get_cloud_cluster_creation_status**](ClusterApi.md#get_cloud_cluster_creation_status) | **GET** /api/v1/clusters/cloud_clusters/{provider}/creation/{cloudClusterName} | check cloud cluster create status
[**get_kube_cluster**](ClusterApi.md#get_kube_cluster) | **GET** /api/v1/clusters/{clusterName} | detail cluster info
[**list_cloud_cluster_creation**](ClusterApi.md#list_cloud_cluster_creation) | **GET** /api/v1/clusters/cloud_clusters/{provider}/creation | list cloud cluster creation
[**list_cloud_clusters**](ClusterApi.md#list_cloud_clusters) | **POST** /api/v1/clusters/cloud_clusters/{provider} | list cloud clusters
[**list_kube_clusters**](ClusterApi.md#list_kube_clusters) | **GET** /api/v1/clusters | list all clusters
[**modify_kube_cluster**](ClusterApi.md#modify_kube_cluster) | **PUT** /api/v1/clusters/{clusterName} | modify cluster

# **connect_cloud_cluster**
> V1ClusterBase connect_cloud_cluster(body, provider)

create cluster from cloud cluster

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
body = vela_client.V1ConnectCloudClusterRequest()  # V1ConnectCloudClusterRequest | 
provider = 'provider_example'  # str | identifier of the cloud provider

try:
    # create cluster from cloud cluster
    api_response = api_instance.connect_cloud_cluster(body, provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->connect_cloud_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ConnectCloudClusterRequest**](V1ConnectCloudClusterRequest.md)|  | 
 **provider** | **str**| identifier of the cloud provider | 

### Return type

[**V1ClusterBase**](V1ClusterBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_cloud_cluster**
> V1CreateCloudClusterResponse create_cloud_cluster(body, provider)

create cloud cluster

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
body = vela_client.V1CreateCloudClusterRequest()  # V1CreateCloudClusterRequest | 
provider = 'provider_example'  # str | identifier of the cloud provider

try:
    # create cloud cluster
    api_response = api_instance.create_cloud_cluster(body, provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cloud_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateCloudClusterRequest**](V1CreateCloudClusterRequest.md)|  | 
 **provider** | **str**| identifier of the cloud provider | 

### Return type

[**V1CreateCloudClusterResponse**](V1CreateCloudClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_kube_cluster**
> V1ClusterBase create_kube_cluster(body)

create cluster

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
body = vela_client.V1CreateClusterRequest()  # V1CreateClusterRequest | 

try:
    # create cluster
    api_response = api_instance.create_kube_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_kube_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateClusterRequest**](V1CreateClusterRequest.md)|  | 

### Return type

[**V1ClusterBase**](V1ClusterBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_namespace**
> V1CreateClusterNamespaceResponse create_namespace(body, cluster_name)

create namespace in cluster

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
body = vela_client.V1CreateClusterNamespaceRequest()  # V1CreateClusterNamespaceRequest | 
cluster_name = 'cluster_name_example'  # str | name of the target cluster

try:
    # create namespace in cluster
    api_response = api_instance.create_namespace(body, cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateClusterNamespaceRequest**](V1CreateClusterNamespaceRequest.md)|  | 
 **cluster_name** | **str**| name of the target cluster | 

### Return type

[**V1CreateClusterNamespaceResponse**](V1CreateClusterNamespaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_cloud_cluster_creation**
> V1CreateCloudClusterResponse delete_cloud_cluster_creation(provider, cloud_cluster_name)

delete cloud cluster creation

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
provider = 'provider_example'  # str | identifier of the cloud provider
cloud_cluster_name = 'cloud_cluster_name_example'  # str | identifier for cloud cluster which is creating

try:
    # delete cloud cluster creation
    api_response = api_instance.delete_cloud_cluster_creation(provider, cloud_cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->delete_cloud_cluster_creation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| identifier of the cloud provider | 
 **cloud_cluster_name** | **str**| identifier for cloud cluster which is creating | 

### Return type

[**V1CreateCloudClusterResponse**](V1CreateCloudClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_kube_cluster**
> V1ClusterBase delete_kube_cluster(cluster_name)

delete cluster

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
cluster_name = 'cluster_name_example'  # str | identifier of the cluster

try:
    # delete cluster
    api_response = api_instance.delete_kube_cluster(cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->delete_kube_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| identifier of the cluster | 

### Return type

[**V1ClusterBase**](V1ClusterBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_cloud_cluster_creation_status**
> V1CreateCloudClusterResponse get_cloud_cluster_creation_status(provider, cloud_cluster_name)

check cloud cluster create status

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
provider = 'provider_example'  # str | identifier of the cloud provider
cloud_cluster_name = 'cloud_cluster_name_example'  # str | identifier for cloud cluster which is creating

try:
    # check cloud cluster create status
    api_response = api_instance.get_cloud_cluster_creation_status(provider, cloud_cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cloud_cluster_creation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| identifier of the cloud provider | 
 **cloud_cluster_name** | **str**| identifier for cloud cluster which is creating | 

### Return type

[**V1CreateCloudClusterResponse**](V1CreateCloudClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_kube_cluster**
> V1DetailClusterResponse get_kube_cluster(cluster_name)

detail cluster info

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
cluster_name = 'cluster_name_example'  # str | identifier of the cluster

try:
    # detail cluster info
    api_response = api_instance.get_kube_cluster(cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_kube_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| identifier of the cluster | 

### Return type

[**V1DetailClusterResponse**](V1DetailClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_cloud_cluster_creation**
> V1ListCloudClusterCreationResponse list_cloud_cluster_creation(provider)

list cloud cluster creation

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
provider = 'provider_example'  # str | identifier of the cloud provider

try:
    # list cloud cluster creation
    api_response = api_instance.list_cloud_cluster_creation(provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cloud_cluster_creation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| identifier of the cloud provider | 

### Return type

[**V1ListCloudClusterCreationResponse**](V1ListCloudClusterCreationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_cloud_clusters**
> V1ListCloudClusterResponse list_cloud_clusters(body, provider, page=page, page_size=page_size)

list cloud clusters

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
body = vela_client.V1AccessKeyRequest()  # V1AccessKeyRequest | 
provider = 'provider_example'  # str | identifier of the cloud provider
page = 0  # int | Page for paging (optional) (default to 0)
page_size = 20  # int | PageSize for paging (optional) (default to 20)

try:
    # list cloud clusters
    api_response = api_instance.list_cloud_clusters(body, provider, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cloud_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AccessKeyRequest**](V1AccessKeyRequest.md)|  | 
 **provider** | **str**| identifier of the cloud provider | 
 **page** | **int**| Page for paging | [optional] [default to 0]
 **page_size** | **int**| PageSize for paging | [optional] [default to 20]

### Return type

[**V1ListCloudClusterResponse**](V1ListCloudClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_kube_clusters**
> V1SimpleResponse list_kube_clusters(query=query, page=page, page_size=page_size)

list all clusters

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
query = 'query_example'  # str | Fuzzy search based on name or description (optional)
page = 0  # int | Page for paging (optional) (default to 0)
page_size = 20  # int | PageSize for paging (optional) (default to 20)

try:
    # list all clusters
    api_response = api_instance.list_kube_clusters(query=query, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_kube_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Fuzzy search based on name or description | [optional] 
 **page** | **int**| Page for paging | [optional] [default to 0]
 **page_size** | **int**| PageSize for paging | [optional] [default to 20]

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **modify_kube_cluster**
> V1ClusterBase modify_kube_cluster(body, cluster_name)

modify cluster

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ClusterApi()
body = vela_client.V1CreateClusterRequest()  # V1CreateClusterRequest | 
cluster_name = 'cluster_name_example'  # str | identifier of the cluster

try:
    # modify cluster
    api_response = api_instance.modify_kube_cluster(body, cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->modify_kube_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateClusterRequest**](V1CreateClusterRequest.md)|  | 
 **cluster_name** | **str**| identifier of the cluster | 

### Return type

[**V1ClusterBase**](V1ClusterBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

