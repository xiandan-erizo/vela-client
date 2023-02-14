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

class V1CreateContextValuesRequest(object):
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
        'name': 'str',
        'values': 'list[ModelValue]'
    }

    attribute_map = {
        'name': 'name',
        'values': 'values'
    }

    def __init__(self, name=None, values=None):  # noqa: E501
        """V1CreateContextValuesRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._values = None
        self.discriminator = None
        self.name = name
        self.values = values

    @property
    def name(self):
        """Gets the name of this V1CreateContextValuesRequest.  # noqa: E501


        :return: The name of this V1CreateContextValuesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CreateContextValuesRequest.


        :param name: The name of this V1CreateContextValuesRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def values(self):
        """Gets the values of this V1CreateContextValuesRequest.  # noqa: E501


        :return: The values of this V1CreateContextValuesRequest.  # noqa: E501
        :rtype: list[ModelValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1CreateContextValuesRequest.


        :param values: The values of this V1CreateContextValuesRequest.  # noqa: E501
        :type: list[ModelValue]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

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
        if issubclass(V1CreateContextValuesRequest, dict):
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
        if not isinstance(other, V1CreateContextValuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
