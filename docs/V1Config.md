# V1Config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args_escaped** | **bool** |  | [optional] 
**attach_stderr** | **bool** |  | [optional] 
**attach_stdin** | **bool** |  | [optional] 
**attach_stdout** | **bool** |  | [optional] 
**cmd** | **list[str]** |  | [optional] 
**domainname** | **str** |  | [optional] 
**entrypoint** | **list[str]** |  | [optional] 
**env** | **list[str]** |  | [optional] 
**exposed_ports** | [**dict(str, V1ConfigExposedPorts)**](V1ConfigExposedPorts.md) |  | [optional] 
**healthcheck** | [**V1HealthConfig**](V1HealthConfig.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**labels** | **dict(str, str)** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**network_disabled** | **bool** |  | [optional] 
**on_build** | **list[str]** |  | [optional] 
**open_stdin** | **bool** |  | [optional] 
**shell** | **list[str]** |  | [optional] 
**stdin_once** | **bool** |  | [optional] 
**stop_signal** | **str** |  | [optional] 
**tty** | **bool** |  | [optional] 
**user** | **str** |  | [optional] 
**volumes** | [**dict(str, V1ConfigVolumes)**](V1ConfigVolumes.md) |  | [optional] 
**working_dir** | **str** |  | [optional] 

[[Back to Model list]](../vela-client/README.md#documentation-for-models) [[Back to API list]](../vela-client/README.md#documentation-for-api-endpoints) [[Back to README]](../vela-client/README.md)

