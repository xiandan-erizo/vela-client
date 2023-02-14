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

class V1ListTerraformProviderResponse(object):
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
        'providers': 'list[V1TerraformProvider]'
    }

    attribute_map = {
        'providers': 'providers'
    }

    def __init__(self, providers=None):  # noqa: E501
        """V1ListTerraformProviderResponse - a model defined in Swagger"""  # noqa: E501
        self._providers = None
        self.discriminator = None
        self.providers = providers

    @property
    def providers(self):
        """Gets the providers of this V1ListTerraformProviderResponse.  # noqa: E501


        :return: The providers of this V1ListTerraformProviderResponse.  # noqa: E501
        :rtype: list[V1TerraformProvider]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this V1ListTerraformProviderResponse.


        :param providers: The providers of this V1ListTerraformProviderResponse.  # noqa: E501
        :type: list[V1TerraformProvider]
        """
        if providers is None:
            raise ValueError("Invalid value for `providers`, must not be `None`")  # noqa: E501

        self._providers = providers

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
        if issubclass(V1ListTerraformProviderResponse, dict):
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
        if not isinstance(other, V1ListTerraformProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
