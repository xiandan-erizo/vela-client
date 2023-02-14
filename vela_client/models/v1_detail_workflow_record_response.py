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

class V1DetailWorkflowRecordResponse(object):
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
        'application_revision': 'str',
        'deploy_time': 'datetime',
        'deploy_user': 'str',
        'name': 'str',
        'namespace': 'str',
        'note': 'str',
        'start_time': 'datetime',
        'status': 'str',
        'steps': 'list[ModelWorkflowStepStatus]',
        'trigger_type': 'str',
        'workflow_alias': 'str',
        'workflow_name': 'str'
    }

    attribute_map = {
        'application_revision': 'applicationRevision',
        'deploy_time': 'deployTime',
        'deploy_user': 'deployUser',
        'name': 'name',
        'namespace': 'namespace',
        'note': 'note',
        'start_time': 'startTime',
        'status': 'status',
        'steps': 'steps',
        'trigger_type': 'triggerType',
        'workflow_alias': 'workflowAlias',
        'workflow_name': 'workflowName'
    }

    def __init__(self, application_revision=None, deploy_time=None, deploy_user=None, name=None, namespace=None, note=None, start_time=None, status=None, steps=None, trigger_type=None, workflow_alias=None, workflow_name=None):  # noqa: E501
        """V1DetailWorkflowRecordResponse - a model defined in Swagger"""  # noqa: E501
        self._application_revision = None
        self._deploy_time = None
        self._deploy_user = None
        self._name = None
        self._namespace = None
        self._note = None
        self._start_time = None
        self._status = None
        self._steps = None
        self._trigger_type = None
        self._workflow_alias = None
        self._workflow_name = None
        self.discriminator = None
        self.application_revision = application_revision
        self.deploy_time = deploy_time
        self.deploy_user = deploy_user
        self.name = name
        self.namespace = namespace
        self.note = note
        if start_time is not None:
            self.start_time = start_time
        self.status = status
        if steps is not None:
            self.steps = steps
        self.trigger_type = trigger_type
        self.workflow_alias = workflow_alias
        self.workflow_name = workflow_name

    @property
    def application_revision(self):
        """Gets the application_revision of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The application_revision of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_revision

    @application_revision.setter
    def application_revision(self, application_revision):
        """Sets the application_revision of this V1DetailWorkflowRecordResponse.


        :param application_revision: The application_revision of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if application_revision is None:
            raise ValueError("Invalid value for `application_revision`, must not be `None`")  # noqa: E501

        self._application_revision = application_revision

    @property
    def deploy_time(self):
        """Gets the deploy_time of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The deploy_time of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._deploy_time

    @deploy_time.setter
    def deploy_time(self, deploy_time):
        """Sets the deploy_time of this V1DetailWorkflowRecordResponse.


        :param deploy_time: The deploy_time of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: datetime
        """
        if deploy_time is None:
            raise ValueError("Invalid value for `deploy_time`, must not be `None`")  # noqa: E501

        self._deploy_time = deploy_time

    @property
    def deploy_user(self):
        """Gets the deploy_user of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The deploy_user of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._deploy_user

    @deploy_user.setter
    def deploy_user(self, deploy_user):
        """Sets the deploy_user of this V1DetailWorkflowRecordResponse.


        :param deploy_user: The deploy_user of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if deploy_user is None:
            raise ValueError("Invalid value for `deploy_user`, must not be `None`")  # noqa: E501

        self._deploy_user = deploy_user

    @property
    def name(self):
        """Gets the name of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The name of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1DetailWorkflowRecordResponse.


        :param name: The name of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The namespace of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1DetailWorkflowRecordResponse.


        :param namespace: The namespace of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def note(self):
        """Gets the note of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The note of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this V1DetailWorkflowRecordResponse.


        :param note: The note of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def start_time(self):
        """Gets the start_time of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The start_time of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1DetailWorkflowRecordResponse.


        :param start_time: The start_time of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The status of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1DetailWorkflowRecordResponse.


        :param status: The status of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def steps(self):
        """Gets the steps of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The steps of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: list[ModelWorkflowStepStatus]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this V1DetailWorkflowRecordResponse.


        :param steps: The steps of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: list[ModelWorkflowStepStatus]
        """

        self._steps = steps

    @property
    def trigger_type(self):
        """Gets the trigger_type of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The trigger_type of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this V1DetailWorkflowRecordResponse.


        :param trigger_type: The trigger_type of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if trigger_type is None:
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501

        self._trigger_type = trigger_type

    @property
    def workflow_alias(self):
        """Gets the workflow_alias of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The workflow_alias of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._workflow_alias

    @workflow_alias.setter
    def workflow_alias(self, workflow_alias):
        """Sets the workflow_alias of this V1DetailWorkflowRecordResponse.


        :param workflow_alias: The workflow_alias of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if workflow_alias is None:
            raise ValueError("Invalid value for `workflow_alias`, must not be `None`")  # noqa: E501

        self._workflow_alias = workflow_alias

    @property
    def workflow_name(self):
        """Gets the workflow_name of this V1DetailWorkflowRecordResponse.  # noqa: E501


        :return: The workflow_name of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this V1DetailWorkflowRecordResponse.


        :param workflow_name: The workflow_name of this V1DetailWorkflowRecordResponse.  # noqa: E501
        :type: str
        """
        if workflow_name is None:
            raise ValueError("Invalid value for `workflow_name`, must not be `None`")  # noqa: E501

        self._workflow_name = workflow_name

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
        if issubclass(V1DetailWorkflowRecordResponse, dict):
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
        if not isinstance(other, V1DetailWorkflowRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other