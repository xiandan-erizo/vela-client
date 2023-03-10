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

class V1ListProjectResponse(object):
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
        'projects': 'list[V1ProjectBase]',
        'total': 'int'
    }

    attribute_map = {
        'projects': 'projects',
        'total': 'total'
    }

    def __init__(self, projects=None, total=None):  # noqa: E501
        """V1ListProjectResponse - a model defined in Swagger"""  # noqa: E501
        self._projects = None
        self._total = None
        self.discriminator = None
        self.projects = projects
        self.total = total

    @property
    def projects(self):
        """Gets the projects of this V1ListProjectResponse.  # noqa: E501


        :return: The projects of this V1ListProjectResponse.  # noqa: E501
        :rtype: list[V1ProjectBase]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this V1ListProjectResponse.


        :param projects: The projects of this V1ListProjectResponse.  # noqa: E501
        :type: list[V1ProjectBase]
        """
        if projects is None:
            raise ValueError("Invalid value for `projects`, must not be `None`")  # noqa: E501

        self._projects = projects

    @property
    def total(self):
        """Gets the total of this V1ListProjectResponse.  # noqa: E501


        :return: The total of this V1ListProjectResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this V1ListProjectResponse.


        :param total: The total of this V1ListProjectResponse.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if issubclass(V1ListProjectResponse, dict):
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
        if not isinstance(other, V1ListProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
