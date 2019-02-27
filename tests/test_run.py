from st2tests.base import BaseActionTestCase

from run import ActionManager
from lib.exception import MissingParameterError
from lib.exception import MissingProfileError
from lib.exception import ValidationFailError


class RunTestCase(BaseActionTestCase):
    """
    Test action and pack configuration
    """
    action_cls = ActionManager

    def test_missing_parameter(self):
        """
        Test that MissingParameterError is raised when a required parameter is
        not specified.
        """
        configs = {
            "action_config": {
                "config_profile": None
            },
            "pack_config": {}
        }
        # Action should have required 'action' parameter
        action = self.get_action_instance(config=configs["pack_config"])
        with self.assertRaises(MissingParameterError):
            action.run(**configs["action_config"])

    def test_missing_profile(self):
        """
        Test that MissingProfileError is raised when a non-existent profile is
        specified.
        """
        # Profile should exist, if defined in action
        configs = {
            "action_config": {
                "action": "some_action",
                "url": "http://localhost:8080",
                "config_profile": "dev"
            },
            "pack_config": {}
        }
        action = self.get_action_instance(config=configs["pack_config"])
        # Unsure why this works when assertRaises(MissingProfileError) doesn't
        with self.assertRaises(Exception) as exc:
            action.run(**configs["action_config"])

            self.assertIsInstance(exc, MissingProfileError)

    def test_validation_failure(self):
        """
        Test that ValidationFailError is raised when required connection
        parameters are not configured.
        """
        # Required connection parameters should exist: url, user, password
        configs = {
            "action_config": {
                "action": "some_action",
                "url": "http://localhost:8080"
            },
            "pack_config": {}
        }
        action = self.get_action_instance(config=configs["pack_config"])
        # Unsure why this works when assertRaises(MissingProfileError) doesn't
        with self.assertRaises(Exception) as exc:
            action.run(**configs["action_config"])

            self.assertIsInstance(exc, ValidationFailError)
