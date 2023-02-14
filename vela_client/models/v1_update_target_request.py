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

class V1UpdateTargetRequest(object):
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
        'variable': 'object'
    }

    attribute_map = {
        'alias': 'alias',
        'description': 'description',
        'variable': 'variable'
    }

    def __init__(self, alias=None, description=None, variable=None):  # noqa: E501
        """V1UpdateTargetRequest - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._description = None
        self._variable = None
        self.discriminator = None
        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description
        if variable is not None:
            self.variable = variable

    @property
    def alias(self):
        """Gets the alias of this V1UpdateTargetRequest.  # noqa: E501


        :return: The alias of this V1UpdateTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1UpdateTargetRequest.


        :param alias: The alias of this V1UpdateTargetRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def description(self):
        """Gets the description of this V1UpdateTargetRequest.  # noqa: E501


        :return: The description of this V1UpdateTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1UpdateTargetRequest.


        :param description: The description of this V1UpdateTargetRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def variable(self):
        """Gets the variable of this V1UpdateTargetRequest.  # noqa: E501


        :return: The variable of this V1UpdateTargetRequest.  # noqa: E501
        :rtype: object
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this V1UpdateTargetRequest.


        :param variable: The variable of this V1UpdateTargetRequest.  # noqa: E501
        :type: object
        """

        self._variable = variable

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
        if issubclass(V1UpdateTargetRequest, dict):
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
        if not isinstance(other, V1UpdateTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other