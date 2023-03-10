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

class V1alpha1WorkflowRunStatus(object):
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
        'conditions': 'list[ConditionCondition]',
        'context_backend': 'V1ObjectReference',
        'end_time': 'str',
        'finished': 'bool',
        'message': 'str',
        'mode': 'V1alpha1WorkflowExecuteMode',
        'start_time': 'str',
        'status': 'str',
        'steps': 'list[V1alpha1WorkflowStepStatus]',
        'suspend': 'bool',
        'suspend_state': 'str',
        'terminated': 'bool'
    }

    attribute_map = {
        'conditions': 'conditions',
        'context_backend': 'contextBackend',
        'end_time': 'endTime',
        'finished': 'finished',
        'message': 'message',
        'mode': 'mode',
        'start_time': 'startTime',
        'status': 'status',
        'steps': 'steps',
        'suspend': 'suspend',
        'suspend_state': 'suspendState',
        'terminated': 'terminated'
    }

    def __init__(self, conditions=None, context_backend=None, end_time=None, finished=None, message=None, mode=None, start_time=None, status=None, steps=None, suspend=None, suspend_state=None, terminated=None):  # noqa: E501
        """V1alpha1WorkflowRunStatus - a model defined in Swagger"""  # noqa: E501
        self._conditions = None
        self._context_backend = None
        self._end_time = None
        self._finished = None
        self._message = None
        self._mode = None
        self._start_time = None
        self._status = None
        self._steps = None
        self._suspend = None
        self._suspend_state = None
        self._terminated = None
        self.discriminator = None
        if conditions is not None:
            self.conditions = conditions
        if context_backend is not None:
            self.context_backend = context_backend
        if end_time is not None:
            self.end_time = end_time
        self.finished = finished
        if message is not None:
            self.message = message
        self.mode = mode
        if start_time is not None:
            self.start_time = start_time
        self.status = status
        if steps is not None:
            self.steps = steps
        self.suspend = suspend
        if suspend_state is not None:
            self.suspend_state = suspend_state
        self.terminated = terminated

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The conditions of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: list[ConditionCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1WorkflowRunStatus.


        :param conditions: The conditions of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: list[ConditionCondition]
        """

        self._conditions = conditions

    @property
    def context_backend(self):
        """Gets the context_backend of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The context_backend of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._context_backend

    @context_backend.setter
    def context_backend(self, context_backend):
        """Sets the context_backend of this V1alpha1WorkflowRunStatus.


        :param context_backend: The context_backend of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: V1ObjectReference
        """

        self._context_backend = context_backend

    @property
    def end_time(self):
        """Gets the end_time of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The end_time of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this V1alpha1WorkflowRunStatus.


        :param end_time: The end_time of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def finished(self):
        """Gets the finished of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The finished of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: bool
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this V1alpha1WorkflowRunStatus.


        :param finished: The finished of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: bool
        """
        if finished is None:
            raise ValueError("Invalid value for `finished`, must not be `None`")  # noqa: E501

        self._finished = finished

    @property
    def message(self):
        """Gets the message of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The message of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1alpha1WorkflowRunStatus.


        :param message: The message of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def mode(self):
        """Gets the mode of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The mode of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: V1alpha1WorkflowExecuteMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this V1alpha1WorkflowRunStatus.


        :param mode: The mode of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: V1alpha1WorkflowExecuteMode
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def start_time(self):
        """Gets the start_time of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The start_time of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1alpha1WorkflowRunStatus.


        :param start_time: The start_time of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The status of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1alpha1WorkflowRunStatus.


        :param status: The status of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def steps(self):
        """Gets the steps of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The steps of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: list[V1alpha1WorkflowStepStatus]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this V1alpha1WorkflowRunStatus.


        :param steps: The steps of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: list[V1alpha1WorkflowStepStatus]
        """

        self._steps = steps

    @property
    def suspend(self):
        """Gets the suspend of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The suspend of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1alpha1WorkflowRunStatus.


        :param suspend: The suspend of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: bool
        """
        if suspend is None:
            raise ValueError("Invalid value for `suspend`, must not be `None`")  # noqa: E501

        self._suspend = suspend

    @property
    def suspend_state(self):
        """Gets the suspend_state of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The suspend_state of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: str
        """
        return self._suspend_state

    @suspend_state.setter
    def suspend_state(self, suspend_state):
        """Sets the suspend_state of this V1alpha1WorkflowRunStatus.


        :param suspend_state: The suspend_state of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: str
        """

        self._suspend_state = suspend_state

    @property
    def terminated(self):
        """Gets the terminated of this V1alpha1WorkflowRunStatus.  # noqa: E501


        :return: The terminated of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :rtype: bool
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this V1alpha1WorkflowRunStatus.


        :param terminated: The terminated of this V1alpha1WorkflowRunStatus.  # noqa: E501
        :type: bool
        """
        if terminated is None:
            raise ValueError("Invalid value for `terminated`, must not be `None`")  # noqa: E501

        self._terminated = terminated

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
        if issubclass(V1alpha1WorkflowRunStatus, dict):
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
        if not isinstance(other, V1alpha1WorkflowRunStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
