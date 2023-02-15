# coding: utf-8

# flake8: noqa
"""
    Kubevela api doc

    Kubevela api doc  # noqa: E501

    OpenAPI spec version: v1beta1
    Contact: feedback@mail.kubevela.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from vela_client.models.addon_dependency import AddonDependency
from vela_client.models.addon_git_addon_source import AddonGitAddonSource
from vela_client.models.addon_gitee_addon_source import AddonGiteeAddonSource
from vela_client.models.addon_gitlab_addon_source import AddonGitlabAddonSource
from vela_client.models.addon_helm_source import AddonHelmSource
from vela_client.models.addon_meta import AddonMeta
from vela_client.models.addon_oss_addon_source import AddonOSSAddonSource
from vela_client.models.addon_system_requirements import AddonSystemRequirements
from vela_client.models.bcode_bcode import BcodeBcode
from vela_client.models.chart_dependency import ChartDependency
from vela_client.models.chart_dependency_import_values import ChartDependencyImportValues
from vela_client.models.chart_maintainer import ChartMaintainer
from vela_client.models.chart_metadata import ChartMetadata
from vela_client.models.cloudprovider_cloud_cluster import CloudproviderCloudCluster
from vela_client.models.common_app_status import CommonAppStatus
from vela_client.models.common_application_component import CommonApplicationComponent
from vela_client.models.common_application_component_status import CommonApplicationComponentStatus
from vela_client.models.common_application_trait import CommonApplicationTrait
from vela_client.models.common_application_trait_status import CommonApplicationTraitStatus
from vela_client.models.common_cue import CommonCUE
from vela_client.models.common_child_resource_kind import CommonChildResourceKind
from vela_client.models.common_cluster_object_reference import CommonClusterObjectReference
from vela_client.models.common_definition_reference import CommonDefinitionReference
from vela_client.models.common_helm import CommonHelm
from vela_client.models.common_kube import CommonKube
from vela_client.models.common_kube_parameter import CommonKubeParameter
from vela_client.models.common_policy_status import CommonPolicyStatus
from vela_client.models.common_revision import CommonRevision
from vela_client.models.common_schematic import CommonSchematic
from vela_client.models.common_status import CommonStatus
from vela_client.models.common_terraform import CommonTerraform
from vela_client.models.common_workflow_status import CommonWorkflowStatus
from vela_client.models.common_workload_gvk import CommonWorkloadGVK
from vela_client.models.common_workload_type_descriptor import CommonWorkloadTypeDescriptor
from vela_client.models.condition_condition import ConditionCondition
from vela_client.models.condition_conditioned_status import ConditionConditionedStatus
from vela_client.models.config_cluster_target import ConfigClusterTarget
from vela_client.models.config_cluster_target_status import ConfigClusterTargetStatus
from vela_client.models.config_distribution import ConfigDistribution
from vela_client.models.config_namespaced_name import ConfigNamespacedName
from vela_client.models.map_stringinterface_ import MapStringinterface_
from vela_client.models.model_application_component import ModelApplicationComponent
from vela_client.models.model_application_revision import ModelApplicationRevision
from vela_client.models.model_application_trait import ModelApplicationTrait
from vela_client.models.model_base_model import ModelBaseModel
from vela_client.models.model_cluster import ModelCluster
from vela_client.models.model_code_info import ModelCodeInfo
from vela_client.models.model_image_info import ModelImageInfo
from vela_client.models.model_image_repository import ModelImageRepository
from vela_client.models.model_image_resource import ModelImageResource
from vela_client.models.model_json_struct import ModelJSONStruct
from vela_client.models.model_project_ref import ModelProjectRef
from vela_client.models.model_provider_info import ModelProviderInfo
from vela_client.models.model_step_status import ModelStepStatus
from vela_client.models.model_value import ModelValue
from vela_client.models.model_workflow_spec import ModelWorkflowSpec
from vela_client.models.model_workflow_step import ModelWorkflowStep
from vela_client.models.model_workflow_step_base import ModelWorkflowStepBase
from vela_client.models.model_workflow_step_status import ModelWorkflowStepStatus
from vela_client.models.repo_chart_version import RepoChartVersion
from vela_client.models.types_namespaced_name import TypesNamespacedName
from vela_client.models.types_reference import TypesReference
from vela_client.models.types_secret_reference import TypesSecretReference
from vela_client.models.utils_condition import UtilsCondition
from vela_client.models.utils_condition_value import UtilsConditionValue
from vela_client.models.utils_group_option import UtilsGroupOption
from vela_client.models.utils_option import UtilsOption
from vela_client.models.utils_option_value import UtilsOptionValue
from vela_client.models.utils_style import UtilsStyle
from vela_client.models.utils_ui_parameter import UtilsUIParameter
from vela_client.models.utils_validate import UtilsValidate
from vela_client.models.utils_validate_default_value import UtilsValidateDefaultValue
from vela_client.models.v1_access_key_request import V1AccessKeyRequest
from vela_client.models.v1_add_project_user_request import V1AddProjectUserRequest
from vela_client.models.v1_addon_base_status import V1AddonBaseStatus
from vela_client.models.v1_addon_definition import V1AddonDefinition
from vela_client.models.v1_addon_info import V1AddonInfo
from vela_client.models.v1_addon_registry import V1AddonRegistry
from vela_client.models.v1_addon_status_response import V1AddonStatusResponse
from vela_client.models.v1_addon_status_response_clusters import V1AddonStatusResponseClusters
from vela_client.models.v1_app_compare_req import V1AppCompareReq
from vela_client.models.v1_app_compare_response import V1AppCompareResponse
from vela_client.models.v1_app_dry_run_req import V1AppDryRunReq
from vela_client.models.v1_app_dry_run_response import V1AppDryRunResponse
from vela_client.models.v1_app_reset_response import V1AppResetResponse
from vela_client.models.v1_application_base import V1ApplicationBase
from vela_client.models.v1_application_deploy_request import V1ApplicationDeployRequest
from vela_client.models.v1_application_deploy_response import V1ApplicationDeployResponse
from vela_client.models.v1_application_request import V1ApplicationRequest
from vela_client.models.v1_application_resource_info import V1ApplicationResourceInfo
from vela_client.models.v1_application_response import V1ApplicationResponse
from vela_client.models.v1_application_revision_base import V1ApplicationRevisionBase
from vela_client.models.v1_application_statistics_response import V1ApplicationStatisticsResponse
from vela_client.models.v1_application_status_response import V1ApplicationStatusResponse
from vela_client.models.v1_application_template_base import V1ApplicationTemplateBase
from vela_client.models.v1_application_template_version import V1ApplicationTemplateVersion
from vela_client.models.v1_application_trait import V1ApplicationTrait
from vela_client.models.v1_application_trigger_base import V1ApplicationTriggerBase
from vela_client.models.v1_chart_version_list_response import V1ChartVersionListResponse
from vela_client.models.v1_cloud_shell_prepare_response import V1CloudShellPrepareResponse
from vela_client.models.v1_cluster_base import V1ClusterBase
from vela_client.models.v1_cluster_resource_info import V1ClusterResourceInfo
from vela_client.models.v1_cluster_target import V1ClusterTarget
from vela_client.models.v1_compare_latest_with_running_option import V1CompareLatestWithRunningOption
from vela_client.models.v1_compare_revision_with_latest_option import V1CompareRevisionWithLatestOption
from vela_client.models.v1_compare_revision_with_running_option import V1CompareRevisionWithRunningOption
from vela_client.models.v1_component_base import V1ComponentBase
from vela_client.models.v1_component_list_response import V1ComponentListResponse
from vela_client.models.v1_component_selector import V1ComponentSelector
from vela_client.models.v1_config import V1Config
from vela_client.models.v1_config_exposed_ports import V1ConfigExposedPorts
from vela_client.models.v1_config_file import V1ConfigFile
from vela_client.models.v1_config_template import V1ConfigTemplate
from vela_client.models.v1_config_template_detail import V1ConfigTemplateDetail
from vela_client.models.v1_config_volumes import V1ConfigVolumes
from vela_client.models.v1_connect_cloud_cluster_request import V1ConnectCloudClusterRequest
from vela_client.models.v1_context import V1Context
from vela_client.models.v1_context_name_response import V1ContextNameResponse
from vela_client.models.v1_create_addon_registry_request import V1CreateAddonRegistryRequest
from vela_client.models.v1_create_application_envbinding_request import V1CreateApplicationEnvbindingRequest
from vela_client.models.v1_create_application_request import V1CreateApplicationRequest
from vela_client.models.v1_create_application_template_request import V1CreateApplicationTemplateRequest
from vela_client.models.v1_create_application_trait_request import V1CreateApplicationTraitRequest
from vela_client.models.v1_create_application_trigger_request import V1CreateApplicationTriggerRequest
from vela_client.models.v1_create_cloud_cluster_request import V1CreateCloudClusterRequest
from vela_client.models.v1_create_cloud_cluster_response import V1CreateCloudClusterResponse
from vela_client.models.v1_create_cluster_namespace_request import V1CreateClusterNamespaceRequest
from vela_client.models.v1_create_cluster_namespace_response import V1CreateClusterNamespaceResponse
from vela_client.models.v1_create_cluster_request import V1CreateClusterRequest
from vela_client.models.v1_create_component_request import V1CreateComponentRequest
from vela_client.models.v1_create_config_distribution_request import V1CreateConfigDistributionRequest
from vela_client.models.v1_create_config_request import V1CreateConfigRequest
from vela_client.models.v1_create_context_values_request import V1CreateContextValuesRequest
from vela_client.models.v1_create_env_request import V1CreateEnvRequest
from vela_client.models.v1_create_permission_request import V1CreatePermissionRequest
from vela_client.models.v1_create_pipeline_request import V1CreatePipelineRequest
from vela_client.models.v1_create_policy_request import V1CreatePolicyRequest
from vela_client.models.v1_create_project_request import V1CreateProjectRequest
from vela_client.models.v1_create_role_request import V1CreateRoleRequest
from vela_client.models.v1_create_target_request import V1CreateTargetRequest
from vela_client.models.v1_create_user_request import V1CreateUserRequest
from vela_client.models.v1_create_workflow_request import V1CreateWorkflowRequest
from vela_client.models.v1_definition_base import V1DefinitionBase
from vela_client.models.v1_descriptor import V1Descriptor
from vela_client.models.v1_detail_addon_response import V1DetailAddonResponse
from vela_client.models.v1_detail_application_response import V1DetailApplicationResponse
from vela_client.models.v1_detail_cluster_response import V1DetailClusterResponse
from vela_client.models.v1_detail_component_response import V1DetailComponentResponse
from vela_client.models.v1_detail_definition_response import V1DetailDefinitionResponse
from vela_client.models.v1_detail_policy_response import V1DetailPolicyResponse
from vela_client.models.v1_detail_revision_response import V1DetailRevisionResponse
from vela_client.models.v1_detail_target_response import V1DetailTargetResponse
from vela_client.models.v1_detail_user_response import V1DetailUserResponse
from vela_client.models.v1_detail_workflow_record_response import V1DetailWorkflowRecordResponse
from vela_client.models.v1_detail_workflow_response import V1DetailWorkflowResponse
from vela_client.models.v1_dex_config_response import V1DexConfigResponse
from vela_client.models.v1_empty_response import V1EmptyResponse
from vela_client.models.v1_enable_addon_request import V1EnableAddonRequest
from vela_client.models.v1_enabling_progress import V1EnablingProgress
from vela_client.models.v1_env import V1Env
from vela_client.models.v1_env_binding import V1EnvBinding
from vela_client.models.v1_env_binding_base import V1EnvBindingBase
from vela_client.models.v1_env_binding_target import V1EnvBindingTarget
from vela_client.models.v1_get_login_type_response import V1GetLoginTypeResponse
from vela_client.models.v1_get_pipeline_response import V1GetPipelineResponse
from vela_client.models.v1_get_pipeline_run_input_response import V1GetPipelineRunInputResponse
from vela_client.models.v1_get_pipeline_run_log_response import V1GetPipelineRunLogResponse
from vela_client.models.v1_get_pipeline_run_output_response import V1GetPipelineRunOutputResponse
from vela_client.models.v1_handle_application_trigger_webhook_request import V1HandleApplicationTriggerWebhookRequest
from vela_client.models.v1_hash import V1Hash
from vela_client.models.v1_health_config import V1HealthConfig
from vela_client.models.v1_history import V1History
from vela_client.models.v1_image_info import V1ImageInfo
from vela_client.models.v1_image_registry import V1ImageRegistry
from vela_client.models.v1_input_var import V1InputVar
from vela_client.models.v1_list_addon_registry_response import V1ListAddonRegistryResponse
from vela_client.models.v1_list_addon_response import V1ListAddonResponse
from vela_client.models.v1_list_application_env_binding import V1ListApplicationEnvBinding
from vela_client.models.v1_list_application_policy import V1ListApplicationPolicy
from vela_client.models.v1_list_application_response import V1ListApplicationResponse
from vela_client.models.v1_list_application_trigger_response import V1ListApplicationTriggerResponse
from vela_client.models.v1_list_cloud_cluster_creation_response import V1ListCloudClusterCreationResponse
from vela_client.models.v1_list_cloud_cluster_response import V1ListCloudClusterResponse
from vela_client.models.v1_list_cluster_response import V1ListClusterResponse
from vela_client.models.v1_list_config_distribution_response import V1ListConfigDistributionResponse
from vela_client.models.v1_list_config_response import V1ListConfigResponse
from vela_client.models.v1_list_config_template_response import V1ListConfigTemplateResponse
from vela_client.models.v1_list_context_value_response import V1ListContextValueResponse
from vela_client.models.v1_list_definition_response import V1ListDefinitionResponse
from vela_client.models.v1_list_enabled_addon_response import V1ListEnabledAddonResponse
from vela_client.models.v1_list_env_response import V1ListEnvResponse
from vela_client.models.v1_list_image_registry_response import V1ListImageRegistryResponse
from vela_client.models.v1_list_pipeline_response import V1ListPipelineResponse
from vela_client.models.v1_list_pipeline_run_response import V1ListPipelineRunResponse
from vela_client.models.v1_list_project_response import V1ListProjectResponse
from vela_client.models.v1_list_project_users_response import V1ListProjectUsersResponse
from vela_client.models.v1_list_revisions_response import V1ListRevisionsResponse
from vela_client.models.v1_list_roles_response import V1ListRolesResponse
from vela_client.models.v1_list_target_response import V1ListTargetResponse
from vela_client.models.v1_list_terraform_provider_response import V1ListTerraformProviderResponse
from vela_client.models.v1_list_user_response import V1ListUserResponse
from vela_client.models.v1_list_workflow_records_response import V1ListWorkflowRecordsResponse
from vela_client.models.v1_list_workflow_response import V1ListWorkflowResponse
from vela_client.models.v1_login_request import V1LoginRequest
from vela_client.models.v1_login_response import V1LoginResponse
from vela_client.models.v1_login_user_info_response import V1LoginUserInfoResponse
from vela_client.models.v1_manifest import V1Manifest
from vela_client.models.v1_name_alias import V1NameAlias
from vela_client.models.v1_namespaced_name import V1NamespacedName
from vela_client.models.v1_object_reference import V1ObjectReference
from vela_client.models.v1_output_var import V1OutputVar
from vela_client.models.v1_permission_base import V1PermissionBase
from vela_client.models.v1_pipeline_base import V1PipelineBase
from vela_client.models.v1_pipeline_info import V1PipelineInfo
from vela_client.models.v1_pipeline_list_item import V1PipelineListItem
from vela_client.models.v1_pipeline_meta import V1PipelineMeta
from vela_client.models.v1_pipeline_meta_response import V1PipelineMetaResponse
from vela_client.models.v1_pipeline_run import V1PipelineRun
from vela_client.models.v1_pipeline_run_base import V1PipelineRunBase
from vela_client.models.v1_pipeline_run_briefing import V1PipelineRunBriefing
from vela_client.models.v1_pipeline_run_meta import V1PipelineRunMeta
from vela_client.models.v1_platform import V1Platform
from vela_client.models.v1_policy_base import V1PolicyBase
from vela_client.models.v1_project_base import V1ProjectBase
from vela_client.models.v1_project_user_base import V1ProjectUserBase
from vela_client.models.v1_put_application_env_binding_request import V1PutApplicationEnvBindingRequest
from vela_client.models.v1_refresh_token_response import V1RefreshTokenResponse
from vela_client.models.v1_role_base import V1RoleBase
from vela_client.models.v1_root_fs import V1RootFS
from vela_client.models.v1_run_pipeline_request import V1RunPipelineRequest
from vela_client.models.v1_run_stat import V1RunStat
from vela_client.models.v1_run_stat_info import V1RunStatInfo
from vela_client.models.v1_simple_response import V1SimpleResponse
from vela_client.models.v1_statistic_info import V1StatisticInfo
from vela_client.models.v1_step_base import V1StepBase
from vela_client.models.v1_step_input_base import V1StepInputBase
from vela_client.models.v1_step_output_base import V1StepOutputBase
from vela_client.models.v1_system_info import V1SystemInfo
from vela_client.models.v1_system_info_request import V1SystemInfoRequest
from vela_client.models.v1_system_info_response import V1SystemInfoResponse
from vela_client.models.v1_system_version import V1SystemVersion
from vela_client.models.v1_target_base import V1TargetBase
from vela_client.models.v1_terraform_provider import V1TerraformProvider
from vela_client.models.v1_update_addon_registry_request import V1UpdateAddonRegistryRequest
from vela_client.models.v1_update_application_component_request import V1UpdateApplicationComponentRequest
from vela_client.models.v1_update_application_component_request_labels import V1UpdateApplicationComponentRequestLabels
from vela_client.models.v1_update_application_request import V1UpdateApplicationRequest
from vela_client.models.v1_update_application_trait_request import V1UpdateApplicationTraitRequest
from vela_client.models.v1_update_config_request import V1UpdateConfigRequest
from vela_client.models.v1_update_context_values_request import V1UpdateContextValuesRequest
from vela_client.models.v1_update_definition_status_request import V1UpdateDefinitionStatusRequest
from vela_client.models.v1_update_pipeline_request import V1UpdatePipelineRequest
from vela_client.models.v1_update_policy_request import V1UpdatePolicyRequest
from vela_client.models.v1_update_project_request import V1UpdateProjectRequest
from vela_client.models.v1_update_project_user_request import V1UpdateProjectUserRequest
from vela_client.models.v1_update_role_request import V1UpdateRoleRequest
from vela_client.models.v1_update_target_request import V1UpdateTargetRequest
from vela_client.models.v1_update_ui_schema_request import V1UpdateUISchemaRequest
from vela_client.models.v1_update_user_request import V1UpdateUserRequest
from vela_client.models.v1_update_workflow_request import V1UpdateWorkflowRequest
from vela_client.models.v1_user_base import V1UserBase
from vela_client.models.v1_vela_ql_view_response import V1VelaQLViewResponse
from vela_client.models.v1_workflow_base import V1WorkflowBase
from vela_client.models.v1_workflow_policy_binding import V1WorkflowPolicyBinding
from vela_client.models.v1_workflow_record import V1WorkflowRecord
from vela_client.models.v1_workflow_step import V1WorkflowStep
from vela_client.models.v1_workflow_step_base import V1WorkflowStepBase
from vela_client.models.v1alpha1_input_item import V1alpha1InputItem
from vela_client.models.v1alpha1_output_item import V1alpha1OutputItem
from vela_client.models.v1alpha1_step_status import V1alpha1StepStatus
from vela_client.models.v1alpha1_workflow_execute_mode import V1alpha1WorkflowExecuteMode
from vela_client.models.v1alpha1_workflow_run_spec import V1alpha1WorkflowRunSpec
from vela_client.models.v1alpha1_workflow_run_status import V1alpha1WorkflowRunStatus
from vela_client.models.v1alpha1_workflow_spec import V1alpha1WorkflowSpec
from vela_client.models.v1alpha1_workflow_step import V1alpha1WorkflowStep
from vela_client.models.v1alpha1_workflow_step_base import V1alpha1WorkflowStepBase
from vela_client.models.v1alpha1_workflow_step_meta import V1alpha1WorkflowStepMeta
from vela_client.models.v1alpha1_workflow_step_status import V1alpha1WorkflowStepStatus
from vela_client.models.v1beta1_app_policy import V1beta1AppPolicy
from vela_client.models.v1beta1_application_spec import V1beta1ApplicationSpec
from vela_client.models.v1beta1_component_definition_spec import V1beta1ComponentDefinitionSpec
from vela_client.models.v1beta1_policy_definition_spec import V1beta1PolicyDefinitionSpec
from vela_client.models.v1beta1_trait_definition_spec import V1beta1TraitDefinitionSpec
from vela_client.models.v1beta1_workflow import V1beta1Workflow
from vela_client.models.v1beta1_workflow_step_definition_spec import V1beta1WorkflowStepDefinitionSpec
