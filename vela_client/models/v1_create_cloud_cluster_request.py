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

class V1CreateCloudClusterRequest(object):
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
        'access_key_id': 'str',
        'access_key_secret': 'str',
        'cpu_cores_per_worker': 'int',
        'memory_per_worker': 'int',
        'name': 'str',
        'worker_number': 'int',
        'zone': 'str'
    }

    attribute_map = {
        'access_key_id': 'accessKeyID',
        'access_key_secret': 'accessKeySecret',
        'cpu_cores_per_worker': 'cpuCoresPerWorker',
        'memory_per_worker': 'memoryPerWorker',
        'name': 'name',
        'worker_number': 'workerNumber',
        'zone': 'zone'
    }

    def __init__(self, access_key_id=None, access_key_secret=None, cpu_cores_per_worker=None, memory_per_worker=None, name=None, worker_number=None, zone=None):  # noqa: E501
        """V1CreateCloudClusterRequest - a model defined in Swagger"""  # noqa: E501
        self._access_key_id = None
        self._access_key_secret = None
        self._cpu_cores_per_worker = None
        self._memory_per_worker = None
        self._name = None
        self._worker_number = None
        self._zone = None
        self.discriminator = None
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.cpu_cores_per_worker = cpu_cores_per_worker
        self.memory_per_worker = memory_per_worker
        self.name = name
        self.worker_number = worker_number
        self.zone = zone

    @property
    def access_key_id(self):
        """Gets the access_key_id of this V1CreateCloudClusterRequest.  # noqa: E501


        :return: The access_key_id of this V1CreateCloudClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this V1CreateCloudClusterRequest.


        :param access_key_id: The access_key_id of this V1CreateCloudClusterRequest.  # noqa: E501
        :type: str
        """
        if access_key_id is None:
            raise ValueError("Invalid value for `access_key_id`, must not be `None`")  # noqa: E501

        self._access_key_id = access_key_id

    @property
    def access_key_secret(self):
        """Gets the access_key_secret of this V1CreateCloudClusterRequest.  # noqa: E501


        :return: The access_key_secret of this V1CreateCloudClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_key_secret

    @access_key_secret.setter
    def access_key_secret(self, access_key_secret):
        """Sets the access_key_secret of this V1CreateCloudClusterRequest.


        :param access_key_secret: The access_key_secret of this V1CreateCloudClusterRequest.  # noqa: E501
        :type: str
        """
        if access_key_secret is None:
            raise ValueError("Invalid value for `access_key_secret`, must not be `None`")  # noqa: E501

        self._access_key_secret = access_key_secret

    @property
    def cpu_cores_per_worker(self):
        """Gets the cpu_cores_per_worker of this V1CreateCloudClusterRequest.  # noqa: E501


        :return: The cpu_cores_per_worker of this V1CreateCloudClusterRequest.  # noqa: E501
        :rtype: int
        """
        return self._cpu_cores_per_worker

    @cpu_cores_per_worker.setter
    def cpu_cores_per_worker(self, cpu_cores_per_worker):
        """Sets the cpu_cores_per_worker of this V1CreateCloudClusterRequest.


        :param cpu_cores_per_worker: The cpu_cores_per_worker of this V1CreateCloudClusterRequest.  # noqa: E501
        :type: int
        """
        if cpu_cores_per_worker is None:
            raise ValueError("Invalid value for `cpu_cores_per_worker`, must not be `None`")  # noqa: E501

        self._cpu_cores_per_worker = cpu_cores_per_worker

    @property
    def memory_per_worker(self):
        """Gets the memory_per_worker of this V1CreateCloudClusterRequest.  # noqa: E501


        :return: The memory_per_worker of this V1CreateCloudClusterRequest.  # noqa: E501
        :rtype: int
        """
        return self._memory_per_worker

    @memory_per_worker.setter
    def memory_per_worker(self, memory_per_worker):
        """Sets the memory_per_worker of this V1CreateCloudClusterRequest.


        :param memory_per_worker: The memory_per_worker of this V1CreateCloudClusterRequest.  # noqa: E501
        :type: int
        """
        if memory_per_worker is None:
            raise ValueError("Invalid value for `memory_per_worker`, must not be `None`")  # noqa: E501

        self._memory_per_worker = memory_per_worker

    @property
    def name(self):
        """Gets the name of this V1CreateCloudClusterRequest.  # noqa: E501


        :return: The name of this V1CreateCloudClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CreateCloudClusterRequest.


        :param name: The name of this V1CreateCloudClusterRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def worker_number(self):
        """Gets the worker_number of this V1CreateCloudClusterRequest.  # noqa: E501


        :return: The worker_number of this V1CreateCloudClusterRequest.  # noqa: E501
        :rtype: int
        """
        return self._worker_number

    @worker_number.setter
    def worker_number(self, worker_number):
        """Sets the worker_number of this V1CreateCloudClusterRequest.


        :param worker_number: The worker_number of this V1CreateCloudClusterRequest.  # noqa: E501
        :type: int
        """
        if worker_number is None:
            raise ValueError("Invalid value for `worker_number`, must not be `None`")  # noqa: E501

        self._worker_number = worker_number

    @property
    def zone(self):
        """Gets the zone of this V1CreateCloudClusterRequest.  # noqa: E501


        :return: The zone of this V1CreateCloudClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this V1CreateCloudClusterRequest.


        :param zone: The zone of this V1CreateCloudClusterRequest.  # noqa: E501
        :type: str
        """
        if zone is None:
            raise ValueError("Invalid value for `zone`, must not be `None`")  # noqa: E501

        self._zone = zone

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
        if issubclass(V1CreateCloudClusterRequest, dict):
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
        if not isinstance(other, V1CreateCloudClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
