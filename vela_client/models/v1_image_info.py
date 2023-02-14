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

class V1ImageInfo(object):
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
        'info': 'V1ConfigFile',
        'manifest': 'V1Manifest',
        'message': 'str',
        'name': 'str',
        'registry': 'str',
        'secret_names': 'list[str]',
        'size': 'int'
    }

    attribute_map = {
        'info': 'info',
        'manifest': 'manifest',
        'message': 'message',
        'name': 'name',
        'registry': 'registry',
        'secret_names': 'secretNames',
        'size': 'size'
    }

    def __init__(self, info=None, manifest=None, message=None, name=None, registry=None, secret_names=None, size=None):  # noqa: E501
        """V1ImageInfo - a model defined in Swagger"""  # noqa: E501
        self._info = None
        self._manifest = None
        self._message = None
        self._name = None
        self._registry = None
        self._secret_names = None
        self._size = None
        self.discriminator = None
        if info is not None:
            self.info = info
        self.manifest = manifest
        if message is not None:
            self.message = message
        self.name = name
        self.registry = registry
        self.secret_names = secret_names
        self.size = size

    @property
    def info(self):
        """Gets the info of this V1ImageInfo.  # noqa: E501


        :return: The info of this V1ImageInfo.  # noqa: E501
        :rtype: V1ConfigFile
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this V1ImageInfo.


        :param info: The info of this V1ImageInfo.  # noqa: E501
        :type: V1ConfigFile
        """

        self._info = info

    @property
    def manifest(self):
        """Gets the manifest of this V1ImageInfo.  # noqa: E501


        :return: The manifest of this V1ImageInfo.  # noqa: E501
        :rtype: V1Manifest
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this V1ImageInfo.


        :param manifest: The manifest of this V1ImageInfo.  # noqa: E501
        :type: V1Manifest
        """
        if manifest is None:
            raise ValueError("Invalid value for `manifest`, must not be `None`")  # noqa: E501

        self._manifest = manifest

    @property
    def message(self):
        """Gets the message of this V1ImageInfo.  # noqa: E501


        :return: The message of this V1ImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1ImageInfo.


        :param message: The message of this V1ImageInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this V1ImageInfo.  # noqa: E501


        :return: The name of this V1ImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ImageInfo.


        :param name: The name of this V1ImageInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def registry(self):
        """Gets the registry of this V1ImageInfo.  # noqa: E501


        :return: The registry of this V1ImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this V1ImageInfo.


        :param registry: The registry of this V1ImageInfo.  # noqa: E501
        :type: str
        """
        if registry is None:
            raise ValueError("Invalid value for `registry`, must not be `None`")  # noqa: E501

        self._registry = registry

    @property
    def secret_names(self):
        """Gets the secret_names of this V1ImageInfo.  # noqa: E501


        :return: The secret_names of this V1ImageInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._secret_names

    @secret_names.setter
    def secret_names(self, secret_names):
        """Sets the secret_names of this V1ImageInfo.


        :param secret_names: The secret_names of this V1ImageInfo.  # noqa: E501
        :type: list[str]
        """
        if secret_names is None:
            raise ValueError("Invalid value for `secret_names`, must not be `None`")  # noqa: E501

        self._secret_names = secret_names

    @property
    def size(self):
        """Gets the size of this V1ImageInfo.  # noqa: E501


        :return: The size of this V1ImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1ImageInfo.


        :param size: The size of this V1ImageInfo.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if issubclass(V1ImageInfo, dict):
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
        if not isinstance(other, V1ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
