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

class CommonTerraform(object):
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
        'configuration': 'str',
        'custom_region': 'str',
        'delete_resource': 'bool',
        'path': 'str',
        'provider_ref': 'TypesReference',
        'type': 'str',
        'write_connection_secret_to_ref': 'TypesSecretReference'
    }

    attribute_map = {
        'configuration': 'configuration',
        'custom_region': 'customRegion',
        'delete_resource': 'deleteResource',
        'path': 'path',
        'provider_ref': 'providerRef',
        'type': 'type',
        'write_connection_secret_to_ref': 'writeConnectionSecretToRef'
    }

    def __init__(self, configuration=None, custom_region=None, delete_resource=None, path=None, provider_ref=None, type=None, write_connection_secret_to_ref=None):  # noqa: E501
        """CommonTerraform - a model defined in Swagger"""  # noqa: E501
        self._configuration = None
        self._custom_region = None
        self._delete_resource = None
        self._path = None
        self._provider_ref = None
        self._type = None
        self._write_connection_secret_to_ref = None
        self.discriminator = None
        self.configuration = configuration
        if custom_region is not None:
            self.custom_region = custom_region
        if delete_resource is not None:
            self.delete_resource = delete_resource
        if path is not None:
            self.path = path
        if provider_ref is not None:
            self.provider_ref = provider_ref
        if type is not None:
            self.type = type
        if write_connection_secret_to_ref is not None:
            self.write_connection_secret_to_ref = write_connection_secret_to_ref

    @property
    def configuration(self):
        """Gets the configuration of this CommonTerraform.  # noqa: E501


        :return: The configuration of this CommonTerraform.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this CommonTerraform.


        :param configuration: The configuration of this CommonTerraform.  # noqa: E501
        :type: str
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def custom_region(self):
        """Gets the custom_region of this CommonTerraform.  # noqa: E501


        :return: The custom_region of this CommonTerraform.  # noqa: E501
        :rtype: str
        """
        return self._custom_region

    @custom_region.setter
    def custom_region(self, custom_region):
        """Sets the custom_region of this CommonTerraform.


        :param custom_region: The custom_region of this CommonTerraform.  # noqa: E501
        :type: str
        """

        self._custom_region = custom_region

    @property
    def delete_resource(self):
        """Gets the delete_resource of this CommonTerraform.  # noqa: E501


        :return: The delete_resource of this CommonTerraform.  # noqa: E501
        :rtype: bool
        """
        return self._delete_resource

    @delete_resource.setter
    def delete_resource(self, delete_resource):
        """Sets the delete_resource of this CommonTerraform.


        :param delete_resource: The delete_resource of this CommonTerraform.  # noqa: E501
        :type: bool
        """

        self._delete_resource = delete_resource

    @property
    def path(self):
        """Gets the path of this CommonTerraform.  # noqa: E501


        :return: The path of this CommonTerraform.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CommonTerraform.


        :param path: The path of this CommonTerraform.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def provider_ref(self):
        """Gets the provider_ref of this CommonTerraform.  # noqa: E501


        :return: The provider_ref of this CommonTerraform.  # noqa: E501
        :rtype: TypesReference
        """
        return self._provider_ref

    @provider_ref.setter
    def provider_ref(self, provider_ref):
        """Sets the provider_ref of this CommonTerraform.


        :param provider_ref: The provider_ref of this CommonTerraform.  # noqa: E501
        :type: TypesReference
        """

        self._provider_ref = provider_ref

    @property
    def type(self):
        """Gets the type of this CommonTerraform.  # noqa: E501


        :return: The type of this CommonTerraform.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CommonTerraform.


        :param type: The type of this CommonTerraform.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def write_connection_secret_to_ref(self):
        """Gets the write_connection_secret_to_ref of this CommonTerraform.  # noqa: E501


        :return: The write_connection_secret_to_ref of this CommonTerraform.  # noqa: E501
        :rtype: TypesSecretReference
        """
        return self._write_connection_secret_to_ref

    @write_connection_secret_to_ref.setter
    def write_connection_secret_to_ref(self, write_connection_secret_to_ref):
        """Sets the write_connection_secret_to_ref of this CommonTerraform.


        :param write_connection_secret_to_ref: The write_connection_secret_to_ref of this CommonTerraform.  # noqa: E501
        :type: TypesSecretReference
        """

        self._write_connection_secret_to_ref = write_connection_secret_to_ref

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
        if issubclass(CommonTerraform, dict):
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
        if not isinstance(other, CommonTerraform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
