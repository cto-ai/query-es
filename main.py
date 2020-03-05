import requests

from cto_ai import ux, prompt

import src.login as login
from src.logos import logo_print
import src.ops_print as ops_print


def login_request(creds):
    """
    Makes a request based on the given credentials
    """
    full_url = creds.url + creds.parameters

    response = requests.request(
        "GET", full_url, headers=creds.headers, data=creds.body)

    return response


def main():
    """
    Prompts user to query ElasticSearch, prints the response
    """
    logo_print()

    # Prompts user for details needed to make a request
    creds = login.Login_credentials()
    try:
        creds.get_url()
        creds.get_specifications()
    except KeyboardInterrupt:
        print("Exiting Op")
        return

    # Makes the request
    try:
        response = login_request(creds)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        err = "Http Error: {}".format(err)
        ux.print(err)
        return
    except requests.exceptions.RequestException as err:
        ux.print("Error: Improper request")
        return
    ux.print(str(response))

    # Prints the response
    try:
        print_for = prompt.list(
            "print_for",
            "How would you like to print the response?",
            choices=["Readability: Indented lines",
                     "Usability: Simple block(s)"]
        )
    except KeyboardInterrupt:
        print("Exiting Op")
        return

    try:
        if print_for == "Usability: Simple block(s)":
            ops_print.print_for_usability(response)
        else:
            ops_print.print_for_readability(response)
    except Exception as e:
        ux.print(e)
        ux.print("Error when printing the response")


if __name__ == "__main__":
    main()
