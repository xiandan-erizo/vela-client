# V1DetailComponentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | 
**app_primary_key** | **str** |  | 
**create_time** | **datetime** |  | 
**creator** | **str** |  | 
**definition** | [**V1beta1ComponentDefinitionSpec**](V1beta1ComponentDefinitionSpec.md) |  | 
**depends_on** | **list[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**external_revision** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**inputs** | [**list[V1alpha1InputItem]**](V1alpha1InputItem.md) |  | [optional] 
**labels** | **dict(str, str)** |  | [optional] 
**main** | **bool** |  | 
**name** | **str** |  | 
**outputs** | [**list[V1alpha1OutputItem]**](V1alpha1OutputItem.md) |  | [optional] 
**properties** | [**ModelJSONStruct**](ModelJSONStruct.md) |  | [optional] 
**scopes** | **dict(str, str)** |  | [optional] 
**traits** | [**list[ModelApplicationTrait]**](ModelApplicationTrait.md) |  | [optional] 
**type** | **str** |  | 
**update_time** | **datetime** |  | 
**workload_type** | [**CommonWorkloadTypeDescriptor**](CommonWorkloadTypeDescriptor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

