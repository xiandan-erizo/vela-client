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

class V1UpdateAddonRegistryRequest(object):
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
        'git': 'AddonGitAddonSource',
        'gitee': 'AddonGiteeAddonSource',
        'gitlab': 'AddonGitlabAddonSource',
        'helm': 'AddonHelmSource',
        'oss': 'AddonOSSAddonSource'
    }

    attribute_map = {
        'git': 'git',
        'gitee': 'gitee',
        'gitlab': 'gitlab',
        'helm': 'helm',
        'oss': 'oss'
    }

    def __init__(self, git=None, gitee=None, gitlab=None, helm=None, oss=None):  # noqa: E501
        """V1UpdateAddonRegistryRequest - a model defined in Swagger"""  # noqa: E501
        self._git = None
        self._gitee = None
        self._gitlab = None
        self._helm = None
        self._oss = None
        self.discriminator = None
        if git is not None:
            self.git = git
        if gitee is not None:
            self.gitee = gitee
        if gitlab is not None:
            self.gitlab = gitlab
        if helm is not None:
            self.helm = helm
        if oss is not None:
            self.oss = oss

    @property
    def git(self):
        """Gets the git of this V1UpdateAddonRegistryRequest.  # noqa: E501


        :return: The git of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :rtype: AddonGitAddonSource
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this V1UpdateAddonRegistryRequest.


        :param git: The git of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :type: AddonGitAddonSource
        """

        self._git = git

    @property
    def gitee(self):
        """Gets the gitee of this V1UpdateAddonRegistryRequest.  # noqa: E501


        :return: The gitee of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :rtype: AddonGiteeAddonSource
        """
        return self._gitee

    @gitee.setter
    def gitee(self, gitee):
        """Sets the gitee of this V1UpdateAddonRegistryRequest.


        :param gitee: The gitee of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :type: AddonGiteeAddonSource
        """

        self._gitee = gitee

    @property
    def gitlab(self):
        """Gets the gitlab of this V1UpdateAddonRegistryRequest.  # noqa: E501


        :return: The gitlab of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :rtype: AddonGitlabAddonSource
        """
        return self._gitlab

    @gitlab.setter
    def gitlab(self, gitlab):
        """Sets the gitlab of this V1UpdateAddonRegistryRequest.


        :param gitlab: The gitlab of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :type: AddonGitlabAddonSource
        """

        self._gitlab = gitlab

    @property
    def helm(self):
        """Gets the helm of this V1UpdateAddonRegistryRequest.  # noqa: E501


        :return: The helm of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :rtype: AddonHelmSource
        """
        return self._helm

    @helm.setter
    def helm(self, helm):
        """Sets the helm of this V1UpdateAddonRegistryRequest.


        :param helm: The helm of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :type: AddonHelmSource
        """

        self._helm = helm

    @property
    def oss(self):
        """Gets the oss of this V1UpdateAddonRegistryRequest.  # noqa: E501


        :return: The oss of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :rtype: AddonOSSAddonSource
        """
        return self._oss

    @oss.setter
    def oss(self, oss):
        """Sets the oss of this V1UpdateAddonRegistryRequest.


        :param oss: The oss of this V1UpdateAddonRegistryRequest.  # noqa: E501
        :type: AddonOSSAddonSource
        """

        self._oss = oss

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
        if issubclass(V1UpdateAddonRegistryRequest, dict):
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
        if not isinstance(other, V1UpdateAddonRegistryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
