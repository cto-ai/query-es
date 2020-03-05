import ops_print
from unittest import TestCase
from unittest.mock import patch
import json

from cto_ai import sdk

import sys
import os
sys.path.append(os.path.abspath('../src'))


class ops_print_test(TestCase):
    @patch('cto_ai.sdk.get_interface_type', return_value="terminal")
    def test_slack_format_in_terminal(self, mock_prompt):
        test_msg = ops_print.slack_format("test")
        self.assertEqual(test_msg, ["test"])

    @patch('cto_ai.sdk.get_interface_type', return_value="slack")
    def test_slack_format_in_slack(self, mock_prompt):
        test_msg = ops_print.slack_format("test")
        self.assertEqual(test_msg, ["```test```"])

    @patch('cto_ai.sdk.get_interface_type', return_value="slack")
    def test_slack_format_in_slack_large(self, mock_prompt):
        a = "a" * 2801  # 2800 is the max print size I am allowing for one block in Slack
        test_msg = ops_print.slack_format(a)
        self.assertEqual(len(test_msg), 2)

    def test_get_print_length(self):
        test_string = "a\nb"
        test_length = ops_print.get_print_length(test_string)
        self.assertEqual(test_length, 2)

    def test_prep_partial_output(self):
        a = "a" * 500
        b = "b" * 500
        test_json = {
            "a": a,
            "b": b
        }
        test_full = json.dumps(test_json, indent='\t')

        test_partial = ops_print.prep_partial_output(test_full)
        # 700 chars from the data + \n.\n.\n.
        self.assertEqual(len(test_partial), 706)

    def test_prep_partial_output_list(self):
        a = "a" * 500
        b = "b" * 500
        test_json = [{
            "a": a,
            "b": b
        }]
        test_full = json.dumps(test_json, indent='\t')

        test_partial = ops_print.prep_partial_output(test_full)
        # 700 chars from the data + \n.\n.\n.\n]
        self.assertEqual(len(test_partial), 708)
        self.assertEqual(test_partial[-1], ']')
