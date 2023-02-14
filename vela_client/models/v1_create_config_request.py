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

class V1CreateConfigRequest(object):
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
        'name': 'str',
        'properties': 'str',
        'template': 'V1NamespacedName'
    }

    attribute_map = {
        'alias': 'alias',
        'description': 'description',
        'name': 'name',
        'properties': 'properties',
        'template': 'template'
    }

    def __init__(self, alias=None, description=None, name=None, properties=None, template=None):  # noqa: E501
        """V1CreateConfigRequest - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._description = None
        self._name = None
        self._properties = None
        self._template = None
        self.discriminator = None
        self.alias = alias
        self.description = description
        self.name = name
        if properties is not None:
            self.properties = properties
        self.template = template

    @property
    def alias(self):
        """Gets the alias of this V1CreateConfigRequest.  # noqa: E501


        :return: The alias of this V1CreateConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1CreateConfigRequest.


        :param alias: The alias of this V1CreateConfigRequest.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def description(self):
        """Gets the description of this V1CreateConfigRequest.  # noqa: E501


        :return: The description of this V1CreateConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1CreateConfigRequest.


        :param description: The description of this V1CreateConfigRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this V1CreateConfigRequest.  # noqa: E501


        :return: The name of this V1CreateConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CreateConfigRequest.


        :param name: The name of this V1CreateConfigRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this V1CreateConfigRequest.  # noqa: E501


        :return: The properties of this V1CreateConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V1CreateConfigRequest.


        :param properties: The properties of this V1CreateConfigRequest.  # noqa: E501
        :type: str
        """

        self._properties = properties

    @property
    def template(self):
        """Gets the template of this V1CreateConfigRequest.  # noqa: E501


        :return: The template of this V1CreateConfigRequest.  # noqa: E501
        :rtype: V1NamespacedName
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1CreateConfigRequest.


        :param template: The template of this V1CreateConfigRequest.  # noqa: E501
        :type: V1NamespacedName
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

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
        if issubclass(V1CreateConfigRequest, dict):
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
        if not isinstance(other, V1CreateConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
