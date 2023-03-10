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

class BcodeBcode(object):
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
        'business_code': 'int',
        'message': 'str'
    }

    attribute_map = {
        'business_code': 'BusinessCode',
        'message': 'Message'
    }

    def __init__(self, business_code=None, message=None):  # noqa: E501
        """BcodeBcode - a model defined in Swagger"""  # noqa: E501
        self._business_code = None
        self._message = None
        self.discriminator = None
        self.business_code = business_code
        self.message = message

    @property
    def business_code(self):
        """Gets the business_code of this BcodeBcode.  # noqa: E501


        :return: The business_code of this BcodeBcode.  # noqa: E501
        :rtype: int
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        """Sets the business_code of this BcodeBcode.


        :param business_code: The business_code of this BcodeBcode.  # noqa: E501
        :type: int
        """
        if business_code is None:
            raise ValueError("Invalid value for `business_code`, must not be `None`")  # noqa: E501

        self._business_code = business_code

    @property
    def message(self):
        """Gets the message of this BcodeBcode.  # noqa: E501


        :return: The message of this BcodeBcode.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BcodeBcode.


        :param message: The message of this BcodeBcode.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if issubclass(BcodeBcode, dict):
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
        if not isinstance(other, BcodeBcode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
