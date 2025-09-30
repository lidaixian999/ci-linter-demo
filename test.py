import os
import sys


def hello_world():
    x = 1 + 2
    print("Hello, world!")
    very_long_variable_name_that_exceeds_the_pep8_line_length_limit_by_far = (
        "This line is definitely longer than 79 or even 88 characters, "
        "which violates PEP8."
    )
    return x