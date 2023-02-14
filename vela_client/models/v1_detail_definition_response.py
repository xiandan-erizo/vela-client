# coding: utf-8

"""
    Kubevela api doc

    Kubevela api doc  # noqa: E501

    OpenAPI spec version: v1beta1
    Contact: feedback@mail.kubevela.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1DetailDefinitionResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alias': 'str',
        'component': 'V1beta1ComponentDefinitionSpec',
        'description': 'str',
        'icon': 'str',
        'labels': 'dict(str, str)',
        'name': 'str',
        'owner_addon': 'str',
        'policy': 'V1beta1PolicyDefinitionSpec',
        'schema': 'str',
        'status': 'str',
        'trait': 'V1beta1TraitDefinitionSpec',
        'ui_schema': 'list[UtilsUIParameter]',
        'workflow_step': 'V1beta1WorkflowStepDefinitionSpec',
        'workload_type': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'component': 'component',
        'description': 'description',
        'icon': 'icon',
        'labels': 'labels',
        'name': 'name',
        'owner_addon': 'ownerAddon',
        'policy': 'policy',
        'schema': 'schema',
        'status': 'status',
        'trait': 'trait',
        'ui_schema': 'uiSchema',
        'workflow_step': 'workflowStep',
        'workload_type': 'workloadType'
    }

    def __init__(self, alias=None, component=None, description=None, icon=None, labels=None, name=None, owner_addon=None, policy=None, schema=None, status=None, trait=None, ui_schema=None, workflow_step=None, workload_type=None):  # noqa: E501
        """V1DetailDefinitionResponse - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._component = None
        self._description = None
        self._icon = None
        self._labels = None
        self._name = None
        self._owner_addon = None
        self._policy = None
        self._schema = None
        self._status = None
        self._trait = None
        self._ui_schema = None
        self._workflow_step = None
        self._workload_type = None
        self.discriminator = None
        self.alias = alias
        if component is not None:
            self.component = component
        self.description = description
        self.icon = icon
        self.labels = labels
        self.name = name
        self.owner_addon = owner_addon
        if policy is not None:
            self.policy = policy
        self.schema = schema
        self.status = status
        if trait is not None:
            self.trait = trait
        self.ui_schema = ui_schema
        if workflow_step is not None:
            self.workflow_step = workflow_step
        if workload_type is not None:
            self.workload_type = workload_type

    @property
    def alias(self):
        """Gets the alias of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The alias of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1DetailDefinitionResponse.


        :param alias: The alias of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def component(self):
        """Gets the component of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The component of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: V1beta1ComponentDefinitionSpec
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this V1DetailDefinitionResponse.


        :param component: The component of this V1DetailDefinitionResponse.  # noqa: E501
        :type: V1beta1ComponentDefinitionSpec
        """

        self._component = component

    @property
    def description(self):
        """Gets the description of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The description of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1DetailDefinitionResponse.


        :param description: The description of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The icon of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this V1DetailDefinitionResponse.


        :param icon: The icon of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """
        if icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def labels(self):
        """Gets the labels of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The labels of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1DetailDefinitionResponse.


        :param labels: The labels of this V1DetailDefinitionResponse.  # noqa: E501
        :type: dict(str, str)
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The name of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1DetailDefinitionResponse.


        :param name: The name of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner_addon(self):
        """Gets the owner_addon of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The owner_addon of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._owner_addon

    @owner_addon.setter
    def owner_addon(self, owner_addon):
        """Sets the owner_addon of this V1DetailDefinitionResponse.


        :param owner_addon: The owner_addon of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """
        if owner_addon is None:
            raise ValueError("Invalid value for `owner_addon`, must not be `None`")  # noqa: E501

        self._owner_addon = owner_addon

    @property
    def policy(self):
        """Gets the policy of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The policy of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: V1beta1PolicyDefinitionSpec
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this V1DetailDefinitionResponse.


        :param policy: The policy of this V1DetailDefinitionResponse.  # noqa: E501
        :type: V1beta1PolicyDefinitionSpec
        """

        self._policy = policy

    @property
    def schema(self):
        """Gets the schema of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The schema of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this V1DetailDefinitionResponse.


        :param schema: The schema of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """
        if schema is None:
            raise ValueError("Invalid value for `schema`, must not be `None`")  # noqa: E501

        self._schema = schema

    @property
    def status(self):
        """Gets the status of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The status of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1DetailDefinitionResponse.


        :param status: The status of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def trait(self):
        """Gets the trait of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The trait of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: V1beta1TraitDefinitionSpec
        """
        return self._trait

    @trait.setter
    def trait(self, trait):
        """Sets the trait of this V1DetailDefinitionResponse.


        :param trait: The trait of this V1DetailDefinitionResponse.  # noqa: E501
        :type: V1beta1TraitDefinitionSpec
        """

        self._trait = trait

    @property
    def ui_schema(self):
        """Gets the ui_schema of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The ui_schema of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: list[UtilsUIParameter]
        """
        return self._ui_schema

    @ui_schema.setter
    def ui_schema(self, ui_schema):
        """Sets the ui_schema of this V1DetailDefinitionResponse.


        :param ui_schema: The ui_schema of this V1DetailDefinitionResponse.  # noqa: E501
        :type: list[UtilsUIParameter]
        """
        if ui_schema is None:
            raise ValueError("Invalid value for `ui_schema`, must not be `None`")  # noqa: E501

        self._ui_schema = ui_schema

    @property
    def workflow_step(self):
        """Gets the workflow_step of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The workflow_step of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: V1beta1WorkflowStepDefinitionSpec
        """
        return self._workflow_step

    @workflow_step.setter
    def workflow_step(self, workflow_step):
        """Sets the workflow_step of this V1DetailDefinitionResponse.


        :param workflow_step: The workflow_step of this V1DetailDefinitionResponse.  # noqa: E501
        :type: V1beta1WorkflowStepDefinitionSpec
        """

        self._workflow_step = workflow_step

    @property
    def workload_type(self):
        """Gets the workload_type of this V1DetailDefinitionResponse.  # noqa: E501


        :return: The workload_type of this V1DetailDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """Sets the workload_type of this V1DetailDefinitionResponse.


        :param workload_type: The workload_type of this V1DetailDefinitionResponse.  # noqa: E501
        :type: str
        """

        self._workload_type = workload_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1DetailDefinitionResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1DetailDefinitionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other