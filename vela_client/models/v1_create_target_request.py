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

class V1CreateTargetRequest(object):
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
        'cluster': 'V1ClusterTarget',
        'description': 'str',
        'name': 'str',
        'project': 'str',
        'variable': 'object'
    }

    attribute_map = {
        'alias': 'alias',
        'cluster': 'cluster',
        'description': 'description',
        'name': 'name',
        'project': 'project',
        'variable': 'variable'
    }

    def __init__(self, alias=None, cluster=None, description=None, name=None, project=None, variable=None):  # noqa: E501
        """V1CreateTargetRequest - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._cluster = None
        self._description = None
        self._name = None
        self._project = None
        self._variable = None
        self.discriminator = None
        if alias is not None:
            self.alias = alias
        if cluster is not None:
            self.cluster = cluster
        if description is not None:
            self.description = description
        self.name = name
        self.project = project
        if variable is not None:
            self.variable = variable

    @property
    def alias(self):
        """Gets the alias of this V1CreateTargetRequest.  # noqa: E501


        :return: The alias of this V1CreateTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1CreateTargetRequest.


        :param alias: The alias of this V1CreateTargetRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def cluster(self):
        """Gets the cluster of this V1CreateTargetRequest.  # noqa: E501


        :return: The cluster of this V1CreateTargetRequest.  # noqa: E501
        :rtype: V1ClusterTarget
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this V1CreateTargetRequest.


        :param cluster: The cluster of this V1CreateTargetRequest.  # noqa: E501
        :type: V1ClusterTarget
        """

        self._cluster = cluster

    @property
    def description(self):
        """Gets the description of this V1CreateTargetRequest.  # noqa: E501


        :return: The description of this V1CreateTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1CreateTargetRequest.


        :param description: The description of this V1CreateTargetRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this V1CreateTargetRequest.  # noqa: E501


        :return: The name of this V1CreateTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CreateTargetRequest.


        :param name: The name of this V1CreateTargetRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project(self):
        """Gets the project of this V1CreateTargetRequest.  # noqa: E501


        :return: The project of this V1CreateTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1CreateTargetRequest.


        :param project: The project of this V1CreateTargetRequest.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def variable(self):
        """Gets the variable of this V1CreateTargetRequest.  # noqa: E501


        :return: The variable of this V1CreateTargetRequest.  # noqa: E501
        :rtype: object
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this V1CreateTargetRequest.


        :param variable: The variable of this V1CreateTargetRequest.  # noqa: E501
        :type: object
        """

        self._variable = variable

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
        if issubclass(V1CreateTargetRequest, dict):
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
        if not isinstance(other, V1CreateTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
