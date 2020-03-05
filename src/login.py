import json
from math import floor

from cto_ai import prompt, sdk


class Login_credentials():

    def __init__(self):
        self.url = ''
        self.body = ''
        self.headers = {}
        self.parameters = ''

    def get_url(self):
        """
        Prompts user to enter a url
        """
        url = prompt.input(
            "url", "Please enter URL (Enter Secret to use Ops Secrets)")
        if url == "Secret":
            url = prompt.secret("secret_url", "Please enter Secret Url")

        self.url = url

    def get_body(self):
        """
        Prompts user to enter their query body
        """
        self.body = prompt.editor("body", "Please enter Query Body")

    def get_headers(self) -> dict:
        """
        Prompt user to enter their request headers
        """
        add_key = True
        while add_key:
            key = prompt.input("key", "Please enter Header Key")
            value = prompt.input(
                "value", "Please enter Value for key {:s}".format(key))

            self.headers[key] = value

            add_key = prompt.confirm("add_key", "Add another Header?")

    def get_parameters(self) -> str:
        """
        Gets parameters for refining the query
        """
        parameter_holder = self.enter_parameters()
        params = self.convert_parameters_to_string(parameter_holder)

        self.parameters = params

    def enter_parameters(self) -> dict:
        """
        Prompts user to enter parameters
        """
        parameter_holder = {}

        add_key = True
        while add_key:
            key = prompt.input("key", "Please enter Parameter Key")
            value = prompt.input(
                "value", "Please enter Value for key {:s}".format(key))

            parameter_holder[key] = value

            add_key = prompt.confirm("add_key", "Add another Parameter?")

        return parameter_holder

    def convert_parameters_to_string(self, parameter_holder: dict) -> str:
        """
        Converts the parameter_holder dict to a usable string
        """
        params = "?"
        for key, value in parameter_holder.items():
            params += '{}={}&'.format(key, value)

        return params[:-1]

    def get_specifications(self):
        """
        Loop for getting the Body, Headers, and Parameters
        """
        status = True
        while status:
            more = prompt.list(
                "more",
                "Enter additional specifications?",
                choices=["Body", "Headers", "Parameters", "Continue"])

            if more == "Body":
                self.get_body()
            if more == "Headers":
                self.get_headers()
            if more == "Parameters":
                self.get_parameters()
            if more == "Continue":
                break
