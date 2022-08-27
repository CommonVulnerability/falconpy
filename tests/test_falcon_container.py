"""
test_falcon_container.py - This class tests the falcon_container service class
"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FalconContainer, APIHarness

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FalconContainer(auth_object=config)
uber = APIHarness(client_id=falcon.auth_object.creds["client_id"],
                  client_secret=falcon.auth_object.creds["client_secret"],
                  base_url=falcon.auth_object.base_url
                  )
AllowedResponses = [200, 201, 400, 403, 404, 429]  # Allowing 400 for now


class TestFalconContainer:
    def run_tests(self):
        error_checks = True

        tests = {
            "GetAssessment": falcon.get_assessment(repository="whatever", tag="whatever"),
            "DeleteImageDetails": falcon.delete_image_details("whatever"),
            "ImageMatchesPolicy": falcon.image_matches_policy(repository="whatever", tag="whatever", body={}),
            "GetAssessmentUber": uber.command("GetImageAssessmentReport", repository="whatever", tag="whatever"),
            "DeleteImageDetailsUber": uber.command("DeleteImageDetails", image_id="12345678"),
            "ImageMatchesPolicyUber": uber.command("ImageMatchesPolicy", repository="whatever", tag="whatever")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(tests[key])
                # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    def test_get_credentials(self):
        """Pytest harness hook"""
        assert bool(falcon.get_credentials()["status_code"] in AllowedResponses) is True

    def test_remaining_code_paths(self):
        """Pytest harness hook"""
        assert self.run_tests() is True
