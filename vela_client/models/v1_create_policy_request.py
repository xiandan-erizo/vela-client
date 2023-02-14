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

class V1CreatePolicyRequest(object):
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
        'description': 'str',
        'env_name': 'str',
        'name': 'str',
        'properties': 'str',
        'type': 'str',
        'workflow_policy_bind': 'list[V1WorkflowPolicyBinding]'
    }

    attribute_map = {
        'alias': 'alias',
        'description': 'description',
        'env_name': 'envName',
        'name': 'name',
        'properties': 'properties',
        'type': 'type',
        'workflow_policy_bind': 'workflowPolicyBind'
    }

    def __init__(self, alias=None, description=None, env_name=None, name=None, properties=None, type=None, workflow_policy_bind=None):  # noqa: E501
        """V1CreatePolicyRequest - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._description = None
        self._env_name = None
        self._name = None
        self._properties = None
        self._type = None
        self._workflow_policy_bind = None
        self.discriminator = None
        self.alias = alias
        self.description = description
        self.env_name = env_name
        self.name = name
        self.properties = properties
        self.type = type
        self.workflow_policy_bind = workflow_policy_bind

    @property
    def alias(self):
        """Gets the alias of this V1CreatePolicyRequest.  # noqa: E501


        :return: The alias of this V1CreatePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1CreatePolicyRequest.


        :param alias: The alias of this V1CreatePolicyRequest.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def description(self):
        """Gets the description of this V1CreatePolicyRequest.  # noqa: E501


        :return: The description of this V1CreatePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1CreatePolicyRequest.


        :param description: The description of this V1CreatePolicyRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def env_name(self):
        """Gets the env_name of this V1CreatePolicyRequest.  # noqa: E501


        :return: The env_name of this V1CreatePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this V1CreatePolicyRequest.


        :param env_name: The env_name of this V1CreatePolicyRequest.  # noqa: E501
        :type: str
        """
        if env_name is None:
            raise ValueError("Invalid value for `env_name`, must not be `None`")  # noqa: E501

        self._env_name = env_name

    @property
    def name(self):
        """Gets the name of this V1CreatePolicyRequest.  # noqa: E501


        :return: The name of this V1CreatePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CreatePolicyRequest.


        :param name: The name of this V1CreatePolicyRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this V1CreatePolicyRequest.  # noqa: E501


        :return: The properties of this V1CreatePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V1CreatePolicyRequest.


        :param properties: The properties of this V1CreatePolicyRequest.  # noqa: E501
        :type: str
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this V1CreatePolicyRequest.  # noqa: E501


        :return: The type of this V1CreatePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1CreatePolicyRequest.


        :param type: The type of this V1CreatePolicyRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def workflow_policy_bind(self):
        """Gets the workflow_policy_bind of this V1CreatePolicyRequest.  # noqa: E501


        :return: The workflow_policy_bind of this V1CreatePolicyRequest.  # noqa: E501
        :rtype: list[V1WorkflowPolicyBinding]
        """
        return self._workflow_policy_bind

    @workflow_policy_bind.setter
    def workflow_policy_bind(self, workflow_policy_bind):
        """Sets the workflow_policy_bind of this V1CreatePolicyRequest.


        :param workflow_policy_bind: The workflow_policy_bind of this V1CreatePolicyRequest.  # noqa: E501
        :type: list[V1WorkflowPolicyBinding]
        """
        if workflow_policy_bind is None:
            raise ValueError("Invalid value for `workflow_policy_bind`, must not be `None`")  # noqa: E501

        self._workflow_policy_bind = workflow_policy_bind

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
        if issubclass(V1CreatePolicyRequest, dict):
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
        if not isinstance(other, V1CreatePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
