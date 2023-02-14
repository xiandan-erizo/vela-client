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

class V1AddonInfo(object):
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
        'meta': 'AddonMeta',
        'registry_name': 'str'
    }

    attribute_map = {
        'meta': 'Meta',
        'registry_name': 'registryName'
    }

    def __init__(self, meta=None, registry_name=None):  # noqa: E501
        """V1AddonInfo - a model defined in Swagger"""  # noqa: E501
        self._meta = None
        self._registry_name = None
        self.discriminator = None
        self.meta = meta
        self.registry_name = registry_name

    @property
    def meta(self):
        """Gets the meta of this V1AddonInfo.  # noqa: E501


        :return: The meta of this V1AddonInfo.  # noqa: E501
        :rtype: AddonMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this V1AddonInfo.


        :param meta: The meta of this V1AddonInfo.  # noqa: E501
        :type: AddonMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def registry_name(self):
        """Gets the registry_name of this V1AddonInfo.  # noqa: E501


        :return: The registry_name of this V1AddonInfo.  # noqa: E501
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        """Sets the registry_name of this V1AddonInfo.


        :param registry_name: The registry_name of this V1AddonInfo.  # noqa: E501
        :type: str
        """
        if registry_name is None:
            raise ValueError("Invalid value for `registry_name`, must not be `None`")  # noqa: E501

        self._registry_name = registry_name

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
        if issubclass(V1AddonInfo, dict):
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
        if not isinstance(other, V1AddonInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
