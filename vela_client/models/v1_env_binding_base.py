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

class V1EnvBindingBase(object):
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
        'app_deploy_name': 'str',
        'app_deploy_namespace': 'str',
        'component_selector': 'V1ComponentSelector',
        'create_time': 'datetime',
        'description': 'str',
        'name': 'str',
        'target_names': 'list[str]',
        'targets': 'list[V1EnvBindingTarget]',
        'update_time': 'datetime'
    }

    attribute_map = {
        'alias': 'alias',
        'app_deploy_name': 'appDeployName',
        'app_deploy_namespace': 'appDeployNamespace',
        'component_selector': 'componentSelector',
        'create_time': 'createTime',
        'description': 'description',
        'name': 'name',
        'target_names': 'targetNames',
        'targets': 'targets',
        'update_time': 'updateTime'
    }

    def __init__(self, alias=None, app_deploy_name=None, app_deploy_namespace=None, component_selector=None, create_time=None, description=None, name=None, target_names=None, targets=None, update_time=None):  # noqa: E501
        """V1EnvBindingBase - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._app_deploy_name = None
        self._app_deploy_namespace = None
        self._component_selector = None
        self._create_time = None
        self._description = None
        self._name = None
        self._target_names = None
        self._targets = None
        self._update_time = None
        self.discriminator = None
        if alias is not None:
            self.alias = alias
        self.app_deploy_name = app_deploy_name
        self.app_deploy_namespace = app_deploy_namespace
        if component_selector is not None:
            self.component_selector = component_selector
        self.create_time = create_time
        if description is not None:
            self.description = description
        self.name = name
        self.target_names = target_names
        if targets is not None:
            self.targets = targets
        self.update_time = update_time

    @property
    def alias(self):
        """Gets the alias of this V1EnvBindingBase.  # noqa: E501


        :return: The alias of this V1EnvBindingBase.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1EnvBindingBase.


        :param alias: The alias of this V1EnvBindingBase.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def app_deploy_name(self):
        """Gets the app_deploy_name of this V1EnvBindingBase.  # noqa: E501


        :return: The app_deploy_name of this V1EnvBindingBase.  # noqa: E501
        :rtype: str
        """
        return self._app_deploy_name

    @app_deploy_name.setter
    def app_deploy_name(self, app_deploy_name):
        """Sets the app_deploy_name of this V1EnvBindingBase.


        :param app_deploy_name: The app_deploy_name of this V1EnvBindingBase.  # noqa: E501
        :type: str
        """
        if app_deploy_name is None:
            raise ValueError("Invalid value for `app_deploy_name`, must not be `None`")  # noqa: E501

        self._app_deploy_name = app_deploy_name

    @property
    def app_deploy_namespace(self):
        """Gets the app_deploy_namespace of this V1EnvBindingBase.  # noqa: E501


        :return: The app_deploy_namespace of this V1EnvBindingBase.  # noqa: E501
        :rtype: str
        """
        return self._app_deploy_namespace

    @app_deploy_namespace.setter
    def app_deploy_namespace(self, app_deploy_namespace):
        """Sets the app_deploy_namespace of this V1EnvBindingBase.


        :param app_deploy_namespace: The app_deploy_namespace of this V1EnvBindingBase.  # noqa: E501
        :type: str
        """
        if app_deploy_namespace is None:
            raise ValueError("Invalid value for `app_deploy_namespace`, must not be `None`")  # noqa: E501

        self._app_deploy_namespace = app_deploy_namespace

    @property
    def component_selector(self):
        """Gets the component_selector of this V1EnvBindingBase.  # noqa: E501


        :return: The component_selector of this V1EnvBindingBase.  # noqa: E501
        :rtype: V1ComponentSelector
        """
        return self._component_selector

    @component_selector.setter
    def component_selector(self, component_selector):
        """Sets the component_selector of this V1EnvBindingBase.


        :param component_selector: The component_selector of this V1EnvBindingBase.  # noqa: E501
        :type: V1ComponentSelector
        """

        self._component_selector = component_selector

    @property
    def create_time(self):
        """Gets the create_time of this V1EnvBindingBase.  # noqa: E501


        :return: The create_time of this V1EnvBindingBase.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1EnvBindingBase.


        :param create_time: The create_time of this V1EnvBindingBase.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this V1EnvBindingBase.  # noqa: E501


        :return: The description of this V1EnvBindingBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1EnvBindingBase.


        :param description: The description of this V1EnvBindingBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this V1EnvBindingBase.  # noqa: E501


        :return: The name of this V1EnvBindingBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1EnvBindingBase.


        :param name: The name of this V1EnvBindingBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target_names(self):
        """Gets the target_names of this V1EnvBindingBase.  # noqa: E501


        :return: The target_names of this V1EnvBindingBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_names

    @target_names.setter
    def target_names(self, target_names):
        """Sets the target_names of this V1EnvBindingBase.


        :param target_names: The target_names of this V1EnvBindingBase.  # noqa: E501
        :type: list[str]
        """
        if target_names is None:
            raise ValueError("Invalid value for `target_names`, must not be `None`")  # noqa: E501

        self._target_names = target_names

    @property
    def targets(self):
        """Gets the targets of this V1EnvBindingBase.  # noqa: E501


        :return: The targets of this V1EnvBindingBase.  # noqa: E501
        :rtype: list[V1EnvBindingTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this V1EnvBindingBase.


        :param targets: The targets of this V1EnvBindingBase.  # noqa: E501
        :type: list[V1EnvBindingTarget]
        """

        self._targets = targets

    @property
    def update_time(self):
        """Gets the update_time of this V1EnvBindingBase.  # noqa: E501


        :return: The update_time of this V1EnvBindingBase.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1EnvBindingBase.


        :param update_time: The update_time of this V1EnvBindingBase.  # noqa: E501
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
        if issubclass(V1EnvBindingBase, dict):
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
        if not isinstance(other, V1EnvBindingBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other