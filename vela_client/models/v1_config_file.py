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

class V1ConfigFile(object):
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
        'architecture': 'str',
        'author': 'str',
        'config': 'V1Config',
        'container': 'str',
        'created': 'str',
        'docker_version': 'str',
        'history': 'list[V1History]',
        'os': 'str',
        'os_version': 'str',
        'rootfs': 'V1RootFS',
        'variant': 'str'
    }

    attribute_map = {
        'architecture': 'architecture',
        'author': 'author',
        'config': 'config',
        'container': 'container',
        'created': 'created',
        'docker_version': 'docker_version',
        'history': 'history',
        'os': 'os',
        'os_version': 'os.version',
        'rootfs': 'rootfs',
        'variant': 'variant'
    }

    def __init__(self, architecture=None, author=None, config=None, container=None, created=None, docker_version=None, history=None, os=None, os_version=None, rootfs=None, variant=None):  # noqa: E501
        """V1ConfigFile - a model defined in Swagger"""  # noqa: E501
        self._architecture = None
        self._author = None
        self._config = None
        self._container = None
        self._created = None
        self._docker_version = None
        self._history = None
        self._os = None
        self._os_version = None
        self._rootfs = None
        self._variant = None
        self.discriminator = None
        self.architecture = architecture
        if author is not None:
            self.author = author
        self.config = config
        if container is not None:
            self.container = container
        if created is not None:
            self.created = created
        if docker_version is not None:
            self.docker_version = docker_version
        if history is not None:
            self.history = history
        self.os = os
        if os_version is not None:
            self.os_version = os_version
        self.rootfs = rootfs
        if variant is not None:
            self.variant = variant

    @property
    def architecture(self):
        """Gets the architecture of this V1ConfigFile.  # noqa: E501


        :return: The architecture of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this V1ConfigFile.


        :param architecture: The architecture of this V1ConfigFile.  # noqa: E501
        :type: str
        """
        if architecture is None:
            raise ValueError("Invalid value for `architecture`, must not be `None`")  # noqa: E501

        self._architecture = architecture

    @property
    def author(self):
        """Gets the author of this V1ConfigFile.  # noqa: E501


        :return: The author of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this V1ConfigFile.


        :param author: The author of this V1ConfigFile.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def config(self):
        """Gets the config of this V1ConfigFile.  # noqa: E501


        :return: The config of this V1ConfigFile.  # noqa: E501
        :rtype: V1Config
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this V1ConfigFile.


        :param config: The config of this V1ConfigFile.  # noqa: E501
        :type: V1Config
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def container(self):
        """Gets the container of this V1ConfigFile.  # noqa: E501


        :return: The container of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this V1ConfigFile.


        :param container: The container of this V1ConfigFile.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def created(self):
        """Gets the created of this V1ConfigFile.  # noqa: E501


        :return: The created of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this V1ConfigFile.


        :param created: The created of this V1ConfigFile.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def docker_version(self):
        """Gets the docker_version of this V1ConfigFile.  # noqa: E501


        :return: The docker_version of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """Sets the docker_version of this V1ConfigFile.


        :param docker_version: The docker_version of this V1ConfigFile.  # noqa: E501
        :type: str
        """

        self._docker_version = docker_version

    @property
    def history(self):
        """Gets the history of this V1ConfigFile.  # noqa: E501


        :return: The history of this V1ConfigFile.  # noqa: E501
        :rtype: list[V1History]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this V1ConfigFile.


        :param history: The history of this V1ConfigFile.  # noqa: E501
        :type: list[V1History]
        """

        self._history = history

    @property
    def os(self):
        """Gets the os of this V1ConfigFile.  # noqa: E501


        :return: The os of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this V1ConfigFile.


        :param os: The os of this V1ConfigFile.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def os_version(self):
        """Gets the os_version of this V1ConfigFile.  # noqa: E501


        :return: The os_version of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this V1ConfigFile.


        :param os_version: The os_version of this V1ConfigFile.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def rootfs(self):
        """Gets the rootfs of this V1ConfigFile.  # noqa: E501


        :return: The rootfs of this V1ConfigFile.  # noqa: E501
        :rtype: V1RootFS
        """
        return self._rootfs

    @rootfs.setter
    def rootfs(self, rootfs):
        """Sets the rootfs of this V1ConfigFile.


        :param rootfs: The rootfs of this V1ConfigFile.  # noqa: E501
        :type: V1RootFS
        """
        if rootfs is None:
            raise ValueError("Invalid value for `rootfs`, must not be `None`")  # noqa: E501

        self._rootfs = rootfs

    @property
    def variant(self):
        """Gets the variant of this V1ConfigFile.  # noqa: E501


        :return: The variant of this V1ConfigFile.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this V1ConfigFile.


        :param variant: The variant of this V1ConfigFile.  # noqa: E501
        :type: str
        """

        self._variant = variant

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
        if issubclass(V1ConfigFile, dict):
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
        if not isinstance(other, V1ConfigFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other