# V1alpha1WorkflowRunStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[ConditionCondition]**](ConditionCondition.md) |  | [optional] 
**context_backend** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**end_time** | **str** |  | [optional] 
**finished** | **bool** |  | 
**message** | **str** |  | [optional] 
**mode** | [**V1alpha1WorkflowExecuteMode**](V1alpha1WorkflowExecuteMode.md) |  | 
**start_time** | **str** |  | [optional] 
**status** | **str** |  | 
**steps** | [**list[V1alpha1WorkflowStepStatus]**](V1alpha1WorkflowStepStatus.md) |  | [optional] 
**suspend** | **bool** |  | 
**suspend_state** | **str** |  | [optional] 
**terminated** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

