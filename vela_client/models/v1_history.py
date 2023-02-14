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

class V1History(object):
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
        'author': 'str',
        'comment': 'str',
        'created': 'str',
        'created_by': 'str',
        'empty_layer': 'bool'
    }

    attribute_map = {
        'author': 'author',
        'comment': 'comment',
        'created': 'created',
        'created_by': 'created_by',
        'empty_layer': 'empty_layer'
    }

    def __init__(self, author=None, comment=None, created=None, created_by=None, empty_layer=None):  # noqa: E501
        """V1History - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._comment = None
        self._created = None
        self._created_by = None
        self._empty_layer = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if comment is not None:
            self.comment = comment
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if empty_layer is not None:
            self.empty_layer = empty_layer

    @property
    def author(self):
        """Gets the author of this V1History.  # noqa: E501


        :return: The author of this V1History.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this V1History.


        :param author: The author of this V1History.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def comment(self):
        """Gets the comment of this V1History.  # noqa: E501


        :return: The comment of this V1History.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V1History.


        :param comment: The comment of this V1History.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created(self):
        """Gets the created of this V1History.  # noqa: E501


        :return: The created of this V1History.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this V1History.


        :param created: The created of this V1History.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this V1History.  # noqa: E501


        :return: The created_by of this V1History.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this V1History.


        :param created_by: The created_by of this V1History.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def empty_layer(self):
        """Gets the empty_layer of this V1History.  # noqa: E501


        :return: The empty_layer of this V1History.  # noqa: E501
        :rtype: bool
        """
        return self._empty_layer

    @empty_layer.setter
    def empty_layer(self, empty_layer):
        """Sets the empty_layer of this V1History.


        :param empty_layer: The empty_layer of this V1History.  # noqa: E501
        :type: bool
        """

        self._empty_layer = empty_layer

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
        if issubclass(V1History, dict):
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
        if not isinstance(other, V1History):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
