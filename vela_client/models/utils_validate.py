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

class UtilsValidate(object):
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
        'default_value': 'UtilsValidateDefaultValue',
        'immutable': 'bool',
        'max': 'float',
        'max_length': 'int',
        'min': 'float',
        'min_length': 'int',
        'options': 'list[UtilsOption]',
        'pattern': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'default_value': 'defaultValue',
        'immutable': 'immutable',
        'max': 'max',
        'max_length': 'maxLength',
        'min': 'min',
        'min_length': 'minLength',
        'options': 'options',
        'pattern': 'pattern',
        'required': 'required'
    }

    def __init__(self, default_value=None, immutable=None, max=None, max_length=None, min=None, min_length=None, options=None, pattern=None, required=None):  # noqa: E501
        """UtilsValidate - a model defined in Swagger"""  # noqa: E501
        self._default_value = None
        self._immutable = None
        self._max = None
        self._max_length = None
        self._min = None
        self._min_length = None
        self._options = None
        self._pattern = None
        self._required = None
        self.discriminator = None
        if default_value is not None:
            self.default_value = default_value
        self.immutable = immutable
        if max is not None:
            self.max = max
        if max_length is not None:
            self.max_length = max_length
        if min is not None:
            self.min = min
        if min_length is not None:
            self.min_length = min_length
        if options is not None:
            self.options = options
        if pattern is not None:
            self.pattern = pattern
        if required is not None:
            self.required = required

    @property
    def default_value(self):
        """Gets the default_value of this UtilsValidate.  # noqa: E501


        :return: The default_value of this UtilsValidate.  # noqa: E501
        :rtype: UtilsValidateDefaultValue
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this UtilsValidate.


        :param default_value: The default_value of this UtilsValidate.  # noqa: E501
        :type: UtilsValidateDefaultValue
        """

        self._default_value = default_value

    @property
    def immutable(self):
        """Gets the immutable of this UtilsValidate.  # noqa: E501


        :return: The immutable of this UtilsValidate.  # noqa: E501
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        """Sets the immutable of this UtilsValidate.


        :param immutable: The immutable of this UtilsValidate.  # noqa: E501
        :type: bool
        """
        if immutable is None:
            raise ValueError("Invalid value for `immutable`, must not be `None`")  # noqa: E501

        self._immutable = immutable

    @property
    def max(self):
        """Gets the max of this UtilsValidate.  # noqa: E501


        :return: The max of this UtilsValidate.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this UtilsValidate.


        :param max: The max of this UtilsValidate.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def max_length(self):
        """Gets the max_length of this UtilsValidate.  # noqa: E501


        :return: The max_length of this UtilsValidate.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this UtilsValidate.


        :param max_length: The max_length of this UtilsValidate.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def min(self):
        """Gets the min of this UtilsValidate.  # noqa: E501


        :return: The min of this UtilsValidate.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this UtilsValidate.


        :param min: The min of this UtilsValidate.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def min_length(self):
        """Gets the min_length of this UtilsValidate.  # noqa: E501


        :return: The min_length of this UtilsValidate.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this UtilsValidate.


        :param min_length: The min_length of this UtilsValidate.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def options(self):
        """Gets the options of this UtilsValidate.  # noqa: E501


        :return: The options of this UtilsValidate.  # noqa: E501
        :rtype: list[UtilsOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this UtilsValidate.


        :param options: The options of this UtilsValidate.  # noqa: E501
        :type: list[UtilsOption]
        """

        self._options = options

    @property
    def pattern(self):
        """Gets the pattern of this UtilsValidate.  # noqa: E501


        :return: The pattern of this UtilsValidate.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this UtilsValidate.


        :param pattern: The pattern of this UtilsValidate.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def required(self):
        """Gets the required of this UtilsValidate.  # noqa: E501


        :return: The required of this UtilsValidate.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this UtilsValidate.


        :param required: The required of this UtilsValidate.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(UtilsValidate, dict):
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
        if not isinstance(other, UtilsValidate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
