"""
"""
import unittest
from src import parse_current_versions


class TestParseRequirements(unittest.TestCase):
    def test_success_parse_requirements(self):
        """
        Test that the requirements file is successfully parsed
        """
        reqs = parse_requirements("./test_requirements.txt")
        self.assertEqual(len(reqs.keys()), 3)

    def test_unsuccess_parse_requirements(self):
        """
        Test that the requirements file is successfully parsed
        """
        reqs = parse_requirements("./test_requirements_bad.txt")
