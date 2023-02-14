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

class ConfigClusterTargetStatus(object):
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
        'application': 'ConfigNamespacedName',
        'cluster_name': 'str',
        'message': 'str',
        'namespace': 'str',
        'status': 'str'
    }

    attribute_map = {
        'application': 'application',
        'cluster_name': 'clusterName',
        'message': 'message',
        'namespace': 'namespace',
        'status': 'status'
    }

    def __init__(self, application=None, cluster_name=None, message=None, namespace=None, status=None):  # noqa: E501
        """ConfigClusterTargetStatus - a model defined in Swagger"""  # noqa: E501
        self._application = None
        self._cluster_name = None
        self._message = None
        self._namespace = None
        self._status = None
        self.discriminator = None
        self.application = application
        self.cluster_name = cluster_name
        self.message = message
        self.namespace = namespace
        self.status = status

    @property
    def application(self):
        """Gets the application of this ConfigClusterTargetStatus.  # noqa: E501


        :return: The application of this ConfigClusterTargetStatus.  # noqa: E501
        :rtype: ConfigNamespacedName
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ConfigClusterTargetStatus.


        :param application: The application of this ConfigClusterTargetStatus.  # noqa: E501
        :type: ConfigNamespacedName
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ConfigClusterTargetStatus.  # noqa: E501


        :return: The cluster_name of this ConfigClusterTargetStatus.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ConfigClusterTargetStatus.


        :param cluster_name: The cluster_name of this ConfigClusterTargetStatus.  # noqa: E501
        :type: str
        """
        if cluster_name is None:
            raise ValueError("Invalid value for `cluster_name`, must not be `None`")  # noqa: E501

        self._cluster_name = cluster_name

    @property
    def message(self):
        """Gets the message of this ConfigClusterTargetStatus.  # noqa: E501


        :return: The message of this ConfigClusterTargetStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConfigClusterTargetStatus.


        :param message: The message of this ConfigClusterTargetStatus.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def namespace(self):
        """Gets the namespace of this ConfigClusterTargetStatus.  # noqa: E501


        :return: The namespace of this ConfigClusterTargetStatus.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ConfigClusterTargetStatus.


        :param namespace: The namespace of this ConfigClusterTargetStatus.  # noqa: E501
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def status(self):
        """Gets the status of this ConfigClusterTargetStatus.  # noqa: E501


        :return: The status of this ConfigClusterTargetStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConfigClusterTargetStatus.


        :param status: The status of this ConfigClusterTargetStatus.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(ConfigClusterTargetStatus, dict):
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
        if not isinstance(other, ConfigClusterTargetStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other