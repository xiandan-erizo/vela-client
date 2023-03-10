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

class ModelWorkflowStep(object):
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
        'depends_on': 'list[str]',
        'description': 'str',
        '_if': 'str',
        'inputs': 'list[V1alpha1InputItem]',
        'meta': 'V1alpha1WorkflowStepMeta',
        'name': 'str',
        'order_index': 'int',
        'outputs': 'list[V1alpha1OutputItem]',
        'properties': 'ModelJSONStruct',
        'sub_steps': 'list[ModelWorkflowStepBase]',
        'timeout': 'str',
        'type': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'depends_on': 'dependsOn',
        'description': 'description',
        '_if': 'if',
        'inputs': 'inputs',
        'meta': 'meta',
        'name': 'name',
        'order_index': 'orderIndex',
        'outputs': 'outputs',
        'properties': 'properties',
        'sub_steps': 'subSteps',
        'timeout': 'timeout',
        'type': 'type'
    }

    def __init__(self, alias=None, depends_on=None, description=None, _if=None, inputs=None, meta=None, name=None, order_index=None, outputs=None, properties=None, sub_steps=None, timeout=None, type=None):  # noqa: E501
        """ModelWorkflowStep - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._depends_on = None
        self._description = None
        self.__if = None
        self._inputs = None
        self._meta = None
        self._name = None
        self._order_index = None
        self._outputs = None
        self._properties = None
        self._sub_steps = None
        self._timeout = None
        self._type = None
        self.discriminator = None
        self.alias = alias
        self.depends_on = depends_on
        self.description = description
        if _if is not None:
            self._if = _if
        if inputs is not None:
            self.inputs = inputs
        if meta is not None:
            self.meta = meta
        self.name = name
        self.order_index = order_index
        if outputs is not None:
            self.outputs = outputs
        if properties is not None:
            self.properties = properties
        if sub_steps is not None:
            self.sub_steps = sub_steps
        if timeout is not None:
            self.timeout = timeout
        self.type = type

    @property
    def alias(self):
        """Gets the alias of this ModelWorkflowStep.  # noqa: E501


        :return: The alias of this ModelWorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ModelWorkflowStep.


        :param alias: The alias of this ModelWorkflowStep.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def depends_on(self):
        """Gets the depends_on of this ModelWorkflowStep.  # noqa: E501


        :return: The depends_on of this ModelWorkflowStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this ModelWorkflowStep.


        :param depends_on: The depends_on of this ModelWorkflowStep.  # noqa: E501
        :type: list[str]
        """
        if depends_on is None:
            raise ValueError("Invalid value for `depends_on`, must not be `None`")  # noqa: E501

        self._depends_on = depends_on

    @property
    def description(self):
        """Gets the description of this ModelWorkflowStep.  # noqa: E501


        :return: The description of this ModelWorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelWorkflowStep.


        :param description: The description of this ModelWorkflowStep.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def _if(self):
        """Gets the _if of this ModelWorkflowStep.  # noqa: E501


        :return: The _if of this ModelWorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """Sets the _if of this ModelWorkflowStep.


        :param _if: The _if of this ModelWorkflowStep.  # noqa: E501
        :type: str
        """

        self.__if = _if

    @property
    def inputs(self):
        """Gets the inputs of this ModelWorkflowStep.  # noqa: E501


        :return: The inputs of this ModelWorkflowStep.  # noqa: E501
        :rtype: list[V1alpha1InputItem]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ModelWorkflowStep.


        :param inputs: The inputs of this ModelWorkflowStep.  # noqa: E501
        :type: list[V1alpha1InputItem]
        """

        self._inputs = inputs

    @property
    def meta(self):
        """Gets the meta of this ModelWorkflowStep.  # noqa: E501


        :return: The meta of this ModelWorkflowStep.  # noqa: E501
        :rtype: V1alpha1WorkflowStepMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ModelWorkflowStep.


        :param meta: The meta of this ModelWorkflowStep.  # noqa: E501
        :type: V1alpha1WorkflowStepMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this ModelWorkflowStep.  # noqa: E501


        :return: The name of this ModelWorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelWorkflowStep.


        :param name: The name of this ModelWorkflowStep.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order_index(self):
        """Gets the order_index of this ModelWorkflowStep.  # noqa: E501


        :return: The order_index of this ModelWorkflowStep.  # noqa: E501
        :rtype: int
        """
        return self._order_index

    @order_index.setter
    def order_index(self, order_index):
        """Sets the order_index of this ModelWorkflowStep.


        :param order_index: The order_index of this ModelWorkflowStep.  # noqa: E501
        :type: int
        """
        if order_index is None:
            raise ValueError("Invalid value for `order_index`, must not be `None`")  # noqa: E501

        self._order_index = order_index

    @property
    def outputs(self):
        """Gets the outputs of this ModelWorkflowStep.  # noqa: E501


        :return: The outputs of this ModelWorkflowStep.  # noqa: E501
        :rtype: list[V1alpha1OutputItem]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ModelWorkflowStep.


        :param outputs: The outputs of this ModelWorkflowStep.  # noqa: E501
        :type: list[V1alpha1OutputItem]
        """

        self._outputs = outputs

    @property
    def properties(self):
        """Gets the properties of this ModelWorkflowStep.  # noqa: E501


        :return: The properties of this ModelWorkflowStep.  # noqa: E501
        :rtype: ModelJSONStruct
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ModelWorkflowStep.


        :param properties: The properties of this ModelWorkflowStep.  # noqa: E501
        :type: ModelJSONStruct
        """

        self._properties = properties

    @property
    def sub_steps(self):
        """Gets the sub_steps of this ModelWorkflowStep.  # noqa: E501


        :return: The sub_steps of this ModelWorkflowStep.  # noqa: E501
        :rtype: list[ModelWorkflowStepBase]
        """
        return self._sub_steps

    @sub_steps.setter
    def sub_steps(self, sub_steps):
        """Sets the sub_steps of this ModelWorkflowStep.


        :param sub_steps: The sub_steps of this ModelWorkflowStep.  # noqa: E501
        :type: list[ModelWorkflowStepBase]
        """

        self._sub_steps = sub_steps

    @property
    def timeout(self):
        """Gets the timeout of this ModelWorkflowStep.  # noqa: E501


        :return: The timeout of this ModelWorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ModelWorkflowStep.


        :param timeout: The timeout of this ModelWorkflowStep.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this ModelWorkflowStep.  # noqa: E501


        :return: The type of this ModelWorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelWorkflowStep.


        :param type: The type of this ModelWorkflowStep.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(ModelWorkflowStep, dict):
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
        if not isinstance(other, ModelWorkflowStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
