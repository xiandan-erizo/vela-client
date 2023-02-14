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

class V1ComponentBase(object):
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
        'component_type': 'str',
        'create_time': 'datetime',
        'creator': 'str',
        'depends_on': 'list[str]',
        'description': 'str',
        'icon': 'str',
        'inputs': 'list[V1alpha1InputItem]',
        'labels': 'dict(str, str)',
        'main': 'bool',
        'name': 'str',
        'outputs': 'list[V1alpha1OutputItem]',
        'traits': 'list[V1ApplicationTrait]',
        'update_time': 'datetime',
        'workload_type': 'CommonWorkloadTypeDescriptor'
    }

    attribute_map = {
        'alias': 'alias',
        'component_type': 'componentType',
        'create_time': 'createTime',
        'creator': 'creator',
        'depends_on': 'dependsOn',
        'description': 'description',
        'icon': 'icon',
        'inputs': 'inputs',
        'labels': 'labels',
        'main': 'main',
        'name': 'name',
        'outputs': 'outputs',
        'traits': 'traits',
        'update_time': 'updateTime',
        'workload_type': 'workloadType'
    }

    def __init__(self, alias=None, component_type=None, create_time=None, creator=None, depends_on=None, description=None, icon=None, inputs=None, labels=None, main=None, name=None, outputs=None, traits=None, update_time=None, workload_type=None):  # noqa: E501
        """V1ComponentBase - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._component_type = None
        self._create_time = None
        self._creator = None
        self._depends_on = None
        self._description = None
        self._icon = None
        self._inputs = None
        self._labels = None
        self._main = None
        self._name = None
        self._outputs = None
        self._traits = None
        self._update_time = None
        self._workload_type = None
        self.discriminator = None
        self.alias = alias
        self.component_type = component_type
        self.create_time = create_time
        if creator is not None:
            self.creator = creator
        self.depends_on = depends_on
        self.description = description
        if icon is not None:
            self.icon = icon
        if inputs is not None:
            self.inputs = inputs
        if labels is not None:
            self.labels = labels
        self.main = main
        self.name = name
        if outputs is not None:
            self.outputs = outputs
        self.traits = traits
        self.update_time = update_time
        if workload_type is not None:
            self.workload_type = workload_type

    @property
    def alias(self):
        """Gets the alias of this V1ComponentBase.  # noqa: E501


        :return: The alias of this V1ComponentBase.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1ComponentBase.


        :param alias: The alias of this V1ComponentBase.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def component_type(self):
        """Gets the component_type of this V1ComponentBase.  # noqa: E501


        :return: The component_type of this V1ComponentBase.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this V1ComponentBase.


        :param component_type: The component_type of this V1ComponentBase.  # noqa: E501
        :type: str
        """
        if component_type is None:
            raise ValueError("Invalid value for `component_type`, must not be `None`")  # noqa: E501

        self._component_type = component_type

    @property
    def create_time(self):
        """Gets the create_time of this V1ComponentBase.  # noqa: E501


        :return: The create_time of this V1ComponentBase.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1ComponentBase.


        :param create_time: The create_time of this V1ComponentBase.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this V1ComponentBase.  # noqa: E501


        :return: The creator of this V1ComponentBase.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this V1ComponentBase.


        :param creator: The creator of this V1ComponentBase.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def depends_on(self):
        """Gets the depends_on of this V1ComponentBase.  # noqa: E501


        :return: The depends_on of this V1ComponentBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this V1ComponentBase.


        :param depends_on: The depends_on of this V1ComponentBase.  # noqa: E501
        :type: list[str]
        """
        if depends_on is None:
            raise ValueError("Invalid value for `depends_on`, must not be `None`")  # noqa: E501

        self._depends_on = depends_on

    @property
    def description(self):
        """Gets the description of this V1ComponentBase.  # noqa: E501


        :return: The description of this V1ComponentBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ComponentBase.


        :param description: The description of this V1ComponentBase.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this V1ComponentBase.  # noqa: E501


        :return: The icon of this V1ComponentBase.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this V1ComponentBase.


        :param icon: The icon of this V1ComponentBase.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def inputs(self):
        """Gets the inputs of this V1ComponentBase.  # noqa: E501


        :return: The inputs of this V1ComponentBase.  # noqa: E501
        :rtype: list[V1alpha1InputItem]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this V1ComponentBase.


        :param inputs: The inputs of this V1ComponentBase.  # noqa: E501
        :type: list[V1alpha1InputItem]
        """

        self._inputs = inputs

    @property
    def labels(self):
        """Gets the labels of this V1ComponentBase.  # noqa: E501


        :return: The labels of this V1ComponentBase.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1ComponentBase.


        :param labels: The labels of this V1ComponentBase.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def main(self):
        """Gets the main of this V1ComponentBase.  # noqa: E501


        :return: The main of this V1ComponentBase.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this V1ComponentBase.


        :param main: The main of this V1ComponentBase.  # noqa: E501
        :type: bool
        """
        if main is None:
            raise ValueError("Invalid value for `main`, must not be `None`")  # noqa: E501

        self._main = main

    @property
    def name(self):
        """Gets the name of this V1ComponentBase.  # noqa: E501


        :return: The name of this V1ComponentBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ComponentBase.


        :param name: The name of this V1ComponentBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this V1ComponentBase.  # noqa: E501


        :return: The outputs of this V1ComponentBase.  # noqa: E501
        :rtype: list[V1alpha1OutputItem]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this V1ComponentBase.


        :param outputs: The outputs of this V1ComponentBase.  # noqa: E501
        :type: list[V1alpha1OutputItem]
        """

        self._outputs = outputs

    @property
    def traits(self):
        """Gets the traits of this V1ComponentBase.  # noqa: E501


        :return: The traits of this V1ComponentBase.  # noqa: E501
        :rtype: list[V1ApplicationTrait]
        """
        return self._traits

    @traits.setter
    def traits(self, traits):
        """Sets the traits of this V1ComponentBase.


        :param traits: The traits of this V1ComponentBase.  # noqa: E501
        :type: list[V1ApplicationTrait]
        """
        if traits is None:
            raise ValueError("Invalid value for `traits`, must not be `None`")  # noqa: E501

        self._traits = traits

    @property
    def update_time(self):
        """Gets the update_time of this V1ComponentBase.  # noqa: E501


        :return: The update_time of this V1ComponentBase.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1ComponentBase.


        :param update_time: The update_time of this V1ComponentBase.  # noqa: E501
        :type: datetime
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def workload_type(self):
        """Gets the workload_type of this V1ComponentBase.  # noqa: E501


        :return: The workload_type of this V1ComponentBase.  # noqa: E501
        :rtype: CommonWorkloadTypeDescriptor
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """Sets the workload_type of this V1ComponentBase.


        :param workload_type: The workload_type of this V1ComponentBase.  # noqa: E501
        :type: CommonWorkloadTypeDescriptor
        """

        self._workload_type = workload_type

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
        if issubclass(V1ComponentBase, dict):
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
        if not isinstance(other, V1ComponentBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other