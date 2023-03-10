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

class CommonApplicationComponentStatus(object):
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
        'cluster': 'str',
        'env': 'str',
        'healthy': 'bool',
        'message': 'str',
        'name': 'str',
        'namespace': 'str',
        'scopes': 'list[V1ObjectReference]',
        'traits': 'list[CommonApplicationTraitStatus]',
        'workload_definition': 'CommonWorkloadGVK'
    }

    attribute_map = {
        'cluster': 'cluster',
        'env': 'env',
        'healthy': 'healthy',
        'message': 'message',
        'name': 'name',
        'namespace': 'namespace',
        'scopes': 'scopes',
        'traits': 'traits',
        'workload_definition': 'workloadDefinition'
    }

    def __init__(self, cluster=None, env=None, healthy=None, message=None, name=None, namespace=None, scopes=None, traits=None, workload_definition=None):  # noqa: E501
        """CommonApplicationComponentStatus - a model defined in Swagger"""  # noqa: E501
        self._cluster = None
        self._env = None
        self._healthy = None
        self._message = None
        self._name = None
        self._namespace = None
        self._scopes = None
        self._traits = None
        self._workload_definition = None
        self.discriminator = None
        if cluster is not None:
            self.cluster = cluster
        if env is not None:
            self.env = env
        self.healthy = healthy
        if message is not None:
            self.message = message
        self.name = name
        if namespace is not None:
            self.namespace = namespace
        if scopes is not None:
            self.scopes = scopes
        if traits is not None:
            self.traits = traits
        if workload_definition is not None:
            self.workload_definition = workload_definition

    @property
    def cluster(self):
        """Gets the cluster of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The cluster of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this CommonApplicationComponentStatus.


        :param cluster: The cluster of this CommonApplicationComponentStatus.  # noqa: E501
        :type: str
        """

        self._cluster = cluster

    @property
    def env(self):
        """Gets the env of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The env of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: str
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this CommonApplicationComponentStatus.


        :param env: The env of this CommonApplicationComponentStatus.  # noqa: E501
        :type: str
        """

        self._env = env

    @property
    def healthy(self):
        """Gets the healthy of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The healthy of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """Sets the healthy of this CommonApplicationComponentStatus.


        :param healthy: The healthy of this CommonApplicationComponentStatus.  # noqa: E501
        :type: bool
        """
        if healthy is None:
            raise ValueError("Invalid value for `healthy`, must not be `None`")  # noqa: E501

        self._healthy = healthy

    @property
    def message(self):
        """Gets the message of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The message of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CommonApplicationComponentStatus.


        :param message: The message of this CommonApplicationComponentStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The name of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommonApplicationComponentStatus.


        :param name: The name of this CommonApplicationComponentStatus.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The namespace of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CommonApplicationComponentStatus.


        :param namespace: The namespace of this CommonApplicationComponentStatus.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def scopes(self):
        """Gets the scopes of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The scopes of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: list[V1ObjectReference]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this CommonApplicationComponentStatus.


        :param scopes: The scopes of this CommonApplicationComponentStatus.  # noqa: E501
        :type: list[V1ObjectReference]
        """

        self._scopes = scopes

    @property
    def traits(self):
        """Gets the traits of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The traits of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: list[CommonApplicationTraitStatus]
        """
        return self._traits

    @traits.setter
    def traits(self, traits):
        """Sets the traits of this CommonApplicationComponentStatus.


        :param traits: The traits of this CommonApplicationComponentStatus.  # noqa: E501
        :type: list[CommonApplicationTraitStatus]
        """

        self._traits = traits

    @property
    def workload_definition(self):
        """Gets the workload_definition of this CommonApplicationComponentStatus.  # noqa: E501


        :return: The workload_definition of this CommonApplicationComponentStatus.  # noqa: E501
        :rtype: CommonWorkloadGVK
        """
        return self._workload_definition

    @workload_definition.setter
    def workload_definition(self, workload_definition):
        """Sets the workload_definition of this CommonApplicationComponentStatus.


        :param workload_definition: The workload_definition of this CommonApplicationComponentStatus.  # noqa: E501
        :type: CommonWorkloadGVK
        """

        self._workload_definition = workload_definition

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
        if issubclass(CommonApplicationComponentStatus, dict):
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
        if not isinstance(other, CommonApplicationComponentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
