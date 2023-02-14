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

class CommonRevision(object):
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
        'name': 'str',
        'revision': 'int',
        'revision_hash': 'str'
    }

    attribute_map = {
        'name': 'name',
        'revision': 'revision',
        'revision_hash': 'revisionHash'
    }

    def __init__(self, name=None, revision=None, revision_hash=None):  # noqa: E501
        """CommonRevision - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._revision = None
        self._revision_hash = None
        self.discriminator = None
        self.name = name
        self.revision = revision
        if revision_hash is not None:
            self.revision_hash = revision_hash

    @property
    def name(self):
        """Gets the name of this CommonRevision.  # noqa: E501


        :return: The name of this CommonRevision.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommonRevision.


        :param name: The name of this CommonRevision.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def revision(self):
        """Gets the revision of this CommonRevision.  # noqa: E501


        :return: The revision of this CommonRevision.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this CommonRevision.


        :param revision: The revision of this CommonRevision.  # noqa: E501
        :type: int
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def revision_hash(self):
        """Gets the revision_hash of this CommonRevision.  # noqa: E501


        :return: The revision_hash of this CommonRevision.  # noqa: E501
        :rtype: str
        """
        return self._revision_hash

    @revision_hash.setter
    def revision_hash(self, revision_hash):
        """Sets the revision_hash of this CommonRevision.


        :param revision_hash: The revision_hash of this CommonRevision.  # noqa: E501
        :type: str
        """

        self._revision_hash = revision_hash

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
        if issubclass(CommonRevision, dict):
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
        if not isinstance(other, CommonRevision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other