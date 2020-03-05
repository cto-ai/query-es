import json
from math import ceil
import time

from cto_ai import ux, sdk, prompt

slack_max_characters = 2800


def slack_print(s: str) -> None:
    """
    Prints a string in a code block if the Op is ran in Slack, prints normally otherwise
    """
    final_msg = slack_format(s)
    for i in final_msg:
        ux.print(i)


def slack_format(s: str) -> list:
    """
    Formats a string for printing based in Interface Type (Slack or Terminal), returns list of separated blocks
    """
    final_msg = []

    interface = sdk.get_interface_type()
    if interface == "slack":
        i = 0
        while i + slack_max_characters < len(s):
            msg = s[i:i + slack_max_characters]
            final_msg.append('```{}```'.format(msg))
            i += slack_max_characters
        final_msg.append('```{}```'.format(s[i:]))

    else:
        final_msg.append(s)

    return final_msg


def print_for_usability(response) -> None:
    """
    Prints the unformatted response.  If the interface is Slack, prints in 2800 character sections
    """
    raw = str(response.json())
    raw = raw.replace("'", '"')

    interface = sdk.get_interface_type()
    if interface == "slack":
        segments = ceil(len(raw) / slack_max_characters)
        seg_check = prompt.confirm(
            "seg_check",
            "The data will be broken up into {} segments ({} characters each).  Continue with print?".format(
                segments, slack_max_characters)
        )

        if seg_check == False:
            return

    slack_print(raw)


def print_for_readability(response) -> None:
    """
    Formats the response and prints lines depending on the user selection
    """
    raw = response.json()

    full = json.dumps(raw, indent='\t')
    full_length = get_print_length(full)
    partial = prep_partial_output(full)
    partial_length = get_print_length(partial)

    print_choices = [
        "Print preview ({} lines)".format(partial_length),
        "Print everything ({} lines)".format(full_length),
        "Do not print"
    ]
    print_check = prompt.list(
        "print_check",
        "Please select a print option",
        choices=print_choices)

    if print_check == "Do not print":
        return None
    elif print_check == "Print everything ({} lines)".format(full_length):
        slack_print(full)
    else:
        slack_print(partial)


def get_print_length(s: str) -> int:
    """
    Returns number of lines a string object would have if split into a list
    """
    return len(s.splitlines())


def prep_partial_output(full: str) -> str:
    """
    Returns a part of the response formatted for printing
    """
    max_partial = ceil(slack_max_characters/4)
    if len(full) > max_partial:
        partial_data = full[:max_partial]
        if partial_data[0] == "[":
            partial = "{}\n.\n.\n.\n]".format(partial_data)
        else:
            partial = "{}\n.\n.\n.".format(partial_data)

        return partial

    return full
