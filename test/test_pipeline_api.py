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
from vela_client.api.pipeline_api import PipelineApi  # noqa: E501
from vela_client.rest import ApiException


class TestPipelineApi(unittest.TestCase):
    """PipelineApi unit test stubs"""

    def setUp(self):
        self.api = PipelineApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_context_value(self):
        """Test case for create_context_value

        create pipeline context values  # noqa: E501
        """
        pass

    def test_create_pipeline(self):
        """Test case for create_pipeline

        create pipeline  # noqa: E501
        """
        pass

    def test_delete_context_value(self):
        """Test case for delete_context_value

        delete pipeline context value  # noqa: E501
        """
        pass

    def test_delete_pipeline(self):
        """Test case for delete_pipeline

        delete pipeline  # noqa: E501
        """
        pass

    def test_delete_pipeline_run(self):
        """Test case for delete_pipeline_run

        delete pipeline run  # noqa: E501
        """
        pass

    def test_get_pipeline(self):
        """Test case for get_pipeline

        get pipeline  # noqa: E501
        """
        pass

    def test_get_pipeline_run(self):
        """Test case for get_pipeline_run

        get pipeline run  # noqa: E501
        """
        pass

    def test_get_pipeline_run_input(self):
        """Test case for get_pipeline_run_input

        get pipeline run input  # noqa: E501
        """
        pass

    def test_get_pipeline_run_log(self):
        """Test case for get_pipeline_run_log

        get pipeline run log  # noqa: E501
        """
        pass

    def test_get_pipeline_run_output(self):
        """Test case for get_pipeline_run_output

        get pipeline run output  # noqa: E501
        """
        pass

    def test_get_pipeline_run_status(self):
        """Test case for get_pipeline_run_status

        get pipeline run status  # noqa: E501
        """
        pass

    def test_list_context_values(self):
        """Test case for list_context_values

        list pipeline context values  # noqa: E501
        """
        pass

    def test_list_pipeline_runs(self):
        """Test case for list_pipeline_runs

        list pipeline runs  # noqa: E501
        """
        pass

    def test_list_pipelines(self):
        """Test case for list_pipelines

        list pipelines  # noqa: E501
        """
        pass

    def test_resume_pipeline_run(self):
        """Test case for resume_pipeline_run

        resume suspend pipeline run  # noqa: E501
        """
        pass

    def test_run_pipeline(self):
        """Test case for run_pipeline

        run pipeline  # noqa: E501
        """
        pass

    def test_stop_pipeline(self):
        """Test case for stop_pipeline

        stop pipeline run  # noqa: E501
        """
        pass

    def test_terminate_pipeline_run(self):
        """Test case for terminate_pipeline_run

        resume suspend pipeline run  # noqa: E501
        """
        pass

    def test_update_context_value(self):
        """Test case for update_context_value

        update pipeline context value  # noqa: E501
        """
        pass

    def test_update_pipeline(self):
        """Test case for update_pipeline

        update pipeline  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
