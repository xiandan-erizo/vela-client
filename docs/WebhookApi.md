# swagger_client.WebhookApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_application_webhook**](WebhookApi.md#handle_application_webhook) | **POST** /api/v1/webhook/{token} | handle application webhook request

# **handle_application_webhook**
> V1ApplicationDeployResponse handle_application_webhook(body, token)

handle application webhook request

### Example

```python
from __future__ import print_function
import time
import vela_client
from vela_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela_client.WebhookApi()
body = vela_client.V1HandleApplicationTriggerWebhookRequest()  # V1HandleApplicationTriggerWebhookRequest | 
token = 'token_example'  # str | webhook token

try:
    # handle application webhook request
    api_response = api_instance.handle_application_webhook(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->handle_application_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HandleApplicationTriggerWebhookRequest**](V1HandleApplicationTriggerWebhookRequest.md)|  | 
 **token** | **str**| webhook token | 

### Return type

[**V1ApplicationDeployResponse**](V1ApplicationDeployResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

