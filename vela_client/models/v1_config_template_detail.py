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

class V1ConfigTemplateDetail(object):
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
        'description': 'str',
        'name': 'str',
        'namespace': 'str',
        'schema': 'str',
        'scope': 'str',
        'sensitive': 'bool',
        'ui_schema': 'list[UtilsUIParameter]'
    }

    attribute_map = {
        'alias': 'alias',
        'create_time': 'createTime',
        'description': 'description',
        'name': 'name',
        'namespace': 'namespace',
        'schema': 'schema',
        'scope': 'scope',
        'sensitive': 'sensitive',
        'ui_schema': 'uiSchema'
    }

    def __init__(self, alias=None, create_time=None, description=None, name=None, namespace=None, schema=None, scope=None, sensitive=None, ui_schema=None):  # noqa: E501
        """V1ConfigTemplateDetail - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._create_time = None
        self._description = None
        self._name = None
        self._namespace = None
        self._schema = None
        self._scope = None
        self._sensitive = None
        self._ui_schema = None
        self.discriminator = None
        self.alias = alias
        self.create_time = create_time
        self.description = description
        self.name = name
        self.namespace = namespace
        self.schema = schema
        self.scope = scope
        self.sensitive = sensitive
        self.ui_schema = ui_schema

    @property
    def alias(self):
        """Gets the alias of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The alias of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this V1ConfigTemplateDetail.


        :param alias: The alias of this V1ConfigTemplateDetail.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def create_time(self):
        """Gets the create_time of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The create_time of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1ConfigTemplateDetail.


        :param create_time: The create_time of this V1ConfigTemplateDetail.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The description of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ConfigTemplateDetail.


        :param description: The description of this V1ConfigTemplateDetail.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The name of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ConfigTemplateDetail.


        :param name: The name of this V1ConfigTemplateDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The namespace of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1ConfigTemplateDetail.


        :param namespace: The namespace of this V1ConfigTemplateDetail.  # noqa: E501
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def schema(self):
        """Gets the schema of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The schema of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this V1ConfigTemplateDetail.


        :param schema: The schema of this V1ConfigTemplateDetail.  # noqa: E501
        :type: str
        """
        if schema is None:
            raise ValueError("Invalid value for `schema`, must not be `None`")  # noqa: E501

        self._schema = schema

    @property
    def scope(self):
        """Gets the scope of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The scope of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this V1ConfigTemplateDetail.


        :param scope: The scope of this V1ConfigTemplateDetail.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def sensitive(self):
        """Gets the sensitive of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The sensitive of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this V1ConfigTemplateDetail.


        :param sensitive: The sensitive of this V1ConfigTemplateDetail.  # noqa: E501
        :type: bool
        """
        if sensitive is None:
            raise ValueError("Invalid value for `sensitive`, must not be `None`")  # noqa: E501

        self._sensitive = sensitive

    @property
    def ui_schema(self):
        """Gets the ui_schema of this V1ConfigTemplateDetail.  # noqa: E501


        :return: The ui_schema of this V1ConfigTemplateDetail.  # noqa: E501
        :rtype: list[UtilsUIParameter]
        """
        return self._ui_schema

    @ui_schema.setter
    def ui_schema(self, ui_schema):
        """Sets the ui_schema of this V1ConfigTemplateDetail.


        :param ui_schema: The ui_schema of this V1ConfigTemplateDetail.  # noqa: E501
        :type: list[UtilsUIParameter]
        """
        if ui_schema is None:
            raise ValueError("Invalid value for `ui_schema`, must not be `None`")  # noqa: E501

        self._ui_schema = ui_schema

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
        if issubclass(V1ConfigTemplateDetail, dict):
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
        if not isinstance(other, V1ConfigTemplateDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
