# swagger_client.PipelineApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_context_value**](PipelineApi.md#create_context_value) | **POST** /api/v1/projects/{projectName}/pipelines/{pipelineName}/contexts | create pipeline context values
[**create_pipeline**](PipelineApi.md#create_pipeline) | **POST** /api/v1/projects/{projectName}/pipelines | create pipeline
[**delete_context_value**](PipelineApi.md#delete_context_value) | **DELETE** /api/v1/projects/{projectName}/pipelines/{pipelineName}/contexts/{contextName} | delete pipeline context value
[**delete_pipeline**](PipelineApi.md#delete_pipeline) | **DELETE** /api/v1/projects/{projectName}/pipelines/{pipelineName} | delete pipeline
[**delete_pipeline_run**](PipelineApi.md#delete_pipeline_run) | **DELETE** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs/{runName} | delete pipeline run
[**get_pipeline**](PipelineApi.md#get_pipeline) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName} | get pipeline
[**get_pipeline_run**](PipelineApi.md#get_pipeline_run) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs/{runName} | get pipeline run
[**get_pipeline_run_input**](PipelineApi.md#get_pipeline_run_input) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs/{runName}/input | get pipeline run input
[**get_pipeline_run_log**](PipelineApi.md#get_pipeline_run_log) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs/{runName}/log | get pipeline run log
[**get_pipeline_run_output**](PipelineApi.md#get_pipeline_run_output) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs/{runName}/output | get pipeline run output
[**get_pipeline_run_status**](PipelineApi.md#get_pipeline_run_status) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs/{runName}/status | get pipeline run status
[**list_context_values**](PipelineApi.md#list_context_values) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName}/contexts | list pipeline context values
[**list_pipeline_runs**](PipelineApi.md#list_pipeline_runs) | **GET** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs | list pipeline runs
[**list_pipelines**](PipelineApi.md#list_pipelines) | **GET** /api/v1/pipelines | list pipelines
[**run_pipeline**](PipelineApi.md#run_pipeline) | **POST** /api/v1/projects/{projectName}/pipelines/{pipelineName}/run | run pipeline
[**stop_pipeline**](PipelineApi.md#stop_pipeline) | **POST** /api/v1/projects/{projectName}/pipelines/{pipelineName}/runs/{runName}/stop | stop pipeline run
[**update_context_value**](PipelineApi.md#update_context_value) | **PUT** /api/v1/projects/{projectName}/pipelines/{pipelineName}/contexts/{contextName} | update pipeline context value
[**update_pipeline**](PipelineApi.md#update_pipeline) | **PUT** /api/v1/projects/{projectName}/pipelines/{pipelineName} | update pipeline

# **create_context_value**
> V1Context create_context_value(body, project_name, pipeline_name)

create pipeline context values

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
body = vela_client.V1CreateContextValuesRequest()  # V1CreateContextValuesRequest | 
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name

try:
    # create pipeline context values
    api_response = api_instance.create_context_value(body, project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->create_context_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateContextValuesRequest**](V1CreateContextValuesRequest.md)|  | 
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 

### Return type

[**V1Context**](V1Context.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pipeline**
> V1PipelineBase create_pipeline(body, project_name)

create pipeline

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
body = vela_client.V1CreatePipelineRequest()  # V1CreatePipelineRequest | 
project_name = 'project_name_example'  # str | project name

try:
    # create pipeline
    api_response = api_instance.create_pipeline(body, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->create_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreatePipelineRequest**](V1CreatePipelineRequest.md)|  | 
 **project_name** | **str**| project name | 

### Return type

[**V1PipelineBase**](V1PipelineBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_context_value**
> V1ContextNameResponse delete_context_value(project_name, pipeline_name, context_name)

delete pipeline context value

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
context_name = 'context_name_example'  # str | pipeline context name

try:
    # delete pipeline context value
    api_response = api_instance.delete_context_value(project_name, pipeline_name, context_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->delete_context_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **context_name** | **str**| pipeline context name | 

### Return type

[**V1ContextNameResponse**](V1ContextNameResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline**
> V1PipelineMetaResponse delete_pipeline(project_name, pipeline_name)

delete pipeline

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name

try:
    # delete pipeline
    api_response = api_instance.delete_pipeline(project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->delete_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 

### Return type

[**V1PipelineMetaResponse**](V1PipelineMetaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline_run**
> V1PipelineRunMeta delete_pipeline_run(project_name, pipeline_name, run_name)

delete pipeline run

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
run_name = 'run_name_example'  # str | pipeline run name

try:
    # delete pipeline run
    api_response = api_instance.delete_pipeline_run(project_name, pipeline_name, run_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->delete_pipeline_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **run_name** | **str**| pipeline run name | 

### Return type

[**V1PipelineRunMeta**](V1PipelineRunMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> V1GetPipelineResponse get_pipeline(pipeline_name, project_name)

get pipeline

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
pipeline_name = 'pipeline_name_example'  # str | pipeline name
project_name = 'project_name_example'  # str | project name

try:
    # get pipeline
    api_response = api_instance.get_pipeline(pipeline_name, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| pipeline name | 
 **project_name** | **str**| project name | 

### Return type

[**V1GetPipelineResponse**](V1GetPipelineResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_run**
> V1PipelineRunBase get_pipeline_run(project_name, pipeline_name, run_name)

get pipeline run

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
run_name = 'run_name_example'  # str | pipeline run name

try:
    # get pipeline run
    api_response = api_instance.get_pipeline_run(project_name, pipeline_name, run_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **run_name** | **str**| pipeline run name | 

### Return type

[**V1PipelineRunBase**](V1PipelineRunBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_run_input**
> V1GetPipelineRunInputResponse get_pipeline_run_input(step, project_name, pipeline_name, run_name)

get pipeline run input

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
step = 'step_example'  # str | query by specific step name
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
run_name = 'run_name_example'  # str | pipeline run name

try:
    # get pipeline run input
    api_response = api_instance.get_pipeline_run_input(step, project_name, pipeline_name, run_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline_run_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **step** | **str**| query by specific step name | 
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **run_name** | **str**| pipeline run name | 

### Return type

[**V1GetPipelineRunInputResponse**](V1GetPipelineRunInputResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_run_log**
> V1GetPipelineRunLogResponse get_pipeline_run_log(project_name, pipeline_name, run_name, step=step)

get pipeline run log

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
run_name = 'run_name_example'  # str | pipeline run name
step = 'step_example'  # str | query by specific step name (optional)

try:
    # get pipeline run log
    api_response = api_instance.get_pipeline_run_log(project_name, pipeline_name, run_name, step=step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline_run_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **run_name** | **str**| pipeline run name | 
 **step** | **str**| query by specific step name | [optional] 

### Return type

[**V1GetPipelineRunLogResponse**](V1GetPipelineRunLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_run_output**
> V1GetPipelineRunOutputResponse get_pipeline_run_output(step, project_name, pipeline_name, run_name)

get pipeline run output

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
step = 'step_example'  # str | query by specific step name
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
run_name = 'run_name_example'  # str | pipeline run name

try:
    # get pipeline run output
    api_response = api_instance.get_pipeline_run_output(step, project_name, pipeline_name, run_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline_run_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **step** | **str**| query by specific step name | 
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **run_name** | **str**| pipeline run name | 

### Return type

[**V1GetPipelineRunOutputResponse**](V1GetPipelineRunOutputResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_run_status**
> V1alpha1WorkflowRunStatus get_pipeline_run_status(project_name, pipeline_name, run_name)

get pipeline run status

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
run_name = 'run_name_example'  # str | pipeline run name

try:
    # get pipeline run status
    api_response = api_instance.get_pipeline_run_status(project_name, pipeline_name, run_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline_run_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **run_name** | **str**| pipeline run name | 

### Return type

[**V1alpha1WorkflowRunStatus**](V1alpha1WorkflowRunStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_context_values**
> V1ListContextValueResponse list_context_values(project_name, pipeline_name)

list pipeline context values

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name

try:
    # list pipeline context values
    api_response = api_instance.list_context_values(project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->list_context_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 

### Return type

[**V1ListContextValueResponse**](V1ListContextValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipeline_runs**
> V1ListPipelineRunResponse list_pipeline_runs(project_name, pipeline_name, status=status)

list pipeline runs

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
status = 'status_example'  # str | query identifier of the status (optional)

try:
    # list pipeline runs
    api_response = api_instance.list_pipeline_runs(project_name, pipeline_name, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->list_pipeline_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **status** | **str**| query identifier of the status | [optional] 

### Return type

[**V1ListPipelineRunResponse**](V1ListPipelineRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipelines**
> V1ListPipelineResponse list_pipelines(query=query, project_name=project_name, detailed=detailed)

list pipelines

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
query = 'query_example'  # str | Fuzzy search based on name or description (optional)
project_name = 'project_name_example'  # str | query pipelines within a project (optional)
detailed = true  # object | query pipelines with detail (optional) (default to true)

try:
    # list pipelines
    api_response = api_instance.list_pipelines(query=query, project_name=project_name, detailed=detailed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->list_pipelines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Fuzzy search based on name or description | [optional] 
 **project_name** | **str**| query pipelines within a project | [optional] 
 **detailed** | [**object**](.md)| query pipelines with detail | [optional] [default to true]

### Return type

[**V1ListPipelineResponse**](V1ListPipelineResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_pipeline**
> V1PipelineRun run_pipeline(body, project_name, pipeline_name)

run pipeline

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
body = vela_client.V1RunPipelineRequest()  # V1RunPipelineRequest | 
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name

try:
    # run pipeline
    api_response = api_instance.run_pipeline(body, project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->run_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RunPipelineRequest**](V1RunPipelineRequest.md)|  | 
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 

### Return type

[**V1PipelineRun**](V1PipelineRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_pipeline**
> V1PipelineRunMeta stop_pipeline(project_name, pipeline_name, run_name)

stop pipeline run

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
run_name = 'run_name_example'  # str | pipeline run name

try:
    # stop pipeline run
    api_response = api_instance.stop_pipeline(project_name, pipeline_name, run_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->stop_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **run_name** | **str**| pipeline run name | 

### Return type

[**V1PipelineRunMeta**](V1PipelineRunMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_context_value**
> V1Context update_context_value(body, project_name, pipeline_name, context_name)

update pipeline context value

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
body = vela_client.V1UpdateContextValuesRequest()  # V1UpdateContextValuesRequest | 
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name
context_name = 'context_name_example'  # str | pipeline context name

try:
    # update pipeline context value
    api_response = api_instance.update_context_value(body, project_name, pipeline_name, context_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->update_context_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateContextValuesRequest**](V1UpdateContextValuesRequest.md)|  | 
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 
 **context_name** | **str**| pipeline context name | 

### Return type

[**V1Context**](V1Context.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline**
> V1PipelineBase update_pipeline(body, project_name, pipeline_name)

update pipeline

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.PipelineApi()
body = vela_client.V1UpdatePipelineRequest()  # V1UpdatePipelineRequest | 
project_name = 'project_name_example'  # str | project name
pipeline_name = 'pipeline_name_example'  # str | pipeline name

try:
    # update pipeline
    api_response = api_instance.update_pipeline(body, project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->update_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdatePipelineRequest**](V1UpdatePipelineRequest.md)|  | 
 **project_name** | **str**| project name | 
 **pipeline_name** | **str**| pipeline name | 

### Return type

[**V1PipelineBase**](V1PipelineBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

