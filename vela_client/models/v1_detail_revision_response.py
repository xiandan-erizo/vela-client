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

class V1DetailRevisionResponse(object):
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
        'app_primary_key': 'str',
        'apply_app_config': 'str',
        'code_info': 'ModelCodeInfo',
        'create_time': 'datetime',
        'deploy_user': 'V1NameAlias',
        'env_name': 'str',
        'image_info': 'ModelImageInfo',
        'note': 'str',
        'reason': 'str',
        'revision_cr_name': 'str',
        'rollback_version': 'str',
        'status': 'str',
        'trigger_type': 'str',
        'update_time': 'datetime',
        'version': 'str',
        'workflow_name': 'str'
    }

    attribute_map = {
        'app_primary_key': 'appPrimaryKey',
        'apply_app_config': 'applyAppConfig',
        'code_info': 'codeInfo',
        'create_time': 'createTime',
        'deploy_user': 'deployUser',
        'env_name': 'envName',
        'image_info': 'imageInfo',
        'note': 'note',
        'reason': 'reason',
        'revision_cr_name': 'revisionCRName',
        'rollback_version': 'rollbackVersion',
        'status': 'status',
        'trigger_type': 'triggerType',
        'update_time': 'updateTime',
        'version': 'version',
        'workflow_name': 'workflowName'
    }

    def __init__(self, app_primary_key=None, apply_app_config=None, code_info=None, create_time=None, deploy_user=None, env_name=None, image_info=None, note=None, reason=None, revision_cr_name=None, rollback_version=None, status=None, trigger_type=None, update_time=None, version=None, workflow_name=None):  # noqa: E501
        """V1DetailRevisionResponse - a model defined in Swagger"""  # noqa: E501
        self._app_primary_key = None
        self._apply_app_config = None
        self._code_info = None
        self._create_time = None
        self._deploy_user = None
        self._env_name = None
        self._image_info = None
        self._note = None
        self._reason = None
        self._revision_cr_name = None
        self._rollback_version = None
        self._status = None
        self._trigger_type = None
        self._update_time = None
        self._version = None
        self._workflow_name = None
        self.discriminator = None
        self.app_primary_key = app_primary_key
        if apply_app_config is not None:
            self.apply_app_config = apply_app_config
        if code_info is not None:
            self.code_info = code_info
        self.create_time = create_time
        self.deploy_user = deploy_user
        self.env_name = env_name
        if image_info is not None:
            self.image_info = image_info
        self.note = note
        self.reason = reason
        self.revision_cr_name = revision_cr_name
        if rollback_version is not None:
            self.rollback_version = rollback_version
        self.status = status
        self.trigger_type = trigger_type
        self.update_time = update_time
        self.version = version
        self.workflow_name = workflow_name

    @property
    def app_primary_key(self):
        """Gets the app_primary_key of this V1DetailRevisionResponse.  # noqa: E501


        :return: The app_primary_key of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._app_primary_key

    @app_primary_key.setter
    def app_primary_key(self, app_primary_key):
        """Sets the app_primary_key of this V1DetailRevisionResponse.


        :param app_primary_key: The app_primary_key of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if app_primary_key is None:
            raise ValueError("Invalid value for `app_primary_key`, must not be `None`")  # noqa: E501

        self._app_primary_key = app_primary_key

    @property
    def apply_app_config(self):
        """Gets the apply_app_config of this V1DetailRevisionResponse.  # noqa: E501


        :return: The apply_app_config of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._apply_app_config

    @apply_app_config.setter
    def apply_app_config(self, apply_app_config):
        """Sets the apply_app_config of this V1DetailRevisionResponse.


        :param apply_app_config: The apply_app_config of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """

        self._apply_app_config = apply_app_config

    @property
    def code_info(self):
        """Gets the code_info of this V1DetailRevisionResponse.  # noqa: E501


        :return: The code_info of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: ModelCodeInfo
        """
        return self._code_info

    @code_info.setter
    def code_info(self, code_info):
        """Sets the code_info of this V1DetailRevisionResponse.


        :param code_info: The code_info of this V1DetailRevisionResponse.  # noqa: E501
        :type: ModelCodeInfo
        """

        self._code_info = code_info

    @property
    def create_time(self):
        """Gets the create_time of this V1DetailRevisionResponse.  # noqa: E501


        :return: The create_time of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1DetailRevisionResponse.


        :param create_time: The create_time of this V1DetailRevisionResponse.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def deploy_user(self):
        """Gets the deploy_user of this V1DetailRevisionResponse.  # noqa: E501


        :return: The deploy_user of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: V1NameAlias
        """
        return self._deploy_user

    @deploy_user.setter
    def deploy_user(self, deploy_user):
        """Sets the deploy_user of this V1DetailRevisionResponse.


        :param deploy_user: The deploy_user of this V1DetailRevisionResponse.  # noqa: E501
        :type: V1NameAlias
        """
        if deploy_user is None:
            raise ValueError("Invalid value for `deploy_user`, must not be `None`")  # noqa: E501

        self._deploy_user = deploy_user

    @property
    def env_name(self):
        """Gets the env_name of this V1DetailRevisionResponse.  # noqa: E501


        :return: The env_name of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this V1DetailRevisionResponse.


        :param env_name: The env_name of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if env_name is None:
            raise ValueError("Invalid value for `env_name`, must not be `None`")  # noqa: E501

        self._env_name = env_name

    @property
    def image_info(self):
        """Gets the image_info of this V1DetailRevisionResponse.  # noqa: E501


        :return: The image_info of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: ModelImageInfo
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        """Sets the image_info of this V1DetailRevisionResponse.


        :param image_info: The image_info of this V1DetailRevisionResponse.  # noqa: E501
        :type: ModelImageInfo
        """

        self._image_info = image_info

    @property
    def note(self):
        """Gets the note of this V1DetailRevisionResponse.  # noqa: E501


        :return: The note of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this V1DetailRevisionResponse.


        :param note: The note of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def reason(self):
        """Gets the reason of this V1DetailRevisionResponse.  # noqa: E501


        :return: The reason of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1DetailRevisionResponse.


        :param reason: The reason of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def revision_cr_name(self):
        """Gets the revision_cr_name of this V1DetailRevisionResponse.  # noqa: E501


        :return: The revision_cr_name of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._revision_cr_name

    @revision_cr_name.setter
    def revision_cr_name(self, revision_cr_name):
        """Sets the revision_cr_name of this V1DetailRevisionResponse.


        :param revision_cr_name: The revision_cr_name of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if revision_cr_name is None:
            raise ValueError("Invalid value for `revision_cr_name`, must not be `None`")  # noqa: E501

        self._revision_cr_name = revision_cr_name

    @property
    def rollback_version(self):
        """Gets the rollback_version of this V1DetailRevisionResponse.  # noqa: E501


        :return: The rollback_version of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._rollback_version

    @rollback_version.setter
    def rollback_version(self, rollback_version):
        """Sets the rollback_version of this V1DetailRevisionResponse.


        :param rollback_version: The rollback_version of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """

        self._rollback_version = rollback_version

    @property
    def status(self):
        """Gets the status of this V1DetailRevisionResponse.  # noqa: E501


        :return: The status of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1DetailRevisionResponse.


        :param status: The status of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def trigger_type(self):
        """Gets the trigger_type of this V1DetailRevisionResponse.  # noqa: E501


        :return: The trigger_type of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this V1DetailRevisionResponse.


        :param trigger_type: The trigger_type of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if trigger_type is None:
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501

        self._trigger_type = trigger_type

    @property
    def update_time(self):
        """Gets the update_time of this V1DetailRevisionResponse.  # noqa: E501


        :return: The update_time of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1DetailRevisionResponse.


        :param update_time: The update_time of this V1DetailRevisionResponse.  # noqa: E501
        :type: datetime
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def version(self):
        """Gets the version of this V1DetailRevisionResponse.  # noqa: E501


        :return: The version of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1DetailRevisionResponse.


        :param version: The version of this V1DetailRevisionResponse.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def workflow_name(self):
        """Gets the workflow_name of this V1DetailRevisionResponse.  # noqa: E501


        :return: The workflow_name of this V1DetailRevisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this V1DetailRevisionResponse.


        :param workflow_name: The workflow_name of this V1DetailRevisionResponse.  # noqa: E501
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
        if issubclass(V1DetailRevisionResponse, dict):
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
        if not isinstance(other, V1DetailRevisionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other