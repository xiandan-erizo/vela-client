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

class V1AppCompareReq(object):
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
        'compare_latest_with_running': 'V1CompareLatestWithRunningOption',
        'compare_revision_with_latest': 'V1CompareRevisionWithLatestOption',
        'compare_revision_with_running': 'V1CompareRevisionWithRunningOption'
    }

    attribute_map = {
        'compare_latest_with_running': 'compareLatestWithRunning',
        'compare_revision_with_latest': 'compareRevisionWithLatest',
        'compare_revision_with_running': 'compareRevisionWithRunning'
    }

    def __init__(self, compare_latest_with_running=None, compare_revision_with_latest=None, compare_revision_with_running=None):  # noqa: E501
        """V1AppCompareReq - a model defined in Swagger"""  # noqa: E501
        self._compare_latest_with_running = None
        self._compare_revision_with_latest = None
        self._compare_revision_with_running = None
        self.discriminator = None
        if compare_latest_with_running is not None:
            self.compare_latest_with_running = compare_latest_with_running
        if compare_revision_with_latest is not None:
            self.compare_revision_with_latest = compare_revision_with_latest
        if compare_revision_with_running is not None:
            self.compare_revision_with_running = compare_revision_with_running

    @property
    def compare_latest_with_running(self):
        """Gets the compare_latest_with_running of this V1AppCompareReq.  # noqa: E501


        :return: The compare_latest_with_running of this V1AppCompareReq.  # noqa: E501
        :rtype: V1CompareLatestWithRunningOption
        """
        return self._compare_latest_with_running

    @compare_latest_with_running.setter
    def compare_latest_with_running(self, compare_latest_with_running):
        """Sets the compare_latest_with_running of this V1AppCompareReq.


        :param compare_latest_with_running: The compare_latest_with_running of this V1AppCompareReq.  # noqa: E501
        :type: V1CompareLatestWithRunningOption
        """

        self._compare_latest_with_running = compare_latest_with_running

    @property
    def compare_revision_with_latest(self):
        """Gets the compare_revision_with_latest of this V1AppCompareReq.  # noqa: E501


        :return: The compare_revision_with_latest of this V1AppCompareReq.  # noqa: E501
        :rtype: V1CompareRevisionWithLatestOption
        """
        return self._compare_revision_with_latest

    @compare_revision_with_latest.setter
    def compare_revision_with_latest(self, compare_revision_with_latest):
        """Sets the compare_revision_with_latest of this V1AppCompareReq.


        :param compare_revision_with_latest: The compare_revision_with_latest of this V1AppCompareReq.  # noqa: E501
        :type: V1CompareRevisionWithLatestOption
        """

        self._compare_revision_with_latest = compare_revision_with_latest

    @property
    def compare_revision_with_running(self):
        """Gets the compare_revision_with_running of this V1AppCompareReq.  # noqa: E501


        :return: The compare_revision_with_running of this V1AppCompareReq.  # noqa: E501
        :rtype: V1CompareRevisionWithRunningOption
        """
        return self._compare_revision_with_running

    @compare_revision_with_running.setter
    def compare_revision_with_running(self, compare_revision_with_running):
        """Sets the compare_revision_with_running of this V1AppCompareReq.


        :param compare_revision_with_running: The compare_revision_with_running of this V1AppCompareReq.  # noqa: E501
        :type: V1CompareRevisionWithRunningOption
        """

        self._compare_revision_with_running = compare_revision_with_running

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
        if issubclass(V1AppCompareReq, dict):
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
        if not isinstance(other, V1AppCompareReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
