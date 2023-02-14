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

class UtilsStyle(object):
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
        'col_span': 'int'
    }

    attribute_map = {
        'col_span': 'colSpan'
    }

    def __init__(self, col_span=None):  # noqa: E501
        """UtilsStyle - a model defined in Swagger"""  # noqa: E501
        self._col_span = None
        self.discriminator = None
        self.col_span = col_span

    @property
    def col_span(self):
        """Gets the col_span of this UtilsStyle.  # noqa: E501


        :return: The col_span of this UtilsStyle.  # noqa: E501
        :rtype: int
        """
        return self._col_span

    @col_span.setter
    def col_span(self, col_span):
        """Sets the col_span of this UtilsStyle.


        :param col_span: The col_span of this UtilsStyle.  # noqa: E501
        :type: int
        """
        if col_span is None:
            raise ValueError("Invalid value for `col_span`, must not be `None`")  # noqa: E501

        self._col_span = col_span

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
        if issubclass(UtilsStyle, dict):
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
        if not isinstance(other, UtilsStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
