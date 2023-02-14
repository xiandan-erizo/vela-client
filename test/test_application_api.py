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
from vela_client.api.application_api import ApplicationApi  # noqa: E501
from vela_client.rest import ApiException


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_application_trait(self):
        """Test case for add_application_trait

        add trait for a component  # noqa: E501
        """
        pass

    def test_application_statistics(self):
        """Test case for application_statistics

        detail one application   # noqa: E501
        """
        pass

    def test_compare_app(self):
        """Test case for compare_app

        compare application  # noqa: E501
        """
        pass

    def test_create_application(self):
        """Test case for create_application

        create one application   # noqa: E501
        """
        pass

    def test_create_application_env(self):
        """Test case for create_application_env

        creating an application environment   # noqa: E501
        """
        pass

    def test_create_application_policy(self):
        """Test case for create_application_policy

        create policy for application  # noqa: E501
        """
        pass

    def test_create_application_trigger(self):
        """Test case for create_application_trigger

        create one application trigger  # noqa: E501
        """
        pass

    def test_create_component(self):
        """Test case for create_component

        create component  for application   # noqa: E501
        """
        pass

    def test_create_or_update_application_workflow(self):
        """Test case for create_or_update_application_workflow

        create application workflow  # noqa: E501
        """
        pass

    def test_delete_application(self):
        """Test case for delete_application

        delete one application  # noqa: E501
        """
        pass

    def test_delete_application_env(self):
        """Test case for delete_application_env

        delete an application environment   # noqa: E501
        """
        pass

    def test_delete_application_policy(self):
        """Test case for delete_application_policy

        detail policy for application  # noqa: E501
        """
        pass

    def test_delete_application_trait(self):
        """Test case for delete_application_trait

        delete trait from a component  # noqa: E501
        """
        pass

    def test_delete_application_trigger(self):
        """Test case for delete_application_trigger

        delete one application trigger  # noqa: E501
        """
        pass

    def test_delete_component(self):
        """Test case for delete_component

        delete a component  # noqa: E501
        """
        pass

    def test_delete_workflow(self):
        """Test case for delete_workflow

        deletet workflow  # noqa: E501
        """
        pass

    def test_deploy_application(self):
        """Test case for deploy_application

        deploy or upgrade the application  # noqa: E501
        """
        pass

    def test_detail_application(self):
        """Test case for detail_application

        detail one application   # noqa: E501
        """
        pass

    def test_detail_application_policy(self):
        """Test case for detail_application_policy

        detail policy for application  # noqa: E501
        """
        pass

    def test_detail_application_revision(self):
        """Test case for detail_application_revision

        detail revision for application  # noqa: E501
        """
        pass

    def test_detail_component(self):
        """Test case for detail_component

        detail component for application   # noqa: E501
        """
        pass

    def test_detail_workflow(self):
        """Test case for detail_workflow

        detail application workflow  # noqa: E501
        """
        pass

    def test_detail_workflow_record(self):
        """Test case for detail_workflow_record

        query application workflow execution record detail  # noqa: E501
        """
        pass

    def test_dry_run_app_or_revision(self):
        """Test case for dry_run_app_or_revision

        dry-run application to latest revision  # noqa: E501
        """
        pass

    def test_get_application_status(self):
        """Test case for get_application_status

        get application status  # noqa: E501
        """
        pass

    def test_list_application_components(self):
        """Test case for list_application_components

        gets the list of application components  # noqa: E501
        """
        pass

    def test_list_application_envs(self):
        """Test case for list_application_envs

        list policy for application  # noqa: E501
        """
        pass

    def test_list_application_policies(self):
        """Test case for list_application_policies

        list policy for application  # noqa: E501
        """
        pass

    def test_list_application_records(self):
        """Test case for list_application_records

        list application records  # noqa: E501
        """
        pass

    def test_list_application_revisions(self):
        """Test case for list_application_revisions

        list revisions for application  # noqa: E501
        """
        pass

    def test_list_application_triggers(self):
        """Test case for list_application_triggers

        list application triggers  # noqa: E501
        """
        pass

    def test_list_application_workflows(self):
        """Test case for list_application_workflows

        list application workflow  # noqa: E501
        """
        pass

    def test_list_applications(self):
        """Test case for list_applications

        list all applications  # noqa: E501
        """
        pass

    def test_list_workflow_records(self):
        """Test case for list_workflow_records

        query application workflow execution record  # noqa: E501
        """
        pass

    def test_publish_application_template(self):
        """Test case for publish_application_template

        create one application template  # noqa: E501
        """
        pass

    def test_recycle_application_env(self):
        """Test case for recycle_application_env

        get application status  # noqa: E501
        """
        pass

    def test_reset_app_to_latest_revision(self):
        """Test case for reset_app_to_latest_revision

        reset application to latest revision  # noqa: E501
        """
        pass

    def test_resume_workflow_record(self):
        """Test case for resume_workflow_record

        resume suspend workflow record  # noqa: E501
        """
        pass

    def test_rollback_workflow_record(self):
        """Test case for rollback_workflow_record

        rollback suspend application record  # noqa: E501
        """
        pass

    def test_terminate_workflow_record(self):
        """Test case for terminate_workflow_record

        terminate suspend workflow record  # noqa: E501
        """
        pass

    def test_update_application(self):
        """Test case for update_application

        update one application   # noqa: E501
        """
        pass

    def test_update_application_env(self):
        """Test case for update_application_env

        set application  differences in the specified environment  # noqa: E501
        """
        pass

    def test_update_application_policy(self):
        """Test case for update_application_policy

        update policy for application  # noqa: E501
        """
        pass

    def test_update_application_trait(self):
        """Test case for update_application_trait

        update trait from a component  # noqa: E501
        """
        pass

    def test_update_component(self):
        """Test case for update_component

        update component config  # noqa: E501
        """
        pass

    def test_update_workflow(self):
        """Test case for update_workflow

        update application workflow config  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
