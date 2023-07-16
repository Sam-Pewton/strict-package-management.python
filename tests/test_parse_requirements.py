"""
Unit tests for parsing current versions
"""
import sys
import unittest
from src import parse_current_versions as pcv


class TestParseRequirements(unittest.TestCase):
    def test_success_parse_requirements(self):
        """
        Test that the requirements file is successfully parsed
        """
        reqs = pcv.parse_requirements_txt("./tests/artifacts/test_requirements.txt")
        self.assertEqual(len(reqs.keys()), 3)

    def test_unsuccess_parse_requirements(self):
        """
        Test that the requirements file raises an indexerror when there are
        version numbers missing
        """
        with self.assertRaises(IndexError):
            reqs = pcv.parse_requirements_txt("./tests/artifacts/test_requirements_bad.txt")
