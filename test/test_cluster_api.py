# coding: utf-8

"""
    Kubevela api doc

    Kubevela api doc  # noqa: E501

    OpenAPI spec version: v1beta1
    Contact: feedback@mail.kubevela.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vela_client
from vela_client.api.cluster_api import ClusterApi  # noqa: E501
from vela_client.rest import ApiException


class TestClusterApi(unittest.TestCase):
    """ClusterApi unit test stubs"""

    def setUp(self):
        self.api = ClusterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_connect_cloud_cluster(self):
        """Test case for connect_cloud_cluster

        create cluster from cloud cluster  # noqa: E501
        """
        pass

    def test_create_cloud_cluster(self):
        """Test case for create_cloud_cluster

        create cloud cluster  # noqa: E501
        """
        pass

    def test_create_kube_cluster(self):
        """Test case for create_kube_cluster

        create cluster  # noqa: E501
        """
        pass

    def test_create_namespace(self):
        """Test case for create_namespace

        create namespace in cluster  # noqa: E501
        """
        pass

    def test_delete_cloud_cluster_creation(self):
        """Test case for delete_cloud_cluster_creation

        delete cloud cluster creation  # noqa: E501
        """
        pass

    def test_delete_kube_cluster(self):
        """Test case for delete_kube_cluster

        delete cluster  # noqa: E501
        """
        pass

    def test_get_cloud_cluster_creation_status(self):
        """Test case for get_cloud_cluster_creation_status

        check cloud cluster create status  # noqa: E501
        """
        pass

    def test_get_kube_cluster(self):
        """Test case for get_kube_cluster

        detail cluster info  # noqa: E501
        """
        pass

    def test_list_cloud_cluster_creation(self):
        """Test case for list_cloud_cluster_creation

        list cloud cluster creation  # noqa: E501
        """
        pass

    def test_list_cloud_clusters(self):
        """Test case for list_cloud_clusters

        list cloud clusters  # noqa: E501
        """
        pass

    def test_list_kube_clusters(self):
        """Test case for list_kube_clusters

        list all clusters  # noqa: E501
        """
        pass

    def test_modify_kube_cluster(self):
        """Test case for modify_kube_cluster

        modify cluster  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
