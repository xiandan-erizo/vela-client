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

class V1CreateWorkflowRequest(object):
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
        'default': 'bool',
        'description': 'str',
        'env_name': 'str',
        'mode': 'str',
        'name': 'str',
        'steps': 'list[V1WorkflowStep]',
        'sub_mode': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'default': 'default',
        'description': 'description',
        'env_name': 'envName',
        'mode': 'mode',
        'name': 'name',
        'steps': 'steps',
        'sub_mode': 'subMode'
    }

    def __init__(self, alias=None, default=None, description=None, env_name=None, mode=None, name=None, steps=None, sub_mode=None):  # noqa: E501
        """V1CreateWorkflowRequest - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._default = None
        self._description = None
        self._env_name = None
        self._mode = None
        self._name = None
        self._steps = None
        self._sub_mode = None
        self.discriminator = None
        if alias is not None:
            self.alias = alias
        self.default = default
        if description is not None:
            self.description = description
        self.env_name = env_name
        self.mode = mode
        self.name = name
        if steps is not None:
            self.steps = steps
        self.sub_mode = sub_mode

    @property
    def alias(self):
        """Gets the alias of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The alias of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1CreateWorkflowRequest.


        :param alias: The alias of this V1CreateWorkflowRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def default(self):
        """Gets the default of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The default of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V1CreateWorkflowRequest.


        :param default: The default of this V1CreateWorkflowRequest.  # noqa: E501
        :type: bool
        """
        if default is None:
            raise ValueError("Invalid value for `default`, must not be `None`")  # noqa: E501

        self._default = default

    @property
    def description(self):
        """Gets the description of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The description of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1CreateWorkflowRequest.


        :param description: The description of this V1CreateWorkflowRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def env_name(self):
        """Gets the env_name of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The env_name of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this V1CreateWorkflowRequest.


        :param env_name: The env_name of this V1CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        if env_name is None:
            raise ValueError("Invalid value for `env_name`, must not be `None`")  # noqa: E501

        self._env_name = env_name

    @property
    def mode(self):
        """Gets the mode of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The mode of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this V1CreateWorkflowRequest.


        :param mode: The mode of this V1CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def name(self):
        """Gets the name of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The name of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CreateWorkflowRequest.


        :param name: The name of this V1CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def steps(self):
        """Gets the steps of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The steps of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: list[V1WorkflowStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this V1CreateWorkflowRequest.


        :param steps: The steps of this V1CreateWorkflowRequest.  # noqa: E501
        :type: list[V1WorkflowStep]
        """

        self._steps = steps

    @property
    def sub_mode(self):
        """Gets the sub_mode of this V1CreateWorkflowRequest.  # noqa: E501


        :return: The sub_mode of this V1CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_mode

    @sub_mode.setter
    def sub_mode(self, sub_mode):
        """Sets the sub_mode of this V1CreateWorkflowRequest.


        :param sub_mode: The sub_mode of this V1CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        if sub_mode is None:
            raise ValueError("Invalid value for `sub_mode`, must not be `None`")  # noqa: E501

        self._sub_mode = sub_mode

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
        if issubclass(V1CreateWorkflowRequest, dict):
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
        if not isinstance(other, V1CreateWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
