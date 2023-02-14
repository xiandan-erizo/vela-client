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

class V1alpha1WorkflowStepStatus(object):
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
        'first_execute_time': 'str',
        'id': 'str',
        'last_execute_time': 'str',
        'message': 'str',
        'name': 'str',
        'phase': 'str',
        'reason': 'str',
        'sub_steps': 'list[V1alpha1StepStatus]',
        'type': 'str'
    }

    attribute_map = {
        'first_execute_time': 'firstExecuteTime',
        'id': 'id',
        'last_execute_time': 'lastExecuteTime',
        'message': 'message',
        'name': 'name',
        'phase': 'phase',
        'reason': 'reason',
        'sub_steps': 'subSteps',
        'type': 'type'
    }

    def __init__(self, first_execute_time=None, id=None, last_execute_time=None, message=None, name=None, phase=None, reason=None, sub_steps=None, type=None):  # noqa: E501
        """V1alpha1WorkflowStepStatus - a model defined in Swagger"""  # noqa: E501
        self._first_execute_time = None
        self._id = None
        self._last_execute_time = None
        self._message = None
        self._name = None
        self._phase = None
        self._reason = None
        self._sub_steps = None
        self._type = None
        self.discriminator = None
        if first_execute_time is not None:
            self.first_execute_time = first_execute_time
        self.id = id
        if last_execute_time is not None:
            self.last_execute_time = last_execute_time
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if phase is not None:
            self.phase = phase
        if reason is not None:
            self.reason = reason
        if sub_steps is not None:
            self.sub_steps = sub_steps
        if type is not None:
            self.type = type

    @property
    def first_execute_time(self):
        """Gets the first_execute_time of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The first_execute_time of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._first_execute_time

    @first_execute_time.setter
    def first_execute_time(self, first_execute_time):
        """Sets the first_execute_time of this V1alpha1WorkflowStepStatus.


        :param first_execute_time: The first_execute_time of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: str
        """

        self._first_execute_time = first_execute_time

    @property
    def id(self):
        """Gets the id of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The id of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1alpha1WorkflowStepStatus.


        :param id: The id of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_execute_time(self):
        """Gets the last_execute_time of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The last_execute_time of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_execute_time

    @last_execute_time.setter
    def last_execute_time(self, last_execute_time):
        """Sets the last_execute_time of this V1alpha1WorkflowStepStatus.


        :param last_execute_time: The last_execute_time of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: str
        """

        self._last_execute_time = last_execute_time

    @property
    def message(self):
        """Gets the message of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The message of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1alpha1WorkflowStepStatus.


        :param message: The message of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The name of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1WorkflowStepStatus.


        :param name: The name of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phase(self):
        """Gets the phase of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The phase of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1alpha1WorkflowStepStatus.


        :param phase: The phase of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The reason of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1alpha1WorkflowStepStatus.


        :param reason: The reason of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def sub_steps(self):
        """Gets the sub_steps of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The sub_steps of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: list[V1alpha1StepStatus]
        """
        return self._sub_steps

    @sub_steps.setter
    def sub_steps(self, sub_steps):
        """Sets the sub_steps of this V1alpha1WorkflowStepStatus.


        :param sub_steps: The sub_steps of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :type: list[V1alpha1StepStatus]
        """

        self._sub_steps = sub_steps

    @property
    def type(self):
        """Gets the type of this V1alpha1WorkflowStepStatus.  # noqa: E501


        :return: The type of this V1alpha1WorkflowStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1alpha1WorkflowStepStatus.


        :param type: The type of this V1alpha1WorkflowStepStatus.  # noqa: E501
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
        if issubclass(V1alpha1WorkflowStepStatus, dict):
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
        if not isinstance(other, V1alpha1WorkflowStepStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other