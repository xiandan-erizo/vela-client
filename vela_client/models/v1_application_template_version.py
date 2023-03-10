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

class V1ApplicationTemplateVersion(object):
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
        'create_time': 'datetime',
        'create_user': 'str',
        'description': 'str',
        'update_time': 'datetime',
        'version': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'create_user': 'createUser',
        'description': 'description',
        'update_time': 'updateTime',
        'version': 'version'
    }

    def __init__(self, create_time=None, create_user=None, description=None, update_time=None, version=None):  # noqa: E501
        """V1ApplicationTemplateVersion - a model defined in Swagger"""  # noqa: E501
        self._create_time = None
        self._create_user = None
        self._description = None
        self._update_time = None
        self._version = None
        self.discriminator = None
        self.create_time = create_time
        self.create_user = create_user
        self.description = description
        self.update_time = update_time
        self.version = version

    @property
    def create_time(self):
        """Gets the create_time of this V1ApplicationTemplateVersion.  # noqa: E501


        :return: The create_time of this V1ApplicationTemplateVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1ApplicationTemplateVersion.


        :param create_time: The create_time of this V1ApplicationTemplateVersion.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this V1ApplicationTemplateVersion.  # noqa: E501


        :return: The create_user of this V1ApplicationTemplateVersion.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this V1ApplicationTemplateVersion.


        :param create_user: The create_user of this V1ApplicationTemplateVersion.  # noqa: E501
        :type: str
        """
        if create_user is None:
            raise ValueError("Invalid value for `create_user`, must not be `None`")  # noqa: E501

        self._create_user = create_user

    @property
    def description(self):
        """Gets the description of this V1ApplicationTemplateVersion.  # noqa: E501


        :return: The description of this V1ApplicationTemplateVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ApplicationTemplateVersion.


        :param description: The description of this V1ApplicationTemplateVersion.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def update_time(self):
        """Gets the update_time of this V1ApplicationTemplateVersion.  # noqa: E501


        :return: The update_time of this V1ApplicationTemplateVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1ApplicationTemplateVersion.


        :param update_time: The update_time of this V1ApplicationTemplateVersion.  # noqa: E501
        :type: datetime
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def version(self):
        """Gets the version of this V1ApplicationTemplateVersion.  # noqa: E501


        :return: The version of this V1ApplicationTemplateVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1ApplicationTemplateVersion.


        :param version: The version of this V1ApplicationTemplateVersion.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if issubclass(V1ApplicationTemplateVersion, dict):
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
        if not isinstance(other, V1ApplicationTemplateVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
