# CommonAppStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_resources** | [**list[CommonClusterObjectReference]**](CommonClusterObjectReference.md) |  | [optional] 
**components** | [**list[V1ObjectReference]**](V1ObjectReference.md) |  | [optional] 
**conditions** | [**list[ConditionCondition]**](ConditionCondition.md) |  | [optional] 
**latest_revision** | [**CommonRevision**](CommonRevision.md) |  | [optional] 
**observed_generation** | **int** |  | [optional] 
**policy** | [**list[CommonPolicyStatus]**](CommonPolicyStatus.md) |  | [optional] 
**services** | [**list[CommonApplicationComponentStatus]**](CommonApplicationComponentStatus.md) |  | [optional] 
**status** | **str** |  | [optional] 
**workflow** | [**CommonWorkflowStatus**](CommonWorkflowStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

