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

class V1SystemVersion(object):
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
        'git_version': 'str',
        'vela_version': 'str'
    }

    attribute_map = {
        'git_version': 'gitVersion',
        'vela_version': 'velaVersion'
    }

    def __init__(self, git_version=None, vela_version=None):  # noqa: E501
        """V1SystemVersion - a model defined in Swagger"""  # noqa: E501
        self._git_version = None
        self._vela_version = None
        self.discriminator = None
        self.git_version = git_version
        self.vela_version = vela_version

    @property
    def git_version(self):
        """Gets the git_version of this V1SystemVersion.  # noqa: E501


        :return: The git_version of this V1SystemVersion.  # noqa: E501
        :rtype: str
        """
        return self._git_version

    @git_version.setter
    def git_version(self, git_version):
        """Sets the git_version of this V1SystemVersion.


        :param git_version: The git_version of this V1SystemVersion.  # noqa: E501
        :type: str
        """
        if git_version is None:
            raise ValueError("Invalid value for `git_version`, must not be `None`")  # noqa: E501

        self._git_version = git_version

    @property
    def vela_version(self):
        """Gets the vela_version of this V1SystemVersion.  # noqa: E501


        :return: The vela_version of this V1SystemVersion.  # noqa: E501
        :rtype: str
        """
        return self._vela_version

    @vela_version.setter
    def vela_version(self, vela_version):
        """Sets the vela_version of this V1SystemVersion.


        :param vela_version: The vela_version of this V1SystemVersion.  # noqa: E501
        :type: str
        """
        if vela_version is None:
            raise ValueError("Invalid value for `vela_version`, must not be `None`")  # noqa: E501

        self._vela_version = vela_version

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
        if issubclass(V1SystemVersion, dict):
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
        if not isinstance(other, V1SystemVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
