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

class V1PipelineListItem(object):
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
        'create_time': 'datetime',
        'description': 'str',
        'info': 'V1PipelineInfo',
        'name': 'str',
        'project': 'V1NameAlias'
    }

    attribute_map = {
        'alias': 'alias',
        'create_time': 'createTime',
        'description': 'description',
        'info': 'info',
        'name': 'name',
        'project': 'project'
    }

    def __init__(self, alias=None, create_time=None, description=None, info=None, name=None, project=None):  # noqa: E501
        """V1PipelineListItem - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._create_time = None
        self._description = None
        self._info = None
        self._name = None
        self._project = None
        self.discriminator = None
        self.alias = alias
        self.create_time = create_time
        self.description = description
        self.info = info
        self.name = name
        self.project = project

    @property
    def alias(self):
        """Gets the alias of this V1PipelineListItem.  # noqa: E501


        :return: The alias of this V1PipelineListItem.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1PipelineListItem.


        :param alias: The alias of this V1PipelineListItem.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def create_time(self):
        """Gets the create_time of this V1PipelineListItem.  # noqa: E501


        :return: The create_time of this V1PipelineListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1PipelineListItem.


        :param create_time: The create_time of this V1PipelineListItem.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this V1PipelineListItem.  # noqa: E501


        :return: The description of this V1PipelineListItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1PipelineListItem.


        :param description: The description of this V1PipelineListItem.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def info(self):
        """Gets the info of this V1PipelineListItem.  # noqa: E501


        :return: The info of this V1PipelineListItem.  # noqa: E501
        :rtype: V1PipelineInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this V1PipelineListItem.


        :param info: The info of this V1PipelineListItem.  # noqa: E501
        :type: V1PipelineInfo
        """
        if info is None:
            raise ValueError("Invalid value for `info`, must not be `None`")  # noqa: E501

        self._info = info

    @property
    def name(self):
        """Gets the name of this V1PipelineListItem.  # noqa: E501


        :return: The name of this V1PipelineListItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1PipelineListItem.


        :param name: The name of this V1PipelineListItem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project(self):
        """Gets the project of this V1PipelineListItem.  # noqa: E501


        :return: The project of this V1PipelineListItem.  # noqa: E501
        :rtype: V1NameAlias
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1PipelineListItem.


        :param project: The project of this V1PipelineListItem.  # noqa: E501
        :type: V1NameAlias
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

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
        if issubclass(V1PipelineListItem, dict):
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
        if not isinstance(other, V1PipelineListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
