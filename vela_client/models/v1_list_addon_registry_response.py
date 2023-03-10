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

class V1ListAddonRegistryResponse(object):
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
        'registries': 'list[V1AddonRegistry]'
    }

    attribute_map = {
        'registries': 'registries'
    }

    def __init__(self, registries=None):  # noqa: E501
        """V1ListAddonRegistryResponse - a model defined in Swagger"""  # noqa: E501
        self._registries = None
        self.discriminator = None
        self.registries = registries

    @property
    def registries(self):
        """Gets the registries of this V1ListAddonRegistryResponse.  # noqa: E501


        :return: The registries of this V1ListAddonRegistryResponse.  # noqa: E501
        :rtype: list[V1AddonRegistry]
        """
        return self._registries

    @registries.setter
    def registries(self, registries):
        """Sets the registries of this V1ListAddonRegistryResponse.


        :param registries: The registries of this V1ListAddonRegistryResponse.  # noqa: E501
        :type: list[V1AddonRegistry]
        """
        if registries is None:
            raise ValueError("Invalid value for `registries`, must not be `None`")  # noqa: E501

        self._registries = registries

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
        if issubclass(V1ListAddonRegistryResponse, dict):
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
        if not isinstance(other, V1ListAddonRegistryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
