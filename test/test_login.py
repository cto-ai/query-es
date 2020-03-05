from unittest import TestCase
from unittest.mock import patch

from cto_ai import prompt, sdk

import sys
import os
sys.path.append(os.path.abspath('../src'))
import login

class login_test(TestCase):
    def test_login(self):
        test_login = login.Login_credentials()
        self.assertEqual(test_login.url, "")
        self.assertEqual(test_login.body, "")
        self.assertEqual(test_login.headers, {})
        self.assertEqual(test_login.parameters, "")
    
    #URL
    @patch('cto_ai.prompt.input', return_value="url")
    def test_get_url(self, mock_prompt):
        test_login = login.Login_credentials()
        test_login.get_url()
        self.assertEqual(test_login.url, "url")

    @patch('cto_ai.prompt.input', return_value="Secret")
    @patch('cto_ai.prompt.secret', return_value="url")
    def test_get_url_secret(self, mock_prompt1, mock_prompt2):
        test_login = login.Login_credentials()
        test_login.get_url()
        self.assertEqual(test_login.url, "url")
    
    #Body
    @patch('cto_ai.prompt.editor', return_value="body")
    def test_get_body(self, mock_prompt):
        test_login = login.Login_credentials()
        test_login.get_body()
        self.assertEqual(test_login.body, "body")

    #Headers
    @patch('cto_ai.prompt.input', return_value="header")
    @patch('cto_ai.prompt.confirm', return_value=False)
    def test_get_headers(self, mock_prompt1, mock_prompt2):
        test_login = login.Login_credentials()
        test_login.get_headers()
        self.assertEqual(test_login.headers, {"header": "header"})

    #Parameters
    @patch('cto_ai.prompt.input', return_value="param")
    @patch('cto_ai.prompt.confirm', return_value=False)
    def test_get_parameter(self, mock_prompt1, mock_prompt2):
        test_login = login.Login_credentials()
        test_login.get_parameters()
        self.assertEqual(test_login.parameters, '?param=param')

    
    
    
    


