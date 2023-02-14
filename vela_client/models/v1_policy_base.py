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

class V1PolicyBase(object):
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
        'creator': 'str',
        'description': 'str',
        'env_name': 'str',
        'name': 'str',
        'properties': 'ModelJSONStruct',
        'type': 'str',
        'update_time': 'datetime'
    }

    attribute_map = {
        'alias': 'alias',
        'create_time': 'createTime',
        'creator': 'creator',
        'description': 'description',
        'env_name': 'envName',
        'name': 'name',
        'properties': 'properties',
        'type': 'type',
        'update_time': 'updateTime'
    }

    def __init__(self, alias=None, create_time=None, creator=None, description=None, env_name=None, name=None, properties=None, type=None, update_time=None):  # noqa: E501
        """V1PolicyBase - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._env_name = None
        self._name = None
        self._properties = None
        self._type = None
        self._update_time = None
        self.discriminator = None
        self.alias = alias
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.env_name = env_name
        self.name = name
        self.properties = properties
        self.type = type
        self.update_time = update_time

    @property
    def alias(self):
        """Gets the alias of this V1PolicyBase.  # noqa: E501


        :return: The alias of this V1PolicyBase.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1PolicyBase.


        :param alias: The alias of this V1PolicyBase.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def create_time(self):
        """Gets the create_time of this V1PolicyBase.  # noqa: E501


        :return: The create_time of this V1PolicyBase.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1PolicyBase.


        :param create_time: The create_time of this V1PolicyBase.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this V1PolicyBase.  # noqa: E501


        :return: The creator of this V1PolicyBase.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this V1PolicyBase.


        :param creator: The creator of this V1PolicyBase.  # noqa: E501
        :type: str
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this V1PolicyBase.  # noqa: E501


        :return: The description of this V1PolicyBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1PolicyBase.


        :param description: The description of this V1PolicyBase.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def env_name(self):
        """Gets the env_name of this V1PolicyBase.  # noqa: E501


        :return: The env_name of this V1PolicyBase.  # noqa: E501
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this V1PolicyBase.


        :param env_name: The env_name of this V1PolicyBase.  # noqa: E501
        :type: str
        """
        if env_name is None:
            raise ValueError("Invalid value for `env_name`, must not be `None`")  # noqa: E501

        self._env_name = env_name

    @property
    def name(self):
        """Gets the name of this V1PolicyBase.  # noqa: E501


        :return: The name of this V1PolicyBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1PolicyBase.


        :param name: The name of this V1PolicyBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this V1PolicyBase.  # noqa: E501


        :return: The properties of this V1PolicyBase.  # noqa: E501
        :rtype: ModelJSONStruct
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V1PolicyBase.


        :param properties: The properties of this V1PolicyBase.  # noqa: E501
        :type: ModelJSONStruct
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this V1PolicyBase.  # noqa: E501


        :return: The type of this V1PolicyBase.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1PolicyBase.


        :param type: The type of this V1PolicyBase.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def update_time(self):
        """Gets the update_time of this V1PolicyBase.  # noqa: E501


        :return: The update_time of this V1PolicyBase.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1PolicyBase.


        :param update_time: The update_time of this V1PolicyBase.  # noqa: E501
        :type: datetime
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

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
        if issubclass(V1PolicyBase, dict):
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
        if not isinstance(other, V1PolicyBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
