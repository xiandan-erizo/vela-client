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

class V1UpdateApplicationComponentRequest(object):
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
        'depends_on': 'list[str]',
        'description': 'str',
        'icon': 'str',
        'labels': 'V1UpdateApplicationComponentRequestLabels',
        'properties': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'depends_on': 'dependsOn',
        'description': 'description',
        'icon': 'icon',
        'labels': 'labels',
        'properties': 'properties'
    }

    def __init__(self, alias=None, depends_on=None, description=None, icon=None, labels=None, properties=None):  # noqa: E501
        """V1UpdateApplicationComponentRequest - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._depends_on = None
        self._description = None
        self._icon = None
        self._labels = None
        self._properties = None
        self.discriminator = None
        if alias is not None:
            self.alias = alias
        if depends_on is not None:
            self.depends_on = depends_on
        if description is not None:
            self.description = description
        if icon is not None:
            self.icon = icon
        if labels is not None:
            self.labels = labels
        if properties is not None:
            self.properties = properties

    @property
    def alias(self):
        """Gets the alias of this V1UpdateApplicationComponentRequest.  # noqa: E501


        :return: The alias of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1UpdateApplicationComponentRequest.


        :param alias: The alias of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def depends_on(self):
        """Gets the depends_on of this V1UpdateApplicationComponentRequest.  # noqa: E501


        :return: The depends_on of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this V1UpdateApplicationComponentRequest.


        :param depends_on: The depends_on of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :type: list[str]
        """

        self._depends_on = depends_on

    @property
    def description(self):
        """Gets the description of this V1UpdateApplicationComponentRequest.  # noqa: E501


        :return: The description of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1UpdateApplicationComponentRequest.


        :param description: The description of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this V1UpdateApplicationComponentRequest.  # noqa: E501


        :return: The icon of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this V1UpdateApplicationComponentRequest.


        :param icon: The icon of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def labels(self):
        """Gets the labels of this V1UpdateApplicationComponentRequest.  # noqa: E501


        :return: The labels of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :rtype: V1UpdateApplicationComponentRequestLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1UpdateApplicationComponentRequest.


        :param labels: The labels of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :type: V1UpdateApplicationComponentRequestLabels
        """

        self._labels = labels

    @property
    def properties(self):
        """Gets the properties of this V1UpdateApplicationComponentRequest.  # noqa: E501


        :return: The properties of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V1UpdateApplicationComponentRequest.


        :param properties: The properties of this V1UpdateApplicationComponentRequest.  # noqa: E501
        :type: str
        """

        self._properties = properties

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
        if issubclass(V1UpdateApplicationComponentRequest, dict):
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
        if not isinstance(other, V1UpdateApplicationComponentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
