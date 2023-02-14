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

class V1SystemInfo(object):
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
        'dex_user_default_platform_roles': 'list[str]',
        'dex_user_default_projects': 'list[ModelProjectRef]',
        'enable_collection': 'bool',
        'install_time': 'datetime',
        'login_type': 'str',
        'platform_id': 'str'
    }

    attribute_map = {
        'dex_user_default_platform_roles': 'dexUserDefaultPlatformRoles',
        'dex_user_default_projects': 'dexUserDefaultProjects',
        'enable_collection': 'enableCollection',
        'install_time': 'installTime',
        'login_type': 'loginType',
        'platform_id': 'platformID'
    }

    def __init__(self, dex_user_default_platform_roles=None, dex_user_default_projects=None, enable_collection=None, install_time=None, login_type=None, platform_id=None):  # noqa: E501
        """V1SystemInfo - a model defined in Swagger"""  # noqa: E501
        self._dex_user_default_platform_roles = None
        self._dex_user_default_projects = None
        self._enable_collection = None
        self._install_time = None
        self._login_type = None
        self._platform_id = None
        self.discriminator = None
        if dex_user_default_platform_roles is not None:
            self.dex_user_default_platform_roles = dex_user_default_platform_roles
        if dex_user_default_projects is not None:
            self.dex_user_default_projects = dex_user_default_projects
        self.enable_collection = enable_collection
        if install_time is not None:
            self.install_time = install_time
        self.login_type = login_type
        self.platform_id = platform_id

    @property
    def dex_user_default_platform_roles(self):
        """Gets the dex_user_default_platform_roles of this V1SystemInfo.  # noqa: E501


        :return: The dex_user_default_platform_roles of this V1SystemInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._dex_user_default_platform_roles

    @dex_user_default_platform_roles.setter
    def dex_user_default_platform_roles(self, dex_user_default_platform_roles):
        """Sets the dex_user_default_platform_roles of this V1SystemInfo.


        :param dex_user_default_platform_roles: The dex_user_default_platform_roles of this V1SystemInfo.  # noqa: E501
        :type: list[str]
        """

        self._dex_user_default_platform_roles = dex_user_default_platform_roles

    @property
    def dex_user_default_projects(self):
        """Gets the dex_user_default_projects of this V1SystemInfo.  # noqa: E501


        :return: The dex_user_default_projects of this V1SystemInfo.  # noqa: E501
        :rtype: list[ModelProjectRef]
        """
        return self._dex_user_default_projects

    @dex_user_default_projects.setter
    def dex_user_default_projects(self, dex_user_default_projects):
        """Sets the dex_user_default_projects of this V1SystemInfo.


        :param dex_user_default_projects: The dex_user_default_projects of this V1SystemInfo.  # noqa: E501
        :type: list[ModelProjectRef]
        """

        self._dex_user_default_projects = dex_user_default_projects

    @property
    def enable_collection(self):
        """Gets the enable_collection of this V1SystemInfo.  # noqa: E501


        :return: The enable_collection of this V1SystemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enable_collection

    @enable_collection.setter
    def enable_collection(self, enable_collection):
        """Sets the enable_collection of this V1SystemInfo.


        :param enable_collection: The enable_collection of this V1SystemInfo.  # noqa: E501
        :type: bool
        """
        if enable_collection is None:
            raise ValueError("Invalid value for `enable_collection`, must not be `None`")  # noqa: E501

        self._enable_collection = enable_collection

    @property
    def install_time(self):
        """Gets the install_time of this V1SystemInfo.  # noqa: E501


        :return: The install_time of this V1SystemInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._install_time

    @install_time.setter
    def install_time(self, install_time):
        """Sets the install_time of this V1SystemInfo.


        :param install_time: The install_time of this V1SystemInfo.  # noqa: E501
        :type: datetime
        """

        self._install_time = install_time

    @property
    def login_type(self):
        """Gets the login_type of this V1SystemInfo.  # noqa: E501


        :return: The login_type of this V1SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._login_type

    @login_type.setter
    def login_type(self, login_type):
        """Sets the login_type of this V1SystemInfo.


        :param login_type: The login_type of this V1SystemInfo.  # noqa: E501
        :type: str
        """
        if login_type is None:
            raise ValueError("Invalid value for `login_type`, must not be `None`")  # noqa: E501

        self._login_type = login_type

    @property
    def platform_id(self):
        """Gets the platform_id of this V1SystemInfo.  # noqa: E501


        :return: The platform_id of this V1SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this V1SystemInfo.


        :param platform_id: The platform_id of this V1SystemInfo.  # noqa: E501
        :type: str
        """
        if platform_id is None:
            raise ValueError("Invalid value for `platform_id`, must not be `None`")  # noqa: E501

        self._platform_id = platform_id

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
        if issubclass(V1SystemInfo, dict):
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
        if not isinstance(other, V1SystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
