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

class V1ApplicationDeployRequest(object):
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
        'code_info': 'ModelCodeInfo',
        'force': 'bool',
        'image_info': 'ModelImageInfo',
        'note': 'str',
        'trigger_type': 'str',
        'workflow_name': 'str'
    }

    attribute_map = {
        'code_info': 'codeInfo',
        'force': 'force',
        'image_info': 'imageInfo',
        'note': 'note',
        'trigger_type': 'triggerType',
        'workflow_name': 'workflowName'
    }

    def __init__(self, code_info=None, force=None, image_info=None, note=None, trigger_type=None, workflow_name=None):  # noqa: E501
        """V1ApplicationDeployRequest - a model defined in Swagger"""  # noqa: E501
        self._code_info = None
        self._force = None
        self._image_info = None
        self._note = None
        self._trigger_type = None
        self._workflow_name = None
        self.discriminator = None
        if code_info is not None:
            self.code_info = code_info
        self.force = force
        if image_info is not None:
            self.image_info = image_info
        self.note = note
        self.trigger_type = trigger_type
        self.workflow_name = workflow_name

    @property
    def code_info(self):
        """Gets the code_info of this V1ApplicationDeployRequest.  # noqa: E501


        :return: The code_info of this V1ApplicationDeployRequest.  # noqa: E501
        :rtype: ModelCodeInfo
        """
        return self._code_info

    @code_info.setter
    def code_info(self, code_info):
        """Sets the code_info of this V1ApplicationDeployRequest.


        :param code_info: The code_info of this V1ApplicationDeployRequest.  # noqa: E501
        :type: ModelCodeInfo
        """

        self._code_info = code_info

    @property
    def force(self):
        """Gets the force of this V1ApplicationDeployRequest.  # noqa: E501


        :return: The force of this V1ApplicationDeployRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this V1ApplicationDeployRequest.


        :param force: The force of this V1ApplicationDeployRequest.  # noqa: E501
        :type: bool
        """
        if force is None:
            raise ValueError("Invalid value for `force`, must not be `None`")  # noqa: E501

        self._force = force

    @property
    def image_info(self):
        """Gets the image_info of this V1ApplicationDeployRequest.  # noqa: E501


        :return: The image_info of this V1ApplicationDeployRequest.  # noqa: E501
        :rtype: ModelImageInfo
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        """Sets the image_info of this V1ApplicationDeployRequest.


        :param image_info: The image_info of this V1ApplicationDeployRequest.  # noqa: E501
        :type: ModelImageInfo
        """

        self._image_info = image_info

    @property
    def note(self):
        """Gets the note of this V1ApplicationDeployRequest.  # noqa: E501


        :return: The note of this V1ApplicationDeployRequest.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this V1ApplicationDeployRequest.


        :param note: The note of this V1ApplicationDeployRequest.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def trigger_type(self):
        """Gets the trigger_type of this V1ApplicationDeployRequest.  # noqa: E501


        :return: The trigger_type of this V1ApplicationDeployRequest.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this V1ApplicationDeployRequest.


        :param trigger_type: The trigger_type of this V1ApplicationDeployRequest.  # noqa: E501
        :type: str
        """
        if trigger_type is None:
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501

        self._trigger_type = trigger_type

    @property
    def workflow_name(self):
        """Gets the workflow_name of this V1ApplicationDeployRequest.  # noqa: E501


        :return: The workflow_name of this V1ApplicationDeployRequest.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this V1ApplicationDeployRequest.


        :param workflow_name: The workflow_name of this V1ApplicationDeployRequest.  # noqa: E501
        :type: str
        """
        if workflow_name is None:
            raise ValueError("Invalid value for `workflow_name`, must not be `None`")  # noqa: E501

        self._workflow_name = workflow_name

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
        if issubclass(V1ApplicationDeployRequest, dict):
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
        if not isinstance(other, V1ApplicationDeployRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
