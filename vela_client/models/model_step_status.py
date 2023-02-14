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

class ModelStepStatus(object):
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
        'first_execute_time': 'datetime',
        'id': 'str',
        'last_execute_time': 'datetime',
        'message': 'str',
        'name': 'str',
        'phase': 'str',
        'reason': 'str',
        'type': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'first_execute_time': 'firstExecuteTime',
        'id': 'id',
        'last_execute_time': 'lastExecuteTime',
        'message': 'message',
        'name': 'name',
        'phase': 'phase',
        'reason': 'reason',
        'type': 'type'
    }

    def __init__(self, alias=None, first_execute_time=None, id=None, last_execute_time=None, message=None, name=None, phase=None, reason=None, type=None):  # noqa: E501
        """ModelStepStatus - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._first_execute_time = None
        self._id = None
        self._last_execute_time = None
        self._message = None
        self._name = None
        self._phase = None
        self._reason = None
        self._type = None
        self.discriminator = None
        self.alias = alias
        if first_execute_time is not None:
            self.first_execute_time = first_execute_time
        self.id = id
        if last_execute_time is not None:
            self.last_execute_time = last_execute_time
        if message is not None:
            self.message = message
        self.name = name
        if phase is not None:
            self.phase = phase
        if reason is not None:
            self.reason = reason
        if type is not None:
            self.type = type

    @property
    def alias(self):
        """Gets the alias of this ModelStepStatus.  # noqa: E501


        :return: The alias of this ModelStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ModelStepStatus.


        :param alias: The alias of this ModelStepStatus.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def first_execute_time(self):
        """Gets the first_execute_time of this ModelStepStatus.  # noqa: E501


        :return: The first_execute_time of this ModelStepStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._first_execute_time

    @first_execute_time.setter
    def first_execute_time(self, first_execute_time):
        """Sets the first_execute_time of this ModelStepStatus.


        :param first_execute_time: The first_execute_time of this ModelStepStatus.  # noqa: E501
        :type: datetime
        """

        self._first_execute_time = first_execute_time

    @property
    def id(self):
        """Gets the id of this ModelStepStatus.  # noqa: E501


        :return: The id of this ModelStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelStepStatus.


        :param id: The id of this ModelStepStatus.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_execute_time(self):
        """Gets the last_execute_time of this ModelStepStatus.  # noqa: E501


        :return: The last_execute_time of this ModelStepStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_execute_time

    @last_execute_time.setter
    def last_execute_time(self, last_execute_time):
        """Sets the last_execute_time of this ModelStepStatus.


        :param last_execute_time: The last_execute_time of this ModelStepStatus.  # noqa: E501
        :type: datetime
        """

        self._last_execute_time = last_execute_time

    @property
    def message(self):
        """Gets the message of this ModelStepStatus.  # noqa: E501


        :return: The message of this ModelStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ModelStepStatus.


        :param message: The message of this ModelStepStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this ModelStepStatus.  # noqa: E501


        :return: The name of this ModelStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelStepStatus.


        :param name: The name of this ModelStepStatus.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def phase(self):
        """Gets the phase of this ModelStepStatus.  # noqa: E501


        :return: The phase of this ModelStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this ModelStepStatus.


        :param phase: The phase of this ModelStepStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this ModelStepStatus.  # noqa: E501


        :return: The reason of this ModelStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ModelStepStatus.


        :param reason: The reason of this ModelStepStatus.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def type(self):
        """Gets the type of this ModelStepStatus.  # noqa: E501


        :return: The type of this ModelStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelStepStatus.


        :param type: The type of this ModelStepStatus.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ModelStepStatus, dict):
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
        if not isinstance(other, ModelStepStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
