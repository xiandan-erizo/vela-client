# swagger_client.ApplicationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_application_trait**](ApplicationApi.md#add_application_trait) | **POST** /api/v1/applications/{appName}/components/{compName}/traits | add trait for a component
[**application_statistics**](ApplicationApi.md#application_statistics) | **GET** /api/v1/applications/{appName}/statistics | detail one application 
[**compare_app**](ApplicationApi.md#compare_app) | **POST** /api/v1/applications/{appName}/compare | compare application
[**create_application**](ApplicationApi.md#create_application) | **POST** /api/v1/applications | create one application 
[**create_application_env**](ApplicationApi.md#create_application_env) | **POST** /api/v1/applications/{appName}/envs | creating an application environment 
[**create_application_policy**](ApplicationApi.md#create_application_policy) | **POST** /api/v1/applications/{appName}/policies | create policy for application
[**create_application_trigger**](ApplicationApi.md#create_application_trigger) | **POST** /api/v1/applications/{appName}/triggers | Create an application trigger
[**create_component**](ApplicationApi.md#create_component) | **POST** /api/v1/applications/{appName}/components | create component  for application 
[**create_or_update_application_workflow**](ApplicationApi.md#create_or_update_application_workflow) | **POST** /api/v1/applications/{appName}/workflows | create application workflow
[**delete_application**](ApplicationApi.md#delete_application) | **DELETE** /api/v1/applications/{appName} | delete one application
[**delete_application_env**](ApplicationApi.md#delete_application_env) | **DELETE** /api/v1/applications/{appName}/envs/{envName} | delete an application environment 
[**delete_application_policy**](ApplicationApi.md#delete_application_policy) | **DELETE** /api/v1/applications/{appName}/policies/{policyName} | detail policy for application
[**delete_application_trait**](ApplicationApi.md#delete_application_trait) | **DELETE** /api/v1/applications/{appName}/components/{compName}/traits/{traitType} | delete trait from a component
[**delete_application_trigger**](ApplicationApi.md#delete_application_trigger) | **DELETE** /api/v1/applications/{appName}/triggers/{token} | Delete an application trigger
[**delete_component**](ApplicationApi.md#delete_component) | **DELETE** /api/v1/applications/{appName}/components/{compName} | delete a component
[**delete_workflow**](ApplicationApi.md#delete_workflow) | **DELETE** /api/v1/applications/{appName}/workflows/{workflowName} | deletet workflow
[**deploy_application**](ApplicationApi.md#deploy_application) | **POST** /api/v1/applications/{appName}/deploy | deploy or upgrade the application
[**detail_application**](ApplicationApi.md#detail_application) | **GET** /api/v1/applications/{appName} | detail one application 
[**detail_application_policy**](ApplicationApi.md#detail_application_policy) | **GET** /api/v1/applications/{appName}/policies/{policyName} | detail policy for application
[**detail_application_revision**](ApplicationApi.md#detail_application_revision) | **GET** /api/v1/applications/{appName}/revisions/{revision} | detail revision for application
[**detail_component**](ApplicationApi.md#detail_component) | **GET** /api/v1/applications/{appName}/components/{compName} | detail component for application 
[**detail_workflow**](ApplicationApi.md#detail_workflow) | **GET** /api/v1/applications/{appName}/workflows/{workflowName} | detail application workflow
[**detail_workflow_record**](ApplicationApi.md#detail_workflow_record) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records/{record} | query application workflow execution record detail
[**dry_run_app_or_revision**](ApplicationApi.md#dry_run_app_or_revision) | **POST** /api/v1/applications/{appName}/dry-run | dry-run application to latest revision
[**get_application_status**](ApplicationApi.md#get_application_status) | **GET** /api/v1/applications/{appName}/envs/{envName}/status | get application status
[**get_workflow_record_inputs**](ApplicationApi.md#get_workflow_record_inputs) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records/{record}/inputs | get the workflow step inputs
[**get_workflow_record_logs**](ApplicationApi.md#get_workflow_record_logs) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records/{record}/logs | get the workflow step logs
[**get_workflow_record_outputs**](ApplicationApi.md#get_workflow_record_outputs) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records/{record}/outputs | get the workflow step inputs
[**list_application_components**](ApplicationApi.md#list_application_components) | **GET** /api/v1/applications/{appName}/components | gets the list of application components
[**list_application_envs**](ApplicationApi.md#list_application_envs) | **GET** /api/v1/applications/{appName}/envs | list policy for application
[**list_application_policies**](ApplicationApi.md#list_application_policies) | **GET** /api/v1/applications/{appName}/policies | list policy for application
[**list_application_records**](ApplicationApi.md#list_application_records) | **GET** /api/v1/applications/{appName}/records | list application records
[**list_application_revisions**](ApplicationApi.md#list_application_revisions) | **GET** /api/v1/applications/{appName}/revisions | list revisions for application
[**list_application_triggers**](ApplicationApi.md#list_application_triggers) | **GET** /api/v1/applications/{appName}/triggers | List the application triggers
[**list_application_workflows**](ApplicationApi.md#list_application_workflows) | **GET** /api/v1/applications/{appName}/workflows | list application workflow
[**list_applications**](ApplicationApi.md#list_applications) | **GET** /api/v1/applications | list all applications
[**list_workflow_records**](ApplicationApi.md#list_workflow_records) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records | query application workflow execution record
[**publish_application_template**](ApplicationApi.md#publish_application_template) | **POST** /api/v1/applications/{appName}/template | create one application template
[**recycle_application_env**](ApplicationApi.md#recycle_application_env) | **POST** /api/v1/applications/{appName}/envs/{envName}/recycle | get application status
[**reset_app_to_latest_revision**](ApplicationApi.md#reset_app_to_latest_revision) | **POST** /api/v1/applications/{appName}/reset | reset application to latest revision
[**resume_workflow_record**](ApplicationApi.md#resume_workflow_record) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records/{record}/resume | resume suspend workflow record
[**rollback_application_with_revision**](ApplicationApi.md#rollback_application_with_revision) | **POST** /api/v1/applications/{appName}/revisions/{revision}/rollback | detail revision for application
[**rollback_workflow_record**](ApplicationApi.md#rollback_workflow_record) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records/{record}/rollback | rollback suspend application record
[**terminate_workflow_record**](ApplicationApi.md#terminate_workflow_record) | **GET** /api/v1/applications/{appName}/workflows/{workflowName}/records/{record}/terminate | terminate suspend workflow record
[**update_application**](ApplicationApi.md#update_application) | **PUT** /api/v1/applications/{appName} | update one application 
[**update_application_env**](ApplicationApi.md#update_application_env) | **PUT** /api/v1/applications/{appName}/envs/{envName} | set application  differences in the specified environment
[**update_application_policy**](ApplicationApi.md#update_application_policy) | **PUT** /api/v1/applications/{appName}/policies/{policyName} | update policy for application
[**update_application_trait**](ApplicationApi.md#update_application_trait) | **PUT** /api/v1/applications/{appName}/components/{compName}/traits/{traitType} | update trait from a component
[**update_application_trigger**](ApplicationApi.md#update_application_trigger) | **PUT** /api/v1/applications/{appName}/triggers/{token} | Update an application trigger
[**update_component**](ApplicationApi.md#update_component) | **PUT** /api/v1/applications/{appName}/components/{compName} | update component config
[**update_workflow**](ApplicationApi.md#update_workflow) | **PUT** /api/v1/applications/{appName}/workflows/{workflowName} | update application workflow config

# **add_application_trait**
> V1EmptyResponse add_application_trait(body, app_name, comp_name)

add trait for a component

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreateApplicationTraitRequest()  # V1CreateApplicationTraitRequest | 
app_name = 'app_name_example'  # str | identifier of the application
comp_name = 'comp_name_example'  # str | identifier of the component

try:
    # add trait for a component
    api_response = api_instance.add_application_trait(body, app_name, comp_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->add_application_trait: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateApplicationTraitRequest**](V1CreateApplicationTraitRequest.md)|  | 
 **app_name** | **str**| identifier of the application | 
 **comp_name** | **str**| identifier of the component | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **application_statistics**
> V1ApplicationStatisticsResponse application_statistics(app_name)

detail one application 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # detail one application 
    api_response = api_instance.application_statistics(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->application_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ApplicationStatisticsResponse**](V1ApplicationStatisticsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **compare_app**
> V1AppCompareResponse compare_app(body, app_name)

compare application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1AppCompareReq()  # V1AppCompareReq | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # compare application
    api_response = api_instance.compare_app(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->compare_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AppCompareReq**](V1AppCompareReq.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1AppCompareResponse**](V1AppCompareResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_application**
> V1ApplicationBase create_application(body)

create one application 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreateApplicationRequest()  # V1CreateApplicationRequest | 

try:
    # create one application 
    api_response = api_instance.create_application(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateApplicationRequest**](V1CreateApplicationRequest.md)|  | 

### Return type

[**V1ApplicationBase**](V1ApplicationBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_application_env**
> V1EnvBinding create_application_env(body, app_name)

creating an application environment 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreateApplicationEnvbindingRequest()  # V1CreateApplicationEnvbindingRequest | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # creating an application environment 
    api_response = api_instance.create_application_env(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_application_env: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateApplicationEnvbindingRequest**](V1CreateApplicationEnvbindingRequest.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1EnvBinding**](V1EnvBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_application_policy**
> V1PolicyBase create_application_policy(body, app_name)

create policy for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreatePolicyRequest()  # V1CreatePolicyRequest | 
app_name = 'app_name_example'  # str | identifier of the application

try:
    # create policy for application
    api_response = api_instance.create_application_policy(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_application_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreatePolicyRequest**](V1CreatePolicyRequest.md)|  | 
 **app_name** | **str**| identifier of the application | 

### Return type

[**V1PolicyBase**](V1PolicyBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_application_trigger**
> V1ApplicationTriggerBase create_application_trigger(body, app_name)

Create an application trigger

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreateApplicationTriggerRequest()  # V1CreateApplicationTriggerRequest | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # Create an application trigger
    api_response = api_instance.create_application_trigger(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_application_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateApplicationTriggerRequest**](V1CreateApplicationTriggerRequest.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ApplicationTriggerBase**](V1ApplicationTriggerBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_component**
> V1ComponentBase create_component(body, app_name)

create component  for application 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreateComponentRequest()  # V1CreateComponentRequest | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # create component  for application 
    api_response = api_instance.create_component(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateComponentRequest**](V1CreateComponentRequest.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ComponentBase**](V1ComponentBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **create_or_update_application_workflow**
> V1SimpleResponse create_or_update_application_workflow(body, app_name)

create application workflow

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreateWorkflowRequest()  # V1CreateWorkflowRequest | 
app_name = 'app_name_example'  # str | identifier of the application.

try:
    # create application workflow
    api_response = api_instance.create_or_update_application_workflow(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_or_update_application_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateWorkflowRequest**](V1CreateWorkflowRequest.md)|  | 
 **app_name** | **str**| identifier of the application. | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_application**
> V1EmptyResponse delete_application(app_name)

delete one application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # delete one application
    api_response = api_instance.delete_application(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_application_env**
> V1EmptyResponse delete_application_env(app_name, env_name)

delete an application environment 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
env_name = 'env_name_example'  # str | identifier of the envBinding 

try:
    # delete an application environment 
    api_response = api_instance.delete_application_env(app_name, env_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application_env: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **env_name** | **str**| identifier of the envBinding  | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_application_policy**
> V1EmptyResponse delete_application_policy(app_name, policy_name, force=force)

detail policy for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application
policy_name = 'policy_name_example'  # str | identifier of the application policy
force = true  # bool | Force delete the policy and all references (optional)

try:
    # detail policy for application
    api_response = api_instance.delete_application_policy(app_name, policy_name, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application | 
 **policy_name** | **str**| identifier of the application policy | 
 **force** | **bool**| Force delete the policy and all references | [optional] 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_application_trait**
> V1ApplicationTrait delete_application_trait(app_name, comp_name, trait_type)

delete trait from a component

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application
comp_name = 'comp_name_example'  # str | identifier of the component
trait_type = 'trait_type_example'  # str | identifier of the type of trait

try:
    # delete trait from a component
    api_response = api_instance.delete_application_trait(app_name, comp_name, trait_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application_trait: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application | 
 **comp_name** | **str**| identifier of the component | 
 **trait_type** | **str**| identifier of the type of trait | 

### Return type

[**V1ApplicationTrait**](V1ApplicationTrait.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_application_trigger**
> V1EmptyResponse delete_application_trigger(app_name, token)

Delete an application trigger

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
token = 'token_example'  # str | identifier of the trigger

try:
    # Delete an application trigger
    api_response = api_instance.delete_application_trigger(app_name, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **token** | **str**| identifier of the trigger | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_component**
> V1EmptyResponse delete_component(app_name, comp_name)

delete a component

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application
comp_name = 'comp_name_example'  # str | identifier of the component

try:
    # delete a component
    api_response = api_instance.delete_component(app_name, comp_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application | 
 **comp_name** | **str**| identifier of the component | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **delete_workflow**
> V1SimpleResponse delete_workflow(app_name, workflow_name)

deletet workflow

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow

try:
    # deletet workflow
    api_response = api_instance.delete_workflow(app_name, workflow_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **deploy_application**
> V1ApplicationDeployResponse deploy_application(body, app_name)

deploy or upgrade the application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1ApplicationDeployRequest()  # V1ApplicationDeployRequest | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # deploy or upgrade the application
    api_response = api_instance.deploy_application(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->deploy_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ApplicationDeployRequest**](V1ApplicationDeployRequest.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ApplicationDeployResponse**](V1ApplicationDeployResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_application**
> V1DetailApplicationResponse detail_application(app_name)

detail one application 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # detail one application 
    api_response = api_instance.detail_application(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->detail_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1DetailApplicationResponse**](V1DetailApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_application_policy**
> V1DetailPolicyResponse detail_application_policy(app_name, policy_name)

detail policy for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application
policy_name = 'policy_name_example'  # str | identifier of the application policy

try:
    # detail policy for application
    api_response = api_instance.detail_application_policy(app_name, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->detail_application_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application | 
 **policy_name** | **str**| identifier of the application policy | 

### Return type

[**V1DetailPolicyResponse**](V1DetailPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_application_revision**
> V1DetailRevisionResponse detail_application_revision(app_name, revision)

detail revision for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application
revision = 'revision_example'  # str | identifier of the application revision

try:
    # detail revision for application
    api_response = api_instance.detail_application_revision(app_name, revision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->detail_application_revision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application | 
 **revision** | **str**| identifier of the application revision | 

### Return type

[**V1DetailRevisionResponse**](V1DetailRevisionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_component**
> V1DetailComponentResponse detail_component(app_name, comp_name)

detail component for application 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
comp_name = 'comp_name_example'  # str | identifier of the component

try:
    # detail component for application 
    api_response = api_instance.detail_component(app_name, comp_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->detail_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **comp_name** | **str**| identifier of the component | 

### Return type

[**V1DetailComponentResponse**](V1DetailComponentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_workflow**
> V1SimpleResponse detail_workflow(app_name, workflow_name)

detail application workflow

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workfloc.

try:
    # detail application workflow
    api_response = api_instance.detail_workflow(app_name, workflow_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->detail_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workfloc. | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **detail_workflow_record**
> V1SimpleResponse detail_workflow_record(app_name, workflow_name, record)

query application workflow execution record detail

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
record = 'record_example'  # str | identifier of the workflow record

try:
    # query application workflow execution record detail
    api_response = api_instance.detail_workflow_record(app_name, workflow_name, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->detail_workflow_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **record** | **str**| identifier of the workflow record | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **dry_run_app_or_revision**
> V1AppDryRunResponse dry_run_app_or_revision(body, app_name)

dry-run application to latest revision

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1AppDryRunReq()  # V1AppDryRunReq | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # dry-run application to latest revision
    api_response = api_instance.dry_run_app_or_revision(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->dry_run_app_or_revision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AppDryRunReq**](V1AppDryRunReq.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1AppDryRunResponse**](V1AppDryRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_application_status**
> V1ApplicationStatusResponse get_application_status(app_name, env_name)

get application status

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
env_name = 'env_name_example'  # str | identifier of the application envbinding

try:
    # get application status
    api_response = api_instance.get_application_status(app_name, env_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **env_name** | **str**| identifier of the application envbinding | 

### Return type

[**V1ApplicationStatusResponse**](V1ApplicationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_workflow_record_inputs**
> V1GetPipelineRunInputResponse get_workflow_record_inputs(app_name, workflow_name, record, step)

get the workflow step inputs

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
record = 'record_example'  # str | identifier of the workflow record
step = 'step_example'  # str | Specified the step filter

try:
    # get the workflow step inputs
    api_response = api_instance.get_workflow_record_inputs(app_name, workflow_name, record, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_workflow_record_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **record** | **str**| identifier of the workflow record | 
 **step** | **str**| Specified the step filter | 

### Return type

[**V1GetPipelineRunInputResponse**](V1GetPipelineRunInputResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_workflow_record_logs**
> get_workflow_record_logs(app_name, workflow_name, record, step)

get the workflow step logs

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
record = 'record_example'  # str | identifier of the workflow record
step = 'step_example'  # str | Specified the step filter

try:
    # get the workflow step logs
    api_instance.get_workflow_record_logs(app_name, workflow_name, record, step)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_workflow_record_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **record** | **str**| identifier of the workflow record | 
 **step** | **str**| Specified the step filter | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **get_workflow_record_outputs**
> V1GetPipelineRunOutputResponse get_workflow_record_outputs(app_name, workflow_name, record, step)

get the workflow step inputs

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
record = 'record_example'  # str | identifier of the workflow record
step = 'step_example'  # str | Specified the step filter

try:
    # get the workflow step inputs
    api_response = api_instance.get_workflow_record_outputs(app_name, workflow_name, record, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_workflow_record_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **record** | **str**| identifier of the workflow record | 
 **step** | **str**| Specified the step filter | 

### Return type

[**V1GetPipelineRunOutputResponse**](V1GetPipelineRunOutputResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_application_components**
> V1ComponentListResponse list_application_components(app_name, env_name=env_name)

gets the list of application components

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
env_name = 'env_name_example'  # str | list components that deployed in define env (optional)

try:
    # gets the list of application components
    api_response = api_instance.list_application_components(app_name, env_name=env_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **env_name** | **str**| list components that deployed in define env | [optional] 

### Return type

[**V1ComponentListResponse**](V1ComponentListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_application_envs**
> V1ListApplicationEnvBinding list_application_envs(app_name)

list policy for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # list policy for application
    api_response = api_instance.list_application_envs(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_envs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ListApplicationEnvBinding**](V1ListApplicationEnvBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_application_policies**
> V1ListApplicationPolicy list_application_policies(app_name)

list policy for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # list policy for application
    api_response = api_instance.list_application_policies(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ListApplicationPolicy**](V1ListApplicationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_application_records**
> list_application_records(app_name)

list application records

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.

try:
    # list application records
    api_instance.list_application_records(app_name)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_application_revisions**
> V1ListRevisionsResponse list_application_revisions(app_name, env_name=env_name, status=status, page=page, page_size=page_size)

list revisions for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
env_name = 'env_name_example'  # str | query identifier of the env (optional)
status = 'status_example'  # str | query identifier of the status (optional)
page = 56  # int | query the page number (optional)
page_size = 56  # int | query the page size number (optional)

try:
    # list revisions for application
    api_response = api_instance.list_application_revisions(app_name, env_name=env_name, status=status, page=page,
                                                           page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_revisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **env_name** | **str**| query identifier of the env | [optional] 
 **status** | **str**| query identifier of the status | [optional] 
 **page** | **int**| query the page number | [optional] 
 **page_size** | **int**| query the page size number | [optional] 

### Return type

[**V1ListRevisionsResponse**](V1ListRevisionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_application_triggers**
> V1ListApplicationTriggerResponse list_application_triggers(app_name)

List the application triggers

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # List the application triggers
    api_response = api_instance.list_application_triggers(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ListApplicationTriggerResponse**](V1ListApplicationTriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_application_workflows**
> V1SimpleResponse list_application_workflows(app_name)

list application workflow

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.

try:
    # list application workflow
    api_response = api_instance.list_application_workflows(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_applications**
> V1ListApplicationResponse list_applications(query=query, project=project, env=env, target_name=target_name)

list all applications

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
query = 'query_example'  # str | Fuzzy search based on name or description (optional)
project = 'project_example'  # str | search base on project name (optional)
env = 'env_example'  # str | search base on env name (optional)
target_name = 'target_name_example'  # str | Name of the application delivery target (optional)

try:
    # list all applications
    api_response = api_instance.list_applications(query=query, project=project, env=env, target_name=target_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Fuzzy search based on name or description | [optional] 
 **project** | **str**| search base on project name | [optional] 
 **env** | **str**| search base on env name | [optional] 
 **target_name** | **str**| Name of the application delivery target | [optional] 

### Return type

[**V1ListApplicationResponse**](V1ListApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **list_workflow_records**
> V1SimpleResponse list_workflow_records(app_name, workflow_name, page=page, page_size=page_size)

query application workflow execution record

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
page = 56  # int | query the page number (optional)
page_size = 56  # int | query the page size number (optional)

try:
    # query application workflow execution record
    api_response = api_instance.list_workflow_records(app_name, workflow_name, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_workflow_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **page** | **int**| query the page number | [optional] 
 **page_size** | **int**| query the page size number | [optional] 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **publish_application_template**
> V1ApplicationTemplateBase publish_application_template(body, app_name)

create one application template

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1CreateApplicationTemplateRequest()  # V1CreateApplicationTemplateRequest | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # create one application template
    api_response = api_instance.publish_application_template(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->publish_application_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateApplicationTemplateRequest**](V1CreateApplicationTemplateRequest.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ApplicationTemplateBase**](V1ApplicationTemplateBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **recycle_application_env**
> V1EmptyResponse recycle_application_env(app_name, env_name)

get application status

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
env_name = 'env_name_example'  # str | identifier of the application envbinding

try:
    # get application status
    api_response = api_instance.recycle_application_env(app_name, env_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->recycle_application_env: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **env_name** | **str**| identifier of the application envbinding | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **reset_app_to_latest_revision**
> V1AppResetResponse reset_app_to_latest_revision(app_name)

reset application to latest revision

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # reset application to latest revision
    api_response = api_instance.reset_app_to_latest_revision(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->reset_app_to_latest_revision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1AppResetResponse**](V1AppResetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **resume_workflow_record**
> V1EmptyResponse resume_workflow_record(app_name, workflow_name, record)

resume suspend workflow record

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
record = 'record_example'  # str | identifier of the  workflow record

try:
    # resume suspend workflow record
    api_response = api_instance.resume_workflow_record(app_name, workflow_name, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->resume_workflow_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **record** | **str**| identifier of the  workflow record | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **rollback_application_with_revision**
> V1ApplicationRollbackResponse rollback_application_with_revision(app_name, revision)

detail revision for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application
revision = 'revision_example'  # str | identifier of the application revision

try:
    # detail revision for application
    api_response = api_instance.rollback_application_with_revision(app_name, revision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->rollback_application_with_revision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application | 
 **revision** | **str**| identifier of the application revision | 

### Return type

[**V1ApplicationRollbackResponse**](V1ApplicationRollbackResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **rollback_workflow_record**
> V1WorkflowRecordBase rollback_workflow_record(app_name, workflow_name, record, rollback_version=rollback_version)

rollback suspend application record

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
record = 'record_example'  # str | identifier of the workflow record
rollback_version = 'rollback_version_example'  # str | identifier of the rollback revision (optional)

try:
    # rollback suspend application record
    api_response = api_instance.rollback_workflow_record(app_name, workflow_name, record,
                                                         rollback_version=rollback_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->rollback_workflow_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **record** | **str**| identifier of the workflow record | 
 **rollback_version** | **str**| identifier of the rollback revision | [optional] 

### Return type

[**V1WorkflowRecordBase**](V1WorkflowRecordBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **terminate_workflow_record**
> V1EmptyResponse terminate_workflow_record(app_name, workflow_name, record)

terminate suspend workflow record

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow
record = 'record_example'  # str | identifier of the workflow record

try:
    # terminate suspend workflow record
    api_response = api_instance.terminate_workflow_record(app_name, workflow_name, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->terminate_workflow_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 
 **record** | **str**| identifier of the workflow record | 

### Return type

[**V1EmptyResponse**](V1EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_application**
> V1ApplicationBase update_application(body, app_name)

update one application 

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1UpdateApplicationRequest()  # V1UpdateApplicationRequest | 
app_name = 'app_name_example'  # str | identifier of the application 

try:
    # update one application 
    api_response = api_instance.update_application(body, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateApplicationRequest**](V1UpdateApplicationRequest.md)|  | 
 **app_name** | **str**| identifier of the application  | 

### Return type

[**V1ApplicationBase**](V1ApplicationBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_application_env**
> V1EnvBinding update_application_env(body, app_name, env_name)

set application  differences in the specified environment

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1PutApplicationEnvBindingRequest()  # V1PutApplicationEnvBindingRequest | 
app_name = 'app_name_example'  # str | identifier of the application 
env_name = 'env_name_example'  # str | identifier of the envBinding 

try:
    # set application  differences in the specified environment
    api_response = api_instance.update_application_env(body, app_name, env_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_application_env: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PutApplicationEnvBindingRequest**](V1PutApplicationEnvBindingRequest.md)|  | 
 **app_name** | **str**| identifier of the application  | 
 **env_name** | **str**| identifier of the envBinding  | 

### Return type

[**V1EnvBinding**](V1EnvBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_application_policy**
> V1DetailPolicyResponse update_application_policy(body, app_name, policy_name)

update policy for application

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1UpdatePolicyRequest()  # V1UpdatePolicyRequest | 
app_name = 'app_name_example'  # str | identifier of the application
policy_name = 'policy_name_example'  # str | identifier of the application policy

try:
    # update policy for application
    api_response = api_instance.update_application_policy(body, app_name, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_application_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdatePolicyRequest**](V1UpdatePolicyRequest.md)|  | 
 **app_name** | **str**| identifier of the application | 
 **policy_name** | **str**| identifier of the application policy | 

### Return type

[**V1DetailPolicyResponse**](V1DetailPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_application_trait**
> V1ApplicationTrait update_application_trait(body, app_name, comp_name, trait_type)

update trait from a component

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1UpdateApplicationTraitRequest()  # V1UpdateApplicationTraitRequest | 
app_name = 'app_name_example'  # str | identifier of the application
comp_name = 'comp_name_example'  # str | identifier of the component
trait_type = 'trait_type_example'  # str | identifier of the type of trait

try:
    # update trait from a component
    api_response = api_instance.update_application_trait(body, app_name, comp_name, trait_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_application_trait: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateApplicationTraitRequest**](V1UpdateApplicationTraitRequest.md)|  | 
 **app_name** | **str**| identifier of the application | 
 **comp_name** | **str**| identifier of the component | 
 **trait_type** | **str**| identifier of the type of trait | 

### Return type

[**V1ApplicationTrait**](V1ApplicationTrait.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_application_trigger**
> V1ApplicationTriggerBase update_application_trigger(app_name, token)

Update an application trigger

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
app_name = 'app_name_example'  # str | identifier of the application 
token = 'token_example'  # str | identifier of the trigger

try:
    # Update an application trigger
    api_response = api_instance.update_application_trigger(app_name, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_application_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| identifier of the application  | 
 **token** | **str**| identifier of the trigger | 

### Return type

[**V1ApplicationTriggerBase**](V1ApplicationTriggerBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_component**
> V1ComponentBase update_component(body, app_name, comp_name)

update component config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1UpdateApplicationComponentRequest()  # V1UpdateApplicationComponentRequest | 
app_name = 'app_name_example'  # str | identifier of the application
comp_name = 'comp_name_example'  # str | identifier of the component

try:
    # update component config
    api_response = api_instance.update_component(body, app_name, comp_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateApplicationComponentRequest**](V1UpdateApplicationComponentRequest.md)|  | 
 **app_name** | **str**| identifier of the application | 
 **comp_name** | **str**| identifier of the component | 

### Return type

[**V1ComponentBase**](V1ComponentBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

# **update_workflow**
> V1SimpleResponse update_workflow(body, app_name, workflow_name)

update application workflow config

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.ApplicationApi()
body = vela_client.V1UpdateWorkflowRequest()  # V1UpdateWorkflowRequest | 
app_name = 'app_name_example'  # str | identifier of the application.
workflow_name = 'workflow_name_example'  # str | identifier of the workflow

try:
    # update application workflow config
    api_response = api_instance.update_workflow(body, app_name, workflow_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateWorkflowRequest**](V1UpdateWorkflowRequest.md)|  | 
 **app_name** | **str**| identifier of the application. | 
 **workflow_name** | **str**| identifier of the workflow | 

### Return type

[**V1SimpleResponse**](V1SimpleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to README]](../vela-client/README.md)

